# Databricks notebook source
# MAGIC %md 
# MAGIC You may find this series of notebooks at https://github.com/databricks-industry-solutions/sample-repo. For more information about this solution accelerator, visit https://www.databricks.com/solutions/accelerators/sample-accelerator

# COMMAND ----------

# MAGIC %pip install mlflow[genai]>=2.9.0
# MAGIC %pip install --upgrade mlflow
# MAGIC %pip install --upgrade langchain
# MAGIC dbutils.library.restartPython()

# COMMAND ----------

# MAGIC %sh
# MAGIC cat /dbfs/FileStore/email_text_example.txt

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

df=spark.read.format("delta").option("multiline","true").table("email_summary_llm_solution.email_llm.emails_foundational_silver")

# COMMAND ----------

from pyspark.sql.functions import col, explode

display(df.select('message_id'), explode('summary_string')
        .withColumn('category', col('summary_string.Category')
        ))

# COMMAND ----------

from pyspark.sql.functions import col, explode, split

display(df.select('message_id', explode(split('summary_string', ',')).alias('summary')).select('message_id', col('summary.Category').alias('category')))

# COMMAND ----------

from pyspark.sql.functions import from_json

json_schema = "Category STRING, Sentiment STRING, Synposis STRING, Reply STRING"

display(df.select('message_id', to_json('summary_string')))

# COMMAND ----------

val dfJSON = dfFromText.withColumn("jsonData",from_json(col("value"),schema))
    .select("jsonData.*")

# COMMAND ----------

from pyspark.sql.types import StructType, StringType
# Declare the schema
json_schema = StructType() \
    .add("Category", StringType(), True) \
    .add("Sentiment", StringType(), True) \
    .add("Synposis", StringType(), True) \
    .add("Reply", StringType(), True)


# COMMAND ----------

from pyspark.sql.functions import from_json, col
df_parsed=df.withColumn("email_response", from_json(col("summary_string"), json_schema, options={'multiLine':True})).select("*","email_response.*").drop("email_response")

# COMMAND ----------

display(df_parsed)

# COMMAND ----------

dfJSON = dfFromText.withColumn("jsonData",from_json(col("value"),schema))
    .select("jsonData.*")
dfJSON.printSchema()
dfJSON.show(false)
