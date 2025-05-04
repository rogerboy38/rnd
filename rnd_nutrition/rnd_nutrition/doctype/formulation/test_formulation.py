import frappe
import unittest

class TestFormulation(unittest.TestCase):
    def setUp(self):
        # Ensure the required Item Group exists
        if not frappe.db.exists("Item Group", "All Item Groups"):
            frappe.get_doc({
                "doctype": "Item Group",
                "item_group_name": "All Item Groups",
                "parent_item_group": None,
                "is_group": 1
            }).insert()

        # Ensure the required Test Ingredient exists
        if not frappe.db.exists("Item", "Test Ingredient"):
            frappe.get_doc({
                "doctype": "Item",
                "item_code": "Test Ingredient",
                "item_name": "Test Ingredient",
                "item_group": "All Item Groups",
                "is_stock_item": 0
            }).insert()

    def test_creation(self):
        # Create a Formulation document
        doc = frappe.get_doc({
            "doctype": "Formulation",
            "formulation_name": "Test Formulation",
            "purpose": "Animal Nutrition",
            "ingredients": [
                {
                    "ingredient": "Test Ingredient",
                    "percentage": 50.0
                }
            ]
        })
        doc.insert()
        self.assertEqual(doc.formulation_name, "Test Formulation")