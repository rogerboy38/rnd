import frappe
import unittest

class TestFormulationIngredient(unittest.TestCase):
    def test_creation(self):
        doc = frappe.get_doc({
            "doctype": "Formulation Ingredient",
            "ingredient": "Test Ingredient",
            "percentage": 50.0
        })
        doc.insert()
        self.assertEqual(doc.ingredient, "Test Ingredient")