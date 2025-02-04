from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType

schema = StructType([
    StructField("user_id", IntegerType()),
    StructField("date", StringType()),
    StructField("steps", IntegerType()),
    StructField("calories_burned", FloatType()),
    StructField("distance_km", FloatType()),
    StructField("active_minutes", IntegerType()),
    StructField("sleep_hours", FloatType()),
    StructField("heart_rate_avg", IntegerType()),
    StructField("workout_type", StringType()),
    StructField("weather_conditions", StringType()),
    StructField("location", StringType()),
    StructField("mood", StringType())
])

spark = SparkSession.builder \
    .appName("UserActivityStreaming") \
    .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.4") \
    .getOrCreate()

df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "user_activity") \
    .option("startingOffsets", "earliest") \
    .load()

parsed_df = df.select(
    from_json(col("value").cast("string"), schema).alias("data")
).select("data.*")

processed_df = parsed_df.groupBy("user_id") \
    .agg({"steps": "sum", "calories_burned": "avg"}) \
    .withColumnRenamed("sum(steps)", "total_steps") \
    .withColumnRenamed("avg(calories_burned)", "avg_calories_burned")

query = processed_df.writeStream \
    .outputMode("complete") \
    .format("console") \
    .option("truncate", "false") \
    .option("numRows", 10) \
    .trigger(processingTime="10 seconds") \
    .start()

query.awaitTermination(60)  # Stop after 60 seconds
