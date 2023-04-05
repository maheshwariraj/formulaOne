# Databricks notebook source
accountkey = dbutils.secrets.get(scope = "keydatabricks",key="adlskey")

# COMMAND ----------

spark.conf.set(
    "fs.azure.account.key.adlsnewtestfree.dfs.core.windows.net",
    accountkey)


# COMMAND ----------

display(dbutils.fs.ls("abfss://demo@adlsnewtestfree.dfs.core.windows.net"))

# COMMAND ----------

df_circuits = spark.read.csv("abfss://demo@adlsnewtestfree.dfs.core.windows.net/circuits.csv")

# COMMAND ----------

df_circuits.show()

# COMMAND ----------


