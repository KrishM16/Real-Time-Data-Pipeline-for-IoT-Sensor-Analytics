from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType, DoubleType

# Spark session
spark = SparkSession.builder \
    .appName("IoT Streaming Pipeline") \
    .getOrCreate()

# Schema for incoming JSON
schema = StructType() \
    .add("sensor_id", StringType()) \
    .add("timestamp", StringType()) \
    .add("temperature", DoubleType()) \
    .add("humidity", DoubleType()) \
    .add("vibration", DoubleType()) \
    .add("status", StringType())

# Read Kafka stream
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "iot-sensor-data") \
    .load()

# Parse JSON
iot_data = df.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*")

# Simple anomaly check
alerts = iot_data.filter((col("temperature") > 90) | (col("vibration") > 0.08))

# Write raw data to parquet
iot_data.writeStream \
    .format("parquet") \
    .option("path", "/tmp/iot/raw/") \
    .option("checkpointLocation", "/tmp/iot/raw_checkpoint/") \
    .outputMode("append") \
    .start()

# Write alerts to console
alerts.writeStream \
    .outputMode("append") \
    .format("console") \
    .start() \
    .awaitTermination()
