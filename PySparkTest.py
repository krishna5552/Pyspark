import findspark
findspark.init()
# import pyspark
from pyspark.sql import *

spark = SparkSession.builder.master("local").appName("test").getOrCreate()

print(spark)