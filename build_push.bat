docker build . -t metrics-streaming
docker tag metrics-streaming karimbenamara/streaming
docker push karimbenamara/streaming