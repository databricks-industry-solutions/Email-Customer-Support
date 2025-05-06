<img src=https://raw.githubusercontent.com/databricks-industry-solutions/.github/main/profile/solacc_logo.png width="600px">

[![DBR](https://img.shields.io/badge/DBR-14.3-red?logo=databricks&style=for-the-badge)](https://docs.databricks.com/release-notes/runtime/14.3.html)
[![CLOUD](https://img.shields.io/badge/CLOUD-ALL-blue?logo=googlecloud&style=for-the-badge)](https://databricks.com/try-databricks)

# Reducing time-to-resolution for email customer support using LLMs

## Business Problem

Organizations often receive customer support inquiries through email channels. These emails need to adhere to service level agreements (SLAs) set by the organization or regulators, with penalties for failing to meet SLAs and rewards for exceeding them. Providing faster and more effective responses to customer inquiries enhances customer experience. However, many organizations struggle to meet SLAs due to the high volume of emails received and limited staff resources to respond to them.

This solution accelerator demonstrates how to use Large Language Models (LLMs) to automate the email response process on Databricks. The solution involves four key activities:

1. **Categorization**: Categorize emails as job requests, customer queries, or generic emails that don't require a response. This helps understand customer requests, urgency, and associated SLAs.

2. **Sentiment Analysis**: Analyze email sentiment as positive, neutral, or negative.

3. **Synopsis**: Create concise summaries to help support professionals quickly understand content without reading entire emails.

4. **Automated Email Response**: Generate appropriate responses based on email category, sentiment, and content analysis.

Ideally, this is implemented as a human-in-the-loop solution rather than end-to-end automation. The support consultant's email inbox is updated with these features in near real-time, providing the ability to review and modify recommended responses.

## Solution Approaches

This accelerator demonstrates two approaches to deploy the solution on Databricks:

1. **Proprietary SaaS LLMs (OpenAI)**: Call proprietary LLM APIs from Databricks, eliminating the need to train models from scratch. The solution demonstrates integration with OpenAI's GPT-3.5-turbo-instruct model.

2. **Open Foundation Models (Mistral)**: Deploy the solution using foundation models within your organization's infrastructure, providing more control and cost efficiency when handling sensitive information. The solution demonstrates integration with Mistral-8X7b-instruct.

## Solution Architecture

<img src="https://github.com/databricks-industry-solutions/Email-Customer-Support/blob/main/images/EmailAutomation-Architetcure.png?raw=true" width=100%>

The solution architecture includes:

- **Data Ingestion**: Customer support emails from popular email clients (Microsoft Outlook, Gmail, etc.) are ingested into Databricks Delta tables using solutions like Azure LogicApps or AWS Step Functions.

- **Model Serving**: Databricks Model Serving provides a unified interface for external models and foundation models. The solution demonstrates:
  - External model interface for OpenAI
  - Foundation model support for Mistral

- **Email Updates**: Enhanced emails with categories, sentiment analysis, synopses, and draft responses are sent back to the customer support inbox.

## Notebook Walkthrough

This accelerator consists of the following notebooks that should be run sequentially:

1. **0_Introduction.py**: Overview of the solution and architectural design.

2. **1_Ingest_Emails_Into_Lakehouse.py**: Demonstrates ingestion of email data into Delta tables.

3. **2a_Configure_External_models_for_Automation.py**: 
   - Creates an OpenAI completion endpoint "Email-OpenAI-Completion-Endpoint" 
   - Configures Langchain with a custom prompt template
   - Tests the approach on a sample email

4. **2b_Test_Foundation_models_for_Automation.py**: 
   - Tests the Mistral-8X7b-instruct foundation model
   - Configures Langchain for the foundation model
   - Tests the model on a sample email

5. **3a_Serve_External_models_for_Automation.py**: 
   - Implements batch processing with the external model (OpenAI)
   - Creates a UDF for model serving
   - Processes emails and saves results to a table

6. **3b_Serve_Foundation_models_for_Automation.py**: 
   - Implements batch processing with the foundation model (Mistral)
   - Creates a similar UDF-based approach for model serving
   - Processes emails and saves results to a table

### Setup

The `_resources/00-setup.py` notebook contains configuration settings used across the solution. It handles:
- Creation of the catalog, schema, and volume
- Database and volume configuration
- Sample data ingestion from GitHub
- OpenAI API credentials setup through Databricks secrets

## Authors
Sachin Patil <sachin.patil@databricks.com><br>
Puneet Jain <puneet.jain@databricks.com>

## Project support 

Please note the code in this project is provided for your exploration only, and are not formally supported by Databricks with Service Level Agreements (SLAs). They are provided AS-IS and we do not make any guarantees of any kind. Please do not submit a support ticket relating to any issues arising from the use of these projects. The source in this project is provided subject to the Databricks [License](./LICENSE.md). All included or referenced third party libraries are subject to the licenses set forth below.

Any issues discovered through the use of this project should be filed as GitHub Issues on the Repo. They will be reviewed as time permits, but there are no formal SLAs for support. 

## License

&copy; 2024 Databricks, Inc. All rights reserved. The source in this notebook is provided subject to the Databricks License [https://databricks.com/db-license-source].  All included or referenced third party libraries are subject to the licenses set forth below.

| library                                | description             | license    | source                                              |
|----------------------------------------|-------------------------|------------|-----------------------------------------------------|
| Sample Email Dataset | This is a small dataset of less than 50 emails created manually | Sample | 


