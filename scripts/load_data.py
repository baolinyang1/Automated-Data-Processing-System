# import psycopg2
# from psycopg2 import sql
# import pandas as pd
# import sys
# import os

# # Append paths so we can import from sibling folders
# sys.path.append(os.path.join(os.path.dirname(__file__), '../data-extraction'))
# sys.path.append(os.path.join(os.path.dirname(__file__), '../data-transformation'))

# from extract_data import extract_from_csv, extract_from_api
# from transform_data import clean_and_transform

# # -------------------------------------------------------
# # DATABASE CONNECTION SETTINGS (Match docker-compose.yml)
# # -------------------------------------------------------
# DB_NAME = "mydatabase"
# DB_USER = "myuser"
# DB_PASS = "mypassword"
# DB_HOST = "localhost"
# DB_PORT = "5433"   # Instead of 5432

# def get_db_connection():
#     conn = psycopg2.connect(
#         dbname="mydatabase",
#         user="myuser",
#         password="mypassword",
#         host="localhost",
#         port="5433"
#     )
#     return conn

# # def create_table_if_not_exists():
# #     """
# #     Creates a table if it doesn't already exist.
# #     Modify columns to match your dataset.
# #     """
# #     conn = get_db_connection()
# #     cur = conn.cursor()

# #     create_table_query = """
# #     CREATE TABLE IF NOT EXISTS my_table (
# #         id SERIAL PRIMARY KEY,
# #         name VARCHAR(100),
# #         date_col DATE
# #         -- Add more columns to reflect your data structure
# #     );
# #     """
# #     cur.execute(create_table_query)
# #     conn.commit()
# #     cur.close()
# #     conn.close()
# def create_table_if_not_exists():
#     """
#     Creates a table if it doesn't already exist.
#     Modify columns to match your dataset.
#     """
#     conn = get_db_connection()
#     cur = conn.cursor()

#     create_table_query = """
#     CREATE TABLE IF NOT EXISTS my_table (
#         id SERIAL PRIMARY KEY,
#         name VARCHAR(100),
#         sales INT,
#         region VARCHAR(50),
#         date_col DATE
#     );
#     """
#     cur.execute(create_table_query)
#     conn.commit()
#     cur.close()
#     conn.close()

# # def load_data_to_db(df: pd.DataFrame):
# #     """
# #     Loads the DataFrame data into PostgreSQL.
# #     """
# #     conn = get_db_connection()
# #     cur = conn.cursor()

# #     insert_query = """
# #         INSERT INTO my_table (name, date_col)
# #         VALUES (%s, %s)
# #     """

# #     for _, row in df.iterrows():
# #         # Adjust based on columns
# #         cur.execute(insert_query, (
# #             row.get('name'),
# #             row.get('date_col')
# #         ))

# #     conn.commit()
# #     cur.close()
# #     conn.close()
# # def load_data_to_db(df: pd.DataFrame):
# #     """
# #     Loads the DataFrame data into PostgreSQL.
# #     """
# #     conn = get_db_connection()
# #     cur = conn.cursor()

# #     insert_query = """
# #         INSERT INTO my_table (name, sales, region, date_col)
# #         VALUES (%s, %s, %s, %s)
# #     """

# #     for _, row in df.iterrows():
# #         cur.execute(insert_query, (
# #             row.get('name'),
# #             row.get('sales'),
# #             row.get('region'),
# #             row.get('date_col')
# #         ))

# #     conn.commit()
# #     cur.close()
# #     conn.close()
# def load_data_to_db(df: pd.DataFrame):
#     """
#     Loads the DataFrame data into PostgreSQL.
#     """
#     if not isinstance(df, pd.DataFrame):
#         raise ValueError("Expected a DataFrame, but got a different type.")
    
#     conn = get_db_connection()
#     cur = conn.cursor()

#     insert_query = """
#         INSERT INTO my_table (name, sales, region, date_col)
#         VALUES (%s, %s, %s, %s)
#     """

#     for _, row in df.iterrows():
#         cur.execute(insert_query, (
#             row.get('name'),
#             row.get('sales'),
#             row.get('region'),
#             row.get('date_col')
#         ))

#     conn.commit()
#     cur.close()
#     conn.close()

# def main():
#     # 1) Choose your data source
#     # Example: CSV file
#     csv_file_path = os.path.join(os.path.dirname(__file__), '../data-extraction/sample.csv')
#     df = extract_from_csv(csv_file_path)

#     # If you have an API instead:
#     # api_url = "https://api.example.com/data"
#     # df = extract_from_api(api_url)
    
#     # 2) Transform/clean data
#     df_cleaned, filtered_df = clean_and_transform(df)

#     # 3) Create table if not exists
#     create_table_if_not_exists()

#     # 4) Load data into PostgreSQL
#     load_data_to_db(df_cleaned)
#     print("Data loaded successfully!")

# if __name__ == "__main__":
#     main()

import psycopg2
from psycopg2 import sql
import pandas as pd
import sys
import os

# Append paths so we can import from sibling folders
sys.path.append(os.path.join(os.path.dirname(__file__), '../data-extraction'))
sys.path.append(os.path.join(os.path.dirname(__file__), '../data-transformation'))

from extract_data import extract_from_csv
from transform_data import clean_and_transform

# -------------------------------------------------------
# DATABASE CONNECTION SETTINGS (Match docker-compose.yml)
# -------------------------------------------------------
DB_NAME = "mydatabase"
DB_USER = "myuser"
DB_PASS = "mypassword"
DB_HOST = "localhost"
DB_PORT = "5433"

def get_db_connection():
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        host=DB_HOST,
        port=DB_PORT
    )
    return conn

def create_table_if_not_exists():
    """
    Creates a table if it doesn't already exist.
    Modify columns to match your dataset.
    """
    conn = get_db_connection()
    cur = conn.cursor()

    create_table_query = """
    CREATE TABLE IF NOT EXISTS my_table (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        sales INT,
        region VARCHAR(50),
        join_date DATE,
        email VARCHAR(100),
        sales_flag VARCHAR(10),
        email_valid BOOLEAN,
        year_joined INT,
        bonus FLOAT
    );
    """
    cur.execute(create_table_query)
    conn.commit()
    cur.close()
    conn.close()

def load_data_to_db(df: pd.DataFrame):
    """
    Loads the DataFrame data into PostgreSQL.
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Expected a DataFrame, but got a different type.")
    
    conn = get_db_connection()
    cur = conn.cursor()

    insert_query = """
        INSERT INTO my_table (name, sales, region, join_date, email, sales_flag, email_valid, year_joined, bonus)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    for _, row in df.iterrows():
        cur.execute(insert_query, (
            row.get('name'),
            row.get('sales'),
            row.get('region'),
            row.get('join_date'),
            row.get('email'),
            row.get('sales_flag'),
            row.get('email_valid'),
            row.get('year_joined'),
            row.get('bonus')
        ))

    conn.commit()
    cur.close()
    conn.close()

def main():
    # 1) Choose your data source
    csv_file_path = os.path.join(os.path.dirname(__file__), '../data-extraction/sample.csv')
    df = extract_from_csv(csv_file_path)

    # 2) Transform/clean data
    df_cleaned, filtered_df = clean_and_transform(df)

    # Display filtered data
    print("\nFiltered data (North region, sales > 1000):\n", filtered_df)

    # 3) Create table if not exists
    create_table_if_not_exists()

    # 4) Load data into PostgreSQL
    load_data_to_db(df_cleaned)
    print("Data loaded successfully!")

if __name__ == "__main__":
    main()
