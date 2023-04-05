# Databricks notebook source
# MAGIC %md
# MAGIC # There type to connect ADLS
# MAGIC 
# MAGIC 1. Using Access keys
# MAGIC   - this is least prefered as this will give you whole container access and with no ristriction. to avoid SAS will come in picture---
# MAGIC 2. Unity Catalog managed external locations
# MAGIC 3. Azure service principals
# MAGIC 4. SAS tokens
# MAGIC 
# MAGIC Account keys
# MAGIC - link: https://www.youtube.com/watch?v=h_mbpd0oqOE
# MAGIC - link: https://docs.databricks.com/storage/azure-storage.html

# COMMAND ----------

spark.conf.set(
    "fs.azure.account.key.adlsnewtestfree.dfs.core.windows.net",
    "kZZsvHIpIV3qkxt19S8nvysHaHSx2huzUV/kvPR2Ks4GyBBmbyYbEqGZz3Sj/0KncebopgVwADee+AStv83o+g==")


# COMMAND ----------

display(dbutils.fs.ls("abfss://demo@adlsnewtestfree.dfs.core.windows.net"))

# COMMAND ----------

df_circuits = spark.read.csv("abfss://demo@adlsnewtestfree.dfs.core.windows.net/circuits.csv")

# COMMAND ----------

df_circuits.show()

# COMMAND ----------


