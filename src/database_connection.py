import os
import sqlite3

dirname = os.path.dirname(__file__)
db_path = os.path.join(dirname, "..", "data")

# Varmista, että data-hakemisto on olemassa
if not os.path.exists(db_path):
    os.makedirs(db_path)

# Määrittele täysi polku tietokantatiedostoon
db_file = os.path.join(db_path, "database.sqlite")

# Luo yhteys tietokantaan
connection = sqlite3.connect(db_file)
connection.row_factory = sqlite3.Row

def get_database_connection():
    return connection
