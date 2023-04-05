# Databricks notebook source
# MAGIC %md
# MAGIC ###below are the benefits to use SAS token
# MAGIC 
# MAGIC 1. Provides fine grained access to the storage
# MAGIC 2. Restrict access to specific resource types/ services
# MAGIC 3. Allow specific permissions
# MAGIC 4. Restrict access to specific time period
# MAGIC 5. Limit access to specific IP addresses
# MAGIC 6. Recommended access pattern for external clients

# COMMAND ----------

spark.conf.set("fs.azure.account.auth.type.adlsnewtestfree.dfs.core.windows.net", "SAS")
spark.conf.set("fs.azure.sas.token.provider.type.adlsnewtestfree.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.sas.FixedSASTokenProvider")
spark.conf.set("fs.azure.sas.fixed.token.adlsnewtestfree.dfs.core.windows.net", "sp=rl&st=2023-04-04T05:47:16Z&se=2023-04-05T13:47:16Z&spr=https&sv=2021-12-02&sr=c&sig=%2BbvocYM5ntwTv1ZZjktvRbMFULKxZ91gXwfbDLPji%2Fk%3D")

# COMMAND ----------

dbutils.fs.ls("abfss://demo@adlsnewtestfree.dfs.core.windows.net")

# COMMAND ----------

spark.read.csv("abfss://demo@adlsnewtestfree.dfs.core.windows.net/circuits.csv")

# COMMAND ----------


