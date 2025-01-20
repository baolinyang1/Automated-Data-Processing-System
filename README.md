#Dynamic Data Analysis and Visualization System

Overview

This project is a Dynamic Data Analysis and Visualization System designed to automate data extraction, transformation, and loading (ETL) processes, integrate results into a PostgreSQL database, and enable interactive analysis using Power BI. The system streamlines reporting, improves data accuracy, and reduces manual effort.

Features

Automated ETL Process:
Extracts data from a CSV file or API.
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

Project Structure

├── data-extraction
│ ├── extract_data.py # Handles data extraction from CSV or API
│ └── sample.csv # Example input data
├── data-transformation
│ ├── transform_data.py # Cleans, validates, and transforms data
├── database
│ ├── docker-compose.yml # Docker configuration for PostgreSQL
├── scripts
│ ├── load_data.py # Loads transformed data into PostgreSQL
│ ├── export_db_to_csv.py # Exports PostgreSQL table to a CSV file
├── start.sh # Bash script to automate the pipeline
├── start.bat # Batch script for Windows users
└── README.md # Project documentation

Setup Instructions

Prerequisites
Python 3.8+
Docker and Docker Compose installed.
Power BI Desktop (optional for visualization).

Install Dependencies
Clone the repository:

bash
git clone <repository-url>
cd project-directory
Create a virtual environment and activate it:

bash
python -m venv venv
source venv/bin/activate # For Linux/Mac
venv\Scripts ctivate # For Windows
Install required Python packages:

bash
pip install -r data-extraction/requirements.txt
Start the PostgreSQL Database
Navigate to the database directory:

bash
cd database
Start the database using Docker Compose:

bash
docker-compose up -d
Verify the PostgreSQL container is running:

bash
docker ps

Usage Instructions

Run the Entire Pipeline
Use the provided script to automate the process:

On Linux/Mac:
bash
./start.sh
On Windows:
cmd
start.bat
The script performs the following:
Executes load_data.py to load data into PostgreSQL.
Executes export_db_to_csv.py to export the transformed table to db_table_data.csv.

Access Data in Power BI
Open Power BI Desktop.
Select Get Data > PostgreSQL database.
Enter the database connection details:
Server: localhost (or Docker container IP).
Port: 5433.
Database: mydatabase.
Username: myuser.
Password: mypassword.
Choose the my_table table and load it into Power BI.
Create visualizations such as bar charts, tables, or slicers.

Example Workflow

Input Data (sample.csv)

id name sales region join_date email 
1 john doe 1000 North 2023-01-01 john.doe@email.com 
2 MARY SMITH 1500 south 2022-07-15 mary.smith@email.com 
3 charlie brown -200 east 2021-12-10 charlie@email 
4 delta KING 2500 west 2024-05-20 delta.king@email.com 
5 echo ROGERS 3000 North NaN echo.rogers@email.com 

Transformed Data in PostgreSQL (my_table)

id name sales region join_date email sales_flag email_valid year_joined bonus 
1 John Doe 1000 North 2023-01-01 john.doe@email.com Valid True 2023 50.0 
2 Mary Smith 1500 South 2022-07-15 mary.smith@email.com Valid True 2022 75.0 
3 Charlie Brown 0 East 2021-12-10 charlie@email Invalid False 2021 0.0 
4 Delta King 2500 West 2024-05-20 delta.king@email.com Valid True 2024 250.0 
5 Echo Rogers 3000 North 2023-01-01 echo.rogers@email.com Valid True 2023 300.0 

Key Files

scripts/load_data.py: Automates data loading into PostgreSQL.
data-transformation/transform_data.py: Cleans, validates, and transforms data.
scripts/export_db_to_csv.py: Exports the PostgreSQL table into a CSV file.
database/docker-compose.yml: Configuration for running PostgreSQL in Docker.

Future Enhancements

Integrate additional data sources (e.g., APIs).
Add support for advanced analytics with DAX in Power BI.
Implement real-time updates using DirectQuery mode in Power BI.

License

This project is licensed under the MIT License.

Contact

For questions or suggestions, please contact:

Name: [Your Name]
Email: [Your Email]
