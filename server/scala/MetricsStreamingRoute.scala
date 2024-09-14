package com.metrics

import akka.actor.{ActorRef, ActorSystem, Props}
import akka.http.scaladsl.model.headers.RawHeader
import akka.http.scaladsl.model.sse.ServerSentEvent
import akka.http.scaladsl.server.{Directive0, Directive1, Directives, Route}
import akka.http.scaladsl.unmarshalling.FromRequestUnmarshaller
import akka.stream.OverflowStrategy
import akka.stream.scaladsl.Source
import com.metrics.MetricsStreamingActor._

import scala.concurrent.Future
import scala.concurrent.duration.{Duration, DurationInt}
import scala.util.{Failure, Success}

object MetricsStreamingRoute extends Directives {
  implicit val actorSystem: ActorSystem = ActorSystem("metrics_streaming")
  import actorSystem.dispatcher
  import akka.http.scaladsl.marshalling.sse.EventStreamMarshalling._
  val metricsStreamingActor: ActorRef = actorSystem.actorOf(Props(new MetricsStreamingActor))

  actorSystem.scheduler.scheduleWithFixedDelay(Duration.Zero, 300.milliseconds, metricsStreamingActor, Tick)
  def streamRoute: Route =
    path("metrics-stream") {
      respondWithHeader(RawHeader("Access-Control-Allow-Origin", "*")) {
        get {
          complete {
            val (queue, source) = Source.queue[ServerSentEvent](10000, OverflowStrategy.dropHead).preMaterialize()
            metricsStreamingActor ! NewConnection(queue)
            source.keepAlive(30.second, () => ServerSentEvent.heartbeat)
          }
        }
      }
    }

  val routes: Route = streamRoute

  def measure[T](id: String, parent: String = null)(block: => T): T = {
    val startTime = System.nanoTime()
    val result = block
    val endTime = System.nanoTime()
    metricsStreamingActor ! LogMetric(id, parent, (startTime, endTime))
    result
  }

  def measureAsync[T](id: String, parent: String = null)(block: => Future[T]): Future[T] = {
    val startTime = System.nanoTime()
    val result = block
    result
      .recover {
        case exception =>
          val endTime = System.nanoTime()
          metricsStreamingActor ! LogMetric(id + s"FAILED ${exception.getMessage}", parent, startEndTimes = (startTime, endTime))
      }

    result
      .foreach {
        _ => {
          val endTime = System.nanoTime()
          metricsStreamingActor ! LogMetric(id, parent, startEndTimes = (startTime, endTime))
        }
      }
    result
  }

  def timedSerialization[T](id: String)(um: FromRequestUnmarshaller[T]): Directive1[T] = {
    val startTime = System.nanoTime()
    entity(um).flatMap {
      deserializedEntity =>
        val endTime = System.nanoTime()
        metricsStreamingActor ! LogMetric(s"Timed serialization of ${id}", parent = null, startEndTimes = (startTime, endTime))
        provide(deserializedEntity)
    }
  }

  def measureRoute(id: String, startTime: Long = System.nanoTime()): Directive0 = {
    mapRouteResult {
      routeResult => {
        val endTime = System.nanoTime()
        metricsStreamingActor ! LogMetric(id = s"Route $id", parent = null, startEndTimes = (startTime, endTime))
        routeResult
      }
    }
  }
}

