import requests
import os
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
            return pd.DataFrame(response.json())
        else:
            raise Exception(f"API request failed. Status code: {response.status_code}")

    def __init__(self, file_path: str) -> None:
        file_name, file_extension = os.path.splitext(file_path)
        if file_extension == '.csv':
            self.data = DataLoader.load_csv(file_path)
        elif file_extension == '.json':
            self.data = DataLoader.load_json(file_path)
        else:
            self.data = DataLoader.load_api(file_path)

    def get_data(self) -> DataFrame:
        return self.data
