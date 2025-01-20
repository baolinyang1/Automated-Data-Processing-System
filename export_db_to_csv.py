import psycopg2
import pandas as pd

# Database connection settings
DB_NAME = "mydatabase"
DB_USER = "myuser"
DB_PASS = "mypassword"
DB_HOST = "localhost"  # Use your Docker container's IP or hostname if localhost doesn't work
DB_PORT = "5433"

# SQL query to fetch data from the table
query = "SELECT * FROM my_table;"

# Connect to the PostgreSQL database and fetch data
try:
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        host=DB_HOST,
        port=DB_PORT
    )
    # Execute the query and load the data into a Pandas DataFrame
    df = pd.read_sql_query(query, conn)
    conn.close()

    # Save the DataFrame to a new CSV file
    csv_file_path = "db_table_data.csv"
    df.to_csv(csv_file_path, index=False)
    print(f"Data exported successfully to {csv_file_path}")

except Exception as e:
    print(f"An error occurred: {e}")
