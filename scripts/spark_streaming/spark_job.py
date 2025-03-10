from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType

# Definição do schema
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

# Inicializando a sessão do Spark
spark = SparkSession.builder \
    .appName("UserActivityStreaming") \
    .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.4") \
    .getOrCreate()

# Lendo dados do Kafka
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "user_activity") \
    .option("startingOffsets", "earliest") \
    .load()

# Parseando os dados com o schema
parsed_df = df.select(
    from_json(col("value").cast("string"), schema).alias("data"),
    col("timestamp")  # Adicionando a coluna timestamp
).select("data.*", "timestamp")

# Extraindo os nomes das colunas para o cabeçalho
columns = parsed_df.columns

# 1. Escrevendo o cabeçalho uma única vez
# Verificando se o arquivo de cabeçalho já existe para evitar sobrescrever
import os
header_path = "/home/mauricio/git/real-time-pipeline/data/output_header/"

if not os.path.exists(header_path):
    header_df = spark.createDataFrame([columns], StructType([StructField(c, StringType(), True) for c in columns]))
    header_df.write \
        .format("csv") \
        .mode("overwrite") \
        .option("header", "true") \
        .save(header_path)

# 2. Escrevendo os dados em arquivos CSV continuamente
query = parsed_df.writeStream \
    .outputMode("append") \
    .format("csv") \
    .option("path", "/home/mauricio/git/real-time-pipeline/data/output/") \
    .option("checkpointLocation", "/home/mauricio/git/real-time-pipeline/data/new_checkpoint") \
    .trigger(processingTime="10 seconds") \
    .start()

# Aguardando a execução do stream por 60 segundos
query.awaitTermination(60)
