# Databricks notebook source
# MAGIC %md 
# MAGIC #Reducing time-to-resolution for email customer support using LLMs

# COMMAND ----------

# MAGIC %md
# MAGIC The purpose of this notebook is to introduce the automation of customer support thorugh email. We use Large Langauge models (LLM) to automation the the email response process. You may find this notebook at https://github.com/sachinpatilb/PersonalRepo/tree/master/EmailSummary

# COMMAND ----------

# MAGIC %md
# MAGIC ### Introduction
# MAGIC Organizations often receive customer support inquiries through email channels. These emails need to adhere to service level agreements (SLAs) set by the organization or regulators, with penalties for failing to meet SLAs and rewards for exceeding them. Providing faster and more effective responses to customer inquiries enhances customer experience. However, many organizations struggle to meet SLAs due to the high volume of emails received and limited staff resources to respond to them.
# MAGIC
# MAGIC This solution accelerator proposes to use Large Language Models (LLMs) to automate the email response process. It involves the following key activities:
# MAGIC
# MAGIC <img src="https://raw.githubusercontent.com/sachinpatilb/ImageRepo/main/EmailAutomation.png" width=70%>
# MAGIC
# MAGIC 1. Categorization: The first step is to categorize the emails to understand the customer requests and urgency, including associated SLAs, and determine the appropriate approach for responding. Emails can be categorized as queries about the product, specific job requests, or generic emails that don't require a response.
# MAGIC 2. Sentiment Analysis: The sentiment of the email - positive, neutral, or negative - is analyzed.
# MAGIC 3. Synopsis: A summary of the email is created to help customer support professionals quickly understand its contents without reading the entire email.
# MAGIC 4. Automated Email Response: Based on the email's category, sentiment, and analysis, an automated customer email response is generated. 
# MAGIC
# MAGIC
# MAGIC As part of the solution, we present two approaches to deploy the solution on the Databricks Data Intelligence Platform:
# MAGIC 1. Proprietary SaaS LLMs: One approach is to call proprietary SaaS LLMs APIs from the Databricks Data Intelligence platform. This is convenient as it eliminates the need to train the model from scratch. Instead, pre-trained models can be used to classify and categorize emails.
# MAGIC 2. Open LLMs: The second approach involves deploying the solution within the organization's infrastructure as emails can contain sensitive information that cannot be shared outside the organization. This can be achieved using existing open LLM models such as LLAMA, Mosaic, etc. Fine-tuning of these models can be done using Databricks Mosaic models. This option provides more control over the infrastructure and can also reduce costs.
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ## Solution Design/architecture
# MAGIC
# MAGIC This section provide a high level of the architecture for this solution. 
# MAGIC
# MAGIC <img src="https://github.com/sachinpatilb/ImageRepo/blob/main/EmailAutomationArchitecture.png?raw=true" width=70%>
# MAGIC
# MAGIC - Data Ingestion: Customer support emails are received within popular email clients such as Microsoft Outlook, GMail etc. There are multiple solutions available to ingest data from the email clients into Databricks Delta tables. A few of the commonly used solutions are Azure LogicApps or AWS Step Functions.
# MAGIC - Model serving: Databricks Model Serving now offers a unified interface, making it easier to experiment, customize, and productionize models across all clouds and providers. This means you can create high-quality GenAI apps using the best model for your use case while securely leveraging your organization's unique data. Databricks Model Serving supports any External models, Foundation Models or custom models. In this solution, we have implemented external model interface for propriatory models like OpenAI as well as foundation models like Mistral.
# MAGIC - Update emails: The emails are enhanced by LLM and auotomated responses including catagory, sentiment and synopsis are sent back to the inbox of the customer support application.
# MAGIC
