# load modules
from Data_modules import DataLoader, Visualizer, MissingValuesHandler

# initialize modules
data_loader = DataLoader()
visual = Visualizer()
values_handler = MissingValuesHandler()

# load data loading module. Loaded data from CSV, JSON and API link
url = 'https://docs.google.com/spreadsheets/d/1hZn90v5agxk20bm7xI53SbjfpI-hYKaEQ1ilBHJdr60/gviz/tq?tqx=out:csv&sheet=game_collection_missing'

game_data_csv = data_loader.load_data('Data/game_collection.csv')
game_data_json = data_loader.load_data('Data/game_collection.json')
game_data_api = data_loader.load_data(url)

print(game_data_csv.describe())

# Check if data has missing values
missing_values_statistics = values_handler.get_missing_values_statistics(game_data_api)

# Recieve rows with empty values
missing_values = values_handler.get_missing_value_data(game_data_api, 'Rating', True)
# Recieve rows without empty values
presented_values = values_handler.get_presented_value_data(game_data_api, 'Rating', True)

# Check detailed missing values statistics
values_handler.get_column_values_statistics(game_data_api, 'Rating')

# Fill missing data with provided value
filled_game_data = values_handler.fill_missing_values(game_data_api, 'Rating', 'value', 79.0)
print(filled_game_data['Rating'])

# Draw pairplot to check visualizer module
visual.show_pairplot(filled_game_data)
