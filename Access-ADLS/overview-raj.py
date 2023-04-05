# Databricks notebook source
# MAGIC %md
# MAGIC ##There few different ways to connect ADLS like 
# MAGIC   1. secret in notebook 
# MAGIC     - Using Access keys
# MAGIC     - SAS tokens
# MAGIC     - service principle
# MAGIC   2. secret at cluster
# MAGIC     - configure in cluster and will have access to all the notebook which is atteched to that cluster which is unsecure
# MAGIC   3. AAD passthrough
# MAGIC     - this also cluster based but it is save
# MAGIC     
# MAGIC 
# MAGIC Account keys
# MAGIC 
# MAGIC - link: https://www.youtube.com/watch?v=h_mbpd0oqOE
# MAGIC - link: https://docs.databricks.com/storage/azure-storage.html

# COMMAND ----------


