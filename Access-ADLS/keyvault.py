# Databricks notebook source
# MAGIC %md
# MAGIC I have create on secret scope named keydatabricks using 
# MAGIC -  https://learn.microsoft.com/en-us/azure/databricks/security/secrets/secret-scopes#create-an-azure-key-vault-backed-secret-scope-using-the-ui

# COMMAND ----------

dbutils.secrets.help()

# COMMAND ----------

dbutils.secrets.listScopes()

# COMMAND ----------

dbutils.secrets.list(scope="keydatabricks")

# COMMAND ----------

dbutils.secrets.get(scope="keydatabricks" , key="app")

# COMMAND ----------


