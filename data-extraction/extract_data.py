import pandas as pd
import requests

def extract_from_csv(file_path: str) -> pd.DataFrame:
    """
    Read data from a CSV file.
    """
    df = pd.read_csv(file_path)
    return df

def extract_from_api(api_url: str) -> pd.DataFrame:
    """
    Fetch data from a REST API endpoint returning JSON.
    """
    response = requests.get(api_url)
    data = response.json()
    df = pd.DataFrame(data)
    return df

if __name__ == "__main__":
    # Quick CSV test (Uncomment or update the path)
    # df_csv = extract_from_csv("C:/path/to/your_file.csv")
    # print("CSV data:\n", df_csv.head())

    # Quick API test (Uncomment or update the URL)
    # test_api_url = "https://api.example.com/data"
    # df_api = extract_from_api(test_api_url)
    # print("API data:\n", df_api.head())
    pass

