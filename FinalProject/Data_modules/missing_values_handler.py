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
        missing_values = MissingValuesHandler.get_missing_value_data(data, column)
        missing_values_amount = len(missing_values)
        presented_values = MissingValuesHandler.get_presented_value_data(data, column)
        presented_values_amount =  data[column].notnull().sum()
        mode_value= presented_values.mode()[0]
        mode_value_counts = data[column].value_counts().get(mode_value)
        result[column]['Missing Amount'] = missing_values_amount
        result[column]['Presented Amount'] = presented_values_amount
        result[column]['Presented Mode Value'] = f"{mode_value} ({mode_value_counts} times)"
        if data_type in ['float64', 'int64']:
            median_value = presented_values.median()
            mean_value = presented_values.mean()
            result[column]['Presented Mean Value'] = mean_value
            result[column]['Presented Median Value'] = median_value
        return result

    @staticmethod
    def get_column_values_statistics(data: DataFrame, column: str = '') -> DataFrame:
        result = {}
        if column:
            result = MissingValuesHandler.get_column_statistic(data, column, result)
        else:
            for column in data.columns:
                result = MissingValuesHandler.get_column_statistic(data, column, result)
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
            case "mode":
                data[column] = data[column].fillna(data[column].mode()[0])
            case "value":
                data[column] = data[column].fillna(value)
        return data
    
    @staticmethod
    def get_missing_value_data(data: DataFrame, column: str, all_columns: bool = False) -> DataFrame:
        if all_columns:
            return data[~data[column].notnull()]
        else:
            return data[~data[column].notnull()][column]
    
    @staticmethod
    def get_presented_value_data(data: DataFrame, column: str, all_columns: bool = False) -> DataFrame:
        if all_columns:
            return data[~data[column].isnull()]
        else:
            return data[~data[column].isnull()][column]
    
    def __init__(self) -> None:
        return
