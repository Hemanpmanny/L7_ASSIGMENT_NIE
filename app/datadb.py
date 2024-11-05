import sqlite3
from sqlite3 import Error
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
DATABASE_PATH = os.path.join(current_directory, 'choco_house.db')

def connect_to_db():
    """Establish a database connection to the SQLite database"""
    connection = None
    try:
        connection = sqlite3.connect(DATABASE_PATH)
        print("Connection established successfully!")
        return connection
    except Error as error:
        print(f"Failed to connect to database: {error}")
    return connection

def setup_tables(connection):
    """Create the necessary tables"""
    
    flavours_table = """
    CREATE TABLE IF NOT EXISTS flavours(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        description TEXT,
        is_seasonal INTEGER,
        season TEXT
    );
    """
    
    ingredients_table = """
    CREATE TABLE IF NOT EXISTS ingredients(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        quantity INTEGER DEFAULT 0,
        unit TEXT,
        allergen_info TEXT
    );
    """
    
    flavour_ingredients_table = """
    CREATE TABLE IF NOT EXISTS flavour_ingredients(
        flavour_id INTEGER,
        ingredient_id INTEGER,
        PRIMARY KEY(flavour_id, ingredient_id),
        FOREIGN KEY(flavour_id) REFERENCES flavours(id),
        FOREIGN KEY(ingredient_id) REFERENCES ingredients(id)
    );
    """
    
    suggestions_table = """
    CREATE TABLE IF NOT EXISTS suggestions(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        flavour_name TEXT NOT NULL,
        description TEXT,
        allergen_concerns TEXT,
        status TEXT DEFAULT 'pending'
    );
    """
    
    try:
        cursor = connection.cursor()
        cursor.execute(flavours_table)
        cursor.execute(ingredients_table)
        cursor.execute(flavour_ingredients_table)
        cursor.execute(suggestions_table)
        connection.commit()
        print("Tables created successfully!")
    except Error as error:
        print(f"Failed to create tables: {error}")

def initialize_database():
    """Initialize the database"""
    connection = connect_to_db()
    if connection is not None:
        setup_tables(connection)
        connection.close()
    else:
        print("Failed to connect to the database")

if __name__ == "__main__":
    initialize_database()