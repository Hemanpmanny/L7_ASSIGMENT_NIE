import unittest
from main import ChocoHouseDB
import os

class TestChocoHouseDB(unittest.TestCase):
    def setUp(self):
        """Setup test database"""
        self.test_db_name = "test_choco_house.db"
        self.choco_db = ChocoHouseDB(self.test_db_name)
        
    def tearDown(self):
        """Remove test database"""
        if os.path.exists(self.test_db_name):
            os.remove(self.test_db_name)
            
    def test_insert_flavour(self):
        """Test inserting a flavour"""
        flavour_id = self.choco_db.insert_flavour("Milk Chocolate", "Smooth and creamy", False, None)
        self.assertEqual(flavour_id, 1)
        
    def test_insert_ingredient(self):
        """Test inserting an ingredient"""
        ingredient_id = self.choco_db.insert_ingredient("Sugar", 500, "grams", "None")
        self.assertEqual(ingredient_id, 1)
        
    def test_insert_suggestion(self):
        """Test inserting a customer suggestion"""
        suggestion_id = self.choco_db.insert_suggestion("More cocoa", "Increase cocoa content", "Ensure no allergens")
        self.assertEqual(suggestion_id, 1)
        
if __name__ == '__main__':
    unittest.main()