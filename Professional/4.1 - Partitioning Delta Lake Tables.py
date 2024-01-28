# Databricks notebook source
# MAGIC %run ../Includes/Copy-Datasets

# COMMAND ----------

bookstore.load_new_data()

# COMMAND ----------

bookstore.process_bronze()

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE TABLE EXTENDED bronze

# COMMAND ----------

files = dbutils.fs.ls("dbfs:/user/hive/warehouse/bookstore_eng_pro.db/bronze")
display(files)

# COMMAND ----------

files = dbutils.fs.ls("dbfs:/user/hive/warehouse/bookstore_eng_pro.db/bronze/topic=customers")
display(files)

# COMMAND ----------

files = dbutils.fs.ls("dbfs:/user/hive/warehouse/bookstore_eng_pro.db/bronze/_delta_log/")
display(files)

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from json.`dbfs:/user/hive/warehouse/bookstore_eng_pro.db/bronze/_delta_log/00000000000000000010.json`

# COMMAND ----------

files = dbutils.fs.ls("dbfs:/user/hive/warehouse/bookstore_eng_pro.db/bronze/topic=customers/year_month=2021-12/")
display(files)

# COMMAND ----------


