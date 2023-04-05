# Databricks notebook source
tenent_id = "d93523cf-ad06-49d5-a4d7-4f1bafa094a2"
application_id = "c5440238-f446-454c-8003-a4404049248e"
client_secret = "QtM8Q~EA-IWDkYIeG_CqygMUzTihcRHnG84Jebmd"

# COMMAND ----------

spark.conf.set("fs.azure.account.auth.type.adlsnewtestfree.dfs.core.windows.net", "OAuth")
spark.conf.set("fs.azure.account.oauth.provider.type.adlsnewtestfree.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
spark.conf.set("fs.azure.account.oauth2.client.id.adlsnewtestfree.dfs.core.windows.net", application_id)
spark.conf.set("fs.azure.account.oauth2.client.secret.adlsnewtestfree.dfs.core.windows.net", client_secret)
spark.conf.set("fs.azure.account.oauth2.client.endpoint.adlsnewtestfree.dfs.core.windows.net", f"https://login.microsoftonline.com/{tenent_id}/oauth2/token")

# COMMAND ----------

dbutils.fs.ls("abfss://demo@adlsnewtestfree.dfs.core.windows.net")
