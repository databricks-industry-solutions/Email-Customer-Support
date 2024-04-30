# Databricks notebook source
# MAGIC %md
# MAGIC ## Configuration Settings
# MAGIC
# MAGIC The following represent configuration settings used across various notebooks in this solution accelerator. You should read through all the notebooks to understand how the configuration settings are used before making any changes to the values below.

# COMMAND ----------

# DBTITLE 1,Instantiate Config Variable
if 'config' not in locals().keys():
  config = {}

# COMMAND ----------

# DBTITLE 1,Database and Volume
config['catalog'] = 'email_summary_llm_solution'
config['schema'] = 'email_llm'
config['volume'] = 'source_data'
config['vol_data_landing'] = f"/Volumes/{config['catalog']}/{config['schema']}/{config['volume']}"
config['table_emails_bronze'] = 'emails_bronze'
config['table_emails_silver_foundationalm'] = 'emails_foundational_silver'
config['table_emails_silver_externalm'] = 'emails_externalm_silver'
config['table_emails_silver'] = 'emails_silver'

# COMMAND ----------

# create catalog if not exists
spark.sql('create catalog if not exists {0}'.format(config['catalog']))

# set current catalog context
spark.sql('USE CATALOG {0}'.format(config['catalog']))

# create database if not exists
spark.sql('create database if not exists {0}'.format(config['schema']))

# set current datebase context
spark.sql('USE {0}'.format(config['schema']))

# COMMAND ----------

config['mount_point'] ='/tmp/emails_summary'
 
# file paths
config['checkpoint_path'] = config['mount_point'] + '/checkpoints'
config['schema_path'] = config['mount_point'] + '/schema'

# COMMAND ----------

# DBTITLE 1,Add OpenAI Key through the secrets
config['openai_api_key']=dbutils.secrets.get(scope = "email_openai_secret_scope", key = "openai_api_key")

# COMMAND ----------


