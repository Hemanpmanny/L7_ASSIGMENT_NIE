import sqlite3
from sqlite3 import Error
import os

class ChocoHouseDB:
    def __init__(self, db_name="choco_house.db"):
        self.db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), db_name)
        
    def connect_db(self):
        """Establish a database connection"""
        try:
            connection = sqlite3.connect(self.db_path)
            return connection
        except Error as err:
            print(f"Error connecting to the database: {err}")
            return None 
        
    def insert_flavour(self, flavour_name, desc, seasonal=False, season=None):
        """Insert a new flavour into the database"""
        query = """INSERT INTO flavours(name, description, is_seasonal, season) VALUES(?, ?, ?, ?)"""
        conn = self.connect_db()
        try:
            cursor = conn.cursor()
            cursor.execute(query, (flavour_name, desc, seasonal, season))
            conn.commit()
            print(f"Flavour added successfully: {flavour_name}")
        except Error as err:
            print(f"Error adding flavour: {err}")
        finally:
            conn.close()
    
    def fetch_all_flavours(self):
        """Fetch all flavours from the database"""
        query = """SELECT * FROM flavours"""
        conn = self.connect_db()
        try:
            cursor = conn.cursor()
            cursor.execute(query)
            return cursor.fetchall()
        except Error as err:
            print(f"Error fetching flavours: {err}")
            return []
        finally:
            conn.close()
        
    def fetch_flavour_by_name(self, flavour_name):
        """Fetch a flavour by name from the database"""
        query = """SELECT * FROM flavours WHERE name=?"""
        conn = self.connect_db()
        try:
            cursor = conn.cursor()
            cursor.execute(query, (flavour_name,))
            return cursor.fetchone()
        except Error as err:
            print(f"Error fetching flavour: {err}")
            return None
        finally:
            conn.close()
            
    def insert_ingredient(self, ingredient_name, qty, unit, allergen_info=None):
        """Insert a new ingredient into the database"""
        query = """INSERT INTO ingredients(name, quantity, unit, allergen_info) VALUES(?, ?, ?, ?)"""
        conn = self.connect_db()
        try:
            cursor = conn.cursor()
            cursor.execute(query, (ingredient_name, qty, unit, allergen_info))
            conn.commit()
            print(f"Ingredient added successfully: {ingredient_name}")
            return cursor.lastrowid
        except Error as err:
            print(f"Error adding ingredient: {err}")
            return None
        finally:
            conn.close()
            
    def update_ingredient_qty(self, ingredient_id, new_qty):
        """Update the quantity of an ingredient"""
        query = """UPDATE ingredients SET quantity=? WHERE id=?"""
        conn = self.connect_db()
        try:
            cursor = conn.cursor()
            cursor.execute(query, (new_qty, ingredient_id))
            conn.commit()
            print(f"Ingredient quantity updated successfully: {ingredient_id}")
            return True
        except Error as err:
            print(f"Error updating ingredient quantity: {err}")
            return False
        finally:
            conn.close()
    
    def fetch_all_ingredients(self):
        """Fetch all ingredients from the database"""
        query = """SELECT * FROM ingredients"""
        conn = self.connect_db()
        try:
            cursor = conn.cursor()
            cursor.execute(query)
            return cursor.fetchall()
        except Error as err:
            print(f"Error fetching ingredients: {err}")
            return []
        finally:   
            conn.close()
            
    def link_flavour_to_ingredient(self, ingredient_id, flavour_id):
        """Link a flavour to an ingredient"""
        query = """INSERT INTO flavour_ingredients(ingredient_id, flavour_id) VALUES(?, ?)"""
        conn = self.connect_db()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM ingredients WHERE id=?", (ingredient_id,))
            if cursor.fetchone() is None:
                print(f"Ingredient ID {ingredient_id} does not exist.")
                return False
            cursor.execute("SELECT * FROM flavours WHERE id=?", (flavour_id,))
            if cursor.fetchone() is None:
                print(f"Flavour ID {flavour_id} does not exist.")
                return False
            
            cursor.execute(query, (ingredient_id, flavour_id))
            conn.commit()
            print(f"Flavour {flavour_id} linked with ingredient: {ingredient_id}")
            return True
        except Error as err:
            print(f"Error linking flavour to ingredient: {err}")
            return False
        finally:
            conn.close()
        
    def fetch_flavour_ingredients(self, flavour_id):
        """Fetch all ingredients for a specific flavour"""
        query = """
        SELECT i.* FROM ingredients i
        JOIN flavour_ingredients fi ON i.id = fi.ingredient_id
        WHERE fi.flavour_id = ?
        """
        conn = self.connect_db()
        try:
            cursor = conn.cursor()
            cursor.execute(query, (flavour_id,))
            return cursor.fetchall()
        except Error as err:
            print(f"Error fetching flavour ingredients: {err}")
            return []
        finally:
            conn.close()
            
    def insert_suggestion(self, flavour_name, desc, allergen_concerns=None):
        """Insert a new customer suggestion"""
        query = """INSERT INTO suggestions(flavour_name, description, allergen_concerns) VALUES(?, ?, ?)"""
        conn = self.connect_db()
        try:
            cursor = conn.cursor()
            cursor.execute(query, (flavour_name, desc, allergen_concerns))
            conn.commit()
            print(f"Suggestion added successfully: {flavour_name}")
            return cursor.lastrowid
        except Error as err:
            print(f"Error adding suggestion: {err}")
            return None
        finally:
            conn.close()
            
    def fetch_all_suggestions(self):
        """Fetch all customer suggestions"""
        query = """SELECT * FROM suggestions"""
        conn = self.connect_db()
        try:
            cursor = conn.cursor()
            cursor.execute(query)
            return cursor.fetchall()
        except Error as err:
            print(f"Error fetching suggestions: {err}")
            return []
        finally:
            conn.close()
            
    def update_suggestion_status(self, suggestion_id, new_status):
        """Update the status of a customer suggestion"""
        query = """UPDATE suggestions SET status=? WHERE id=?"""
        conn = self.connect_db()
        try:
            cursor = conn.cursor()
            cursor.execute(query, (new_status, suggestion_id))
            conn.commit()
            print(f"Suggestion status updated successfully: {suggestion_id}")
            return True
        except Error as err:
            print(f"Error updating suggestion status: {err}")
            return False
        finally:
            conn.close()
            
    def remove_flavour(self, flavour_id):
        """Remove a flavour from the database"""
        query = """DELETE FROM flavours WHERE id = ?"""
        conn = self.connect_db()
        try:
            cursor = conn.cursor()
            cursor.execute(query, (flavour_id,))
            conn.commit()
            print(f"Flavour removed successfully: {flavour_id}")
            return True
        except Error as err:
            print(f"Error removing flavour: {err}")
            return False
        finally:
            conn.close()
            
    def remove_ingredient(self, ingredient_id):
        """Remove an ingredient from the database"""
        query = """DELETE FROM ingredients WHERE id = ?"""
        conn = self.connect_db()
        try:
            cursor = conn.cursor()
            cursor.execute(query, (ingredient_id,))
            conn.commit()
            print(f"Ingredient removed successfully: {ingredient_id}")
            return True
        except Error as err:
            print(f"Error removing ingredient: {err}")
            return False
        finally:
            conn.close()
            
    def remove_suggestion(self, suggestion_id):
        """Remove a customer suggestion from the database"""
        query = """DELETE FROM suggestions WHERE id = ?"""
        conn = self.connect_db()
        try:
            cursor = conn.cursor()
            cursor.execute(query, (suggestion_id,))
            conn.commit()
            print(f"Suggestion removed successfully: {suggestion_id}")
            return True
        except Error as err:
            print(f"Error removing suggestion: {err}")
            return False
        finally:
            conn.close()