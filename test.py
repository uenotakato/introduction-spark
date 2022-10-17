# Getting started
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg
from pyspark.sql.types import IntegerType, FloatType

spark = SparkSession.builder.getOrCreate()

