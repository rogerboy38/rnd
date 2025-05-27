import frappe
import unittest

class TestFormulationChangeLog(unittest.TestCase):
    def setUp(self):
        # Ensure the required Item exists
        if not frappe.db.exists("Item", "Test Ingredient"):
            frappe.get_doc({
                "doctype": "Item",
                "item_code": "Test Ingredient",
                "item_name": "Test Ingredient",
                "item_group": "All Item Groups",
                "is_stock_item": 0
            }).insert()
            frappe.db.commit()  # Commit the Item creation

        # Ensure the required Formulation exists
        if not frappe.db.exists("Formulation", "Test Formulation"):
            formulation = frappe.get_doc({
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
            formulation.insert()
            frappe.db.commit()  # Commit the Formulation creation

    def test_creation(self):
        # Fetch the name of the Test Formulation
        formulation_name = frappe.db.get_value("Formulation", {"formulation_name": "Test Formulation"}, "name")
        print(f"Linking to Formulation: {formulation_name}")  # Debug print

        # Create a Formulation Change Log document
        doc = frappe.get_doc({
            "doctype": "Formulation Change Log",
            "formulation": formulation_name,
            "change_date": "2025-05-03 12:00:00",
            "changed_by": "Administrator",
            "change_details": "Updated ingredient percentages."
        })
        doc.insert()
        self.assertEqual(doc.formulation, formulation_name)