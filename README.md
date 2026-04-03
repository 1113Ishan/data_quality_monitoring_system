Data Quality Monitoring System
==============================

Overview
--------

The Data Quality Monitoring System (DQMS) is an automated framework designed to validate, monitor, and report on the quality of data pipelines. In modern businesses, data reliability is crucial for analytics and decision-making. DQMS addresses common data issues including missing values, duplicate records, invalid timestamps or statuses, cross-table inconsistencies, and schema mismatches. By ensuring consistent, clean data, it improves trust in reporting and analytics processes.

The system is ideal for real-world pipelines where data arrives daily from multiple sources and quality must be continuously monitored.

Architecture
------------

DQMS is organized into three main layers:

1.  **Python Validation Scripts**
    
2.  **SQL Data Quality Tables**
    
3.  **Power BI Monitoring Dashboard**
    

The data flows from raw datasets through Python scripts, which perform checks and generate results. These results are stored in SQL tables, which are then visualized using Power BI to provide stakeholders with actionable insights.

**Data Flow:**Raw Data → Python Validation → SQL Logging → Power BI Dashboard

1\. Python Validation
---------------------

### Data Loading

The loader.py module loads CSV datasets into Pandas DataFrames. It handles parsing dates, standardizing column names, and type conversion to prepare data for validation.

Example:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   orders = pd.read_csv('orders.csv', parse_dates=['order_purchase_timestamp'])   `

### Validation Checks (checks.py)

The system runs multiple types of data quality checks:

*   **Missing Values:** Counts null entries in critical columns
    
*   **Duplicate Records:** Detects repeated rows based on unique identifiers
    
*   **Invalid Timestamps:** Identifies approvals before purchases or deliveries before shipment
    
*   **Invalid Status:** Flags records with incorrect order statuses
    
*   **Cross-Table Validation:** Ensures orders reference valid customers
    
*   **Late Deliveries:** Compares actual delivery dates against estimated dates
    

### Utilities (utils.py)

Utility functions format validation results for SQL insertion. They convert Python objects, including NumPy types, into JSON-compatible formats and attach timestamps.

Example formatted result:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   {  "table_name": "orders",  "check_type": "duplicate_orders",  "check_result": 0,  "check_time": "2026-04-03T15:01:09"}   `

### Main Pipeline (main.py)

The main script orchestrates the workflow:

1.  Load datasets
    
2.  Execute all validation checks
    
3.  Format results for SQL insertion
    
4.  Log pipeline metadata, including number of records processed and total errors
    

This allows fully automated pipeline monitoring without manual intervention.

2\. SQL Data Storage
--------------------

Two SQL tables store the results:

1.  **data\_quality\_check**
    
    *   check\_id (primary key)
        
    *   table\_name
        
    *   check\_type
        
    *   check\_result (JSON or numeric)
        
    *   check\_time
        
2.  **data\_pipeline\_runs**
    
    *   run\_id (primary key)
        
    *   run\_time
        
    *   status (success/failure)
        
    *   records\_processed
        
    *   errors\_detected
        

These tables provide a historical log of data quality metrics and pipeline runs, enabling trend analysis and reporting over time.

3\. Power BI Dashboard
----------------------

The Power BI dashboard visualizes key metrics:

*   **Pipeline Status:** Last run, success/failure trends
    
*   **Data Quality Metrics:** Missing values per column, duplicate records, schema errors
    
*   **Data Freshness:** Last update per table, latency tracking
    
*   **Business Insights:** Highlights critical issues, e.g., missing emails or delayed orders
    

This visualization helps stakeholders quickly understand the state of the data and identify areas requiring attention.

Setup & Usage
-------------

1.  **Clone the repository:**
    

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   git clone https://github.com/1113Ishan/data_quality_monitoring_system.gitcd data_quality_monitoring_system   `

1.  **Set up Python environment:**
    

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   python -m venv venv# Activate environmentsource venv/bin/activate  # macOS/Linuxvenv\Scripts\activate     # Windowspip install -r requirements.txt   `

1.  **PostgreSQL setup:**
    

*   Create a database and the required tables (data\_quality\_check and data\_pipeline\_runs)
    
*   Update db.py with your credentials
    

1.  **Run the pipeline:**
    

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   python scripts/main.py   `

The pipeline automatically loads datasets, runs checks, and logs results into the database. Refresh the Power BI dashboard to visualize the metrics.

Reusability and Future Enhancements
-----------------------------------

*   Modular design allows adding new validation checks or datasets easily.
    
*   Supports multiple tables and pipelines.
    
*   Can be integrated with schedulers such as Airflow or cron for real-time monitoring.
    
*   Future enhancements may include real-time alerts, additional type or regex validations, multi-source ingestion, and automated notifications via email or Slack.
    

Conclusion
----------

DQMS provides a complete end-to-end solution for monitoring data quality using Python, SQL, and Power BI. It ensures automated validation, persistent logging, and visualization of key metrics. Implementing DQMS in pipelines improves data governance, reliability, and confidence in analytics outputs, making it a valuable framework for businesses relying on clean and accurate data.
