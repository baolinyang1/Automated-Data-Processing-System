# import pandas as pd


# from datetime import datetime

# def clean_and_transform(df: pd.DataFrame) -> pd.DataFrame:
#     """
#     Perform basic data cleaning and transformations.
#     """
#     # Drop rows where 'id' or 'name' is missing
#     df.dropna(subset=['id', 'name'], inplace=True)

#     # Standardize 'name' column
#     if 'name' in df.columns:
#         df['name'] = df['name'].str.title()

#     # Add a default date if 'date_col' doesn't exist or is empty
#     if 'date_col' not in df.columns:
#         df['date_col'] = datetime.now().date()  # Use today's date

#     return df

# if __name__ == "__main__":
#     # Quick test
#     sample_data = {
#         'id': [1, 2, None],
#         'date_col': ['2023-12-01', '2023-12-02', None],
#         'name': ['john', 'mary', 'JOHN'],
#     }
#     test_df = pd.DataFrame(sample_data)
#     print("Before transform:\n", test_df)
#     transformed_df = clean_and_transform(test_df)
#     print("After transform:\n", transformed_df)

import pandas as pd
from datetime import datetime
import re

def validate_email(email: str) -> bool:
    """Check if an email address is valid."""
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(email_regex, email))

def clean_and_transform(df: pd.DataFrame) -> pd.DataFrame:
    """
    Perform advanced data cleaning and transformations.
    """
    # 1. Drop rows with missing 'id' or 'name'
    df.dropna(subset=['id', 'name'], inplace=True)

    # 2. Standardize 'name' and 'region'
    df['name'] = df['name'].str.title()
    df['region'] = df['region'].str.title()

    # 3. Handle invalid sales values
    df['sales_flag'] = df['sales'].apply(lambda x: 'Valid' if x >= 0 else 'Invalid')
    df['sales'] = df['sales'].apply(lambda x: max(0, x))  # Replace negatives with 0

    # 4. Handle missing or invalid join_date
    df['join_date'] = pd.to_datetime(df['join_date'], errors='coerce')  # Convert to datetime
    df['join_date'].fillna(pd.Timestamp('2023-01-01'), inplace=True)  # Fill NaT with default date

    # 5. Validate email addresses
    df['email_valid'] = df['email'].apply(lambda x: validate_email(str(x)))

    # 6. Add derived columns
    df['year_joined'] = df['join_date'].dt.year
    df['bonus'] = df['sales'].apply(lambda x: x * 0.1 if x > 2000 else x * 0.05)

    # 7. Filter rows (Optional: For analysis)
    filtered_df = df[(df['region'] == 'North') & (df['sales'] > 1000)]

    return df, filtered_df
