import findspark
findspark.init()
# import pyspark
from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *

spark = SparkSession.builder.master("local").appName("test").getOrCreate()

df =  spark.read.format("csv").load("E:/DataAnalytics/CRICKETANALYTICS/Batsman_Data.csv",header = True)
df.show()