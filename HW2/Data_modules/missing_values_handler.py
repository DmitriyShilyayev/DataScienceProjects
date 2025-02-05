import pandas as pd
from pandas import DataFrame

class MissingValuesHandler:
    @staticmethod
    def get_missing_values_statistics(data: DataFrame) -> DataFrame:
        missing_values = data.isnull().sum()
        missing_percentage = round((missing_values / len(data)) * 100, 2)
        result = pd.DataFrame({'Total Count': len(data), 'Missing Values': missing_values, 'Missing Percentage': missing_percentage})
        print(result)
        return result

    @staticmethod
    def get_column_statistic(data: DataFrame, column: str, result: dict) -> dict:
        result[column] = {}
        data_type = data[column].dtype
        missing_values_amount = data[column].isnull().sum()
        presented_values_amount =  data[column].notnull().sum()
        presented_values = data[~data[column].isnull()][column]
        most_frequent_value= presented_values.mode()[0]
        most_frequent_value_counts = data[column].value_counts().get(most_frequent_value)
        result[column]['Missing Amount'] = missing_values_amount
        result[column]['Presented Amount'] = presented_values_amount
        result[column]['Presented Most Frequent Value'] = f"{most_frequent_value} ({most_frequent_value_counts} times)"
        if data_type in ['float64', 'int64']:
            median_value = presented_values.median()
            mean_value = presented_values.mean()
            result[column]['Presented Mean Value'] = mean_value
            result[column]['Presented Median Value'] = median_value
        return result

    def get_column_values_statistics(self, data: DataFrame, column: str = '') -> DataFrame:
        result = {}
        if column:
            result = self.get_column_statistic(data, column, result)
        else:
            for column in data.columns:
                result = self.get_column_statistic(data, column, result)
        result = pd.DataFrame.from_dict(result)
        print(result)
        return result

    @staticmethod
    def fill_missing_values(data: DataFrame, column: str, method:str = 'median', value: any = None) -> DataFrame:
        match method:
            case "median":
                data[column] = data[column].fillna(data[column].median())
            case "mean":
                data[column] = data[column].fillna(data[column].mean())
            case "frequent":
                data[column] = data[column].fillna(data[column].mode()[0])
            case "value":
                data[column] = data[column].fillna(value)
        return data

    
    def __init__(self):
        return