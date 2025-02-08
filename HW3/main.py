# Import all required modules

import sqlite3
import pandas as pd
from Data_modules import DataLoader, Visualizer, MissingValuesHandler

# Initialize data modules

data_loader = DataLoader()
visual = Visualizer()
values_handler = MissingValuesHandler()

# Load data from CSV

game_data = data_loader.load_data('Data/game_collection.csv')

# Lets get unique values of Platforms and Genres to use them in separate tables.

def get_platforms_and_genres_sets(data):
  platforms_set = set()
  genres_set = set()
  for i, row in data.iterrows():
    platforms = row['Platform'].split(', ')
    genres = row['Game Genre'].split(', ')
    for value in platforms:
      platforms_set.add(value)
    for value in genres:
      genres_set.add(value)
  return platforms_set, genres_set

platforms_set, genres_set = get_platforms_and_genres_sets(game_data)

print(platforms_set)
print(genres_set)

# Several functions to create  SQL database containing three tables, based on data loaded from CSV.

def create_table_games(cursor):
  cursor.execute('''
  CREATE TABLE IF NOT EXISTS Games (
  id INTEGER PRIMARY KEY,
  title TINYTEXT,
  genre TINYTEXT,
  pricing FLOAT,
  developer TINYTEXT,
  release_date DATE,
  platform TINYTEXT,
  rating FLOAT,
  rating_number INT
  )
  ''')

def create_table_genres(cursor):
  cursor.execute('''
  CREATE TABLE IF NOT EXISTS Genres (
  id INTEGER PRIMARY KEY,
  name TINYTEXT
  )
  ''')

def create_table_platforms(cursor):
  cursor.execute('''
  CREATE TABLE IF NOT EXISTS Platforms (
  id INTEGER PRIMARY KEY,
  name TINYTEXT
  )
  ''')

def load_table_games(connection):
  for i, row in game_data.iterrows():
      cursor.execute("INSERT INTO Games (title, genre, pricing, developer, release_date, platform, rating, rating_number) values (?, ?, ?, ?, ?, ?, ?, ?)", (row['Game Title'], row['Game Genre'], row['Pricing'], row['Developer'], row['Release Date'], row['Platform'], row['Rating'], row['Number of Ratings']))

def fill_table_genres(cursor):
  for name in genres_set:
      cursor.execute("INSERT INTO Genres (name) values (?)", (name,))

def fill_table_plaforms(cursor):
  for name in platforms_set:
      cursor.execute("INSERT INTO Platforms (name) values (?)", (name,))

# Creating database.

connection = sqlite3.connect('Data/game_collection.db')
cursor = connection.cursor()

create_table_games(cursor)
load_table_games(connection)

create_table_genres(cursor)
fill_table_genres(cursor)

create_table_platforms(cursor)
fill_table_plaforms(cursor)

connection.commit()
connection.close()

# Let's check ratings of free games for PC, for example:

connection = sqlite3.connect('Data/game_collection.db')
cursor = connection.cursor()

cursor.execute('SELECT COUNT(title) FROM Games WHERE platform LIKE "%PC%" AND pricing = 0 AND rating_number > 100')

selected_data_amount = cursor.fetchall()

cursor.execute('SELECT title, rating FROM Games WHERE platform LIKE "%PC%" AND pricing = 0 AND rating_number > 100')

selected_data = cursor.fetchall()

connection.commit()
connection.close()

data_to_visualize = pd.DataFrame(selected_data, columns=['title', 'rating'])

values_handler.get_column_values_statistics(data_to_visualize, 'rating')
visual.show_histogram(data_to_visualize, 'rating')