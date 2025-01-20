#Dynamic Data Analysis and Visualization System

Overview

This project is a Dynamic Data Analysis and Visualization System designed to automate data extraction, transformation, and loading (ETL) processes, integrate results into a PostgreSQL database, and enable interactive analysis using Power BI. The system streamlines reporting, improves data accuracy, and reduces manual effort.

Features

Automated ETL Process:
Extracts data from a CSV file
Transforms data to clean, validate, and add derived fields.
Loads transformed data into a PostgreSQL database.
Data Transformation:
Standardizes fields (e.g., names, regions).
Handles invalid and missing data.
Adds derived columns like bonus and year_joined.
Integration with Power BI:
Allows data visualization using Power BI dashboards.
Supports Import or DirectQuery modes for analysis.
Automated Workflow:
Bash or Batch script (start.sh or start.bat) to execute the full pipeline.
