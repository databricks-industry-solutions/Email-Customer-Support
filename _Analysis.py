# Databricks notebook source
# MAGIC %md 
# MAGIC You may find this series of notebooks at https://github.com/databricks-industry-solutions/sample-repo. For more information about this solution accelerator, visit https://www.databricks.com/solutions/accelerators/sample-accelerator

# COMMAND ----------

# MAGIC %pip install mlflow[genai]>=2.9.0
# MAGIC %pip install --upgrade mlflow
# MAGIC %pip install --upgrade langchain
# MAGIC dbutils.library.restartPython()

# COMMAND ----------

if 'config' not in locals().keys():
  config = {}

# COMMAND ----------

config['catalog'] = 'email_summary_llm_solution'
config['schema'] = 'email_llm'
config['volume'] = 'source_data'
config['vol_data_landing'] = f"/Volumes/{config['catalog']}/{config['schema']}/{config['volume']}"
config['table_emails_bronze'] = 'emails_bronze'
config['table_emails_silver_foundationalm'] = 'emails_foundational_silver'
config['table_emails_silver_externalm'] = 'emails_externalm_silver'
config['table_emails_silver'] = 'emails_silver'

# COMMAND ----------

spark.sql('USE CATALOG {0}'.format(config['catalog']))
spark.sql('drop database if exists {0}'.format(config['schema']))

# COMMAND ----------

dbutils.fs.ls(config['vol_data_landing'])

# COMMAND ----------

import mlflow
import mlflow.deployments

client = mlflow.deployments.get_deploy_client("databricks")
print(client.delete_endpoint("Email-OpenAI-Completion-Endpoint"))

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from email_summary_llm_solution.email_llm.emails_bronze

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from email_summary_llm_solution.email_llm.emails_externalm_silver

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from email_summary_llm_solution.email_llm.emails_foundational_silver

# COMMAND ----------

# MAGIC %sql
# MAGIC drop table email_summary_llm_solution.email_llm.emails_foundational_silver

# COMMAND ----------


