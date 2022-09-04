from pyspark.sql import SparkSession

spark = SparkSession.builder\
    .appName("sample").getOrCreate()

df = spark.read.format("org.neo4j.spark.DataSource")\
  .option("url", "bolt://localhost:7687")\
  .option("authentication.basic.username", "neo4j_graphql")\
  .option("authentication.basic.password", "root")\
  .option("labels", "Actor")\
  .load()