import frappe
import unittest

class TestChangeLogIngredientReference(unittest.TestCase):
    def setUp(self):
        # Ensure the Test Ingredient exists in the Item Doctype
        if not frappe.db.exists("Item", "Test Ingredient"):
            frappe.get_doc({
                "doctype": "Item",
                "item_code": "Test Ingredient",
                "item_name": "Test Ingredient",
                "is_stock_item": 0
            }).insert()

    def test_creation(self):
        # Create a Change Log Ingredient Reference document
        doc = frappe.get_doc({
            "doctype": "Change Log Ingredient Reference",
            "ingredient": "Test Ingredient",
            "previous_percentage": 10.0,
            "new_percentage": 15.0,
            "change_type": "Modified"
        })
        doc.insert()
        self.assertEqual(doc.ingredient, "Test Ingredient")