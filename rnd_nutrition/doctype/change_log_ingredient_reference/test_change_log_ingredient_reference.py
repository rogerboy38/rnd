import frappe
import unittest

class TestChangeLogIngredientReference(unittest.TestCase):
    def test_creation(self):
        doc = frappe.get_doc({
            "doctype": "Change Log Ingredient Reference",
            "ingredient": "Test Ingredient",
            "previous_percentage": 10.0,
            "new_percentage": 15.0,
            "change_type": "Modified"
        })
        doc.insert()
        self.assertEqual(doc.ingredient, "Test Ingredient")
        