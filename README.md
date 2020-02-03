# SF-Crime-Statistics-with-Spark-Streaming

###How did changing values on the SparkSession property parameters affect the throughput and latency of the data?
different property parameters affect the delay and through put of data for example incresing processedRowsPerSecond: means to process more rows in second, which leads to higher throughput. spark.streaming.receiver.maxRate means that each recieaver can reciave at most this much of data is data is take long time to process we should lower this value to minimize delay.

###What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?
spark.streaming.backpressure.enabled speed up the process by checking the info logs on how long the process took you can check the change.spark.default.parallelism was also worked use parallelism can increase thorughput of data.
