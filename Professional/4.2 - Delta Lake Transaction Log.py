# Databricks notebook source
# MAGIC %run ../Includes/Copy-Datasets

# COMMAND ----------

files = dbutils.fs.ls("dbfs:/user/hive/warehouse/bookstore_eng_pro.db/bronze/_delta_log")
display(files)

# COMMAND ----------

display(spark.read.json("dbfs:/user/hive/warehouse/bookstore_eng_pro.db/bronze/_delta_log/00000000000000000012.json"))

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT COUNT(*) FROM bronze

# COMMAND ----------

files = dbutils.fs.ls("dbfs:/user/hive/warehouse/bookstore_eng_pro.db/bronze/_delta_log")
display(files)

# COMMAND ----------

display(spark.read.parquet("dbfs:/user/hive/warehouse/bookstore_eng_pro.db/bronze/_delta_log/00000000000000000010.checkpoint.parquet"))

# COMMAND ----------

files = dbutils.fs.ls(f"{dataset_bookstore}/kafka-raw/")
display(files)

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE HISTORY bronze

# COMMAND ----------

# MAGIC %fs ls dbfs:/mnt/uploads

# COMMAND ----------

dbutils.secrets.help()

# COMMAND ----------


