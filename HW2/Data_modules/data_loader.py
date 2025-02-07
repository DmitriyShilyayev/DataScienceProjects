import requests
import os
import io
import pandas as pd
from pandas import DataFrame

class DataLoader:
    @staticmethod
    def load_csv(file_path: str) -> DataFrame:
        return pd.read_csv(file_path)

    @staticmethod
    def load_json(file_path: str) -> DataFrame:
        return pd.read_json(file_path)

    @staticmethod
    def load_api(url: str) -> DataFrame:
        response = requests.get(url)
        if response.status_code == 200:
            if response.headers['Content-Type'].find('text/csv') > -1:
                return pd.read_csv(io.StringIO(response.text))
            elif response.headers['Content-Type'].find('application/json') > -1:
                return pd.DataFrame(response.json())
        else:
            raise Exception(f"API request failed. Status code: {response.status_code}")

    @staticmethod
    def load_data(file_path: str) -> DataFrame:
        file_name, file_extension = os.path.splitext(file_path)
        if file_extension == '.csv':
            data = DataLoader.load_csv(file_path)
        elif file_extension == '.json':
            data = DataLoader.load_json(file_path)
        else:
            data = DataLoader.load_api(file_path)
        return data

    def __init__(self) -> None:
        return
