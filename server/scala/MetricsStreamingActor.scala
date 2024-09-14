package com.metrics

import akka.actor.Actor
import akka.http.scaladsl.model.sse.ServerSentEvent
import akka.stream.scaladsl.SourceQueueWithComplete
import com.metrics.MetricsStreamingActor._
import spray.json.DefaultJsonProtocol

import scala.concurrent.ExecutionContext

class MetricsStreamingActor(implicit val ec: ExecutionContext) extends Actor with DefaultJsonProtocol {
  import spray.json._
  case class Metric(
                     id: String,
                     parent: String,
                     startEndTimes: (Long, Long)
                   )
  def writer(metric: Metric): JsValue = JsObject(
    "parent" -> {if (metric.parent == null) JsNull else JsString(metric.parent)},
    "id" -> JsString(metric.id),
    "start_end_times" -> metric.startEndTimes.toJson
  ).toJson

  private var connection = Option.empty[SourceQueueWithComplete[ServerSentEvent]]
  private var metrics = List.empty[Metric]

  var obsolete: Boolean = true
  var lastMessageDeliveredAtTimestmap: Long = System.currentTimeMillis()

  def pushDownStream(): Unit = {
    obsolete = false
    connection.foreach {
      queue =>
        queue.offer(
          ServerSentEvent(JsArray(metrics.map(writer):_*).toString)
        )
        metrics = List.empty[Metric]
        lastMessageDeliveredAtTimestmap = System.currentTimeMillis()
    }
  }

  override def receive: Receive = {
    case NewConnection(queue) =>
      connection.foreach(_.complete())
      connection = Some(queue)
      metrics = List.empty[Metric]
      queue.watchCompletion()
        .onComplete(_ => {
          metrics = List.empty[Metric]
//          connection = Option.empty
        })

    case LogMetric(id, parent, startEndTimes) =>
      if (connection.isDefined) {
        obsolete = true
        metrics = metrics :+ Metric(id = id, parent = parent, startEndTimes = startEndTimes)
        if (System.currentTimeMillis() - lastMessageDeliveredAtTimestmap > 500) {
          pushDownStream()
        }
      }

    case Tick =>
      if (obsolete) pushDownStream()
  }
}

object MetricsStreamingActor {
  case class NewConnection(queue: SourceQueueWithComplete[ServerSentEvent])
  case class LogMetric(id: String, parent: String = null, startEndTimes: (Long, Long))
  case object Tick
}

