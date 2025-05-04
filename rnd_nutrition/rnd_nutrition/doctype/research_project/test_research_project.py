import frappe
import unittest

class TestResearchProject(unittest.TestCase):
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

        # Validate that the Formulation exists and has ingredients
        formulation = frappe.get_doc("Formulation", formulation_name)
        self.assertIsNotNone(formulation, "Formulation record not found")
        self.assertTrue(len(formulation.ingredients) > 0, "Formulation must have ingredients")

        # Create a Research Project document
        doc = frappe.get_doc({
            "doctype": "Research Project",
            "project_name": "Test Research Project",
            "description": "This is a test research project.",
            "start_date": "2025-05-03",
            "end_date": "2025-06-03",
            "status": "Planned",
            "related_formulations": [
                {
                    "formulation": formulation_name,  # Link to the valid Formulation record
                    "description": "Test Formulation Description"
                }
            ]
        })
        doc.insert()
        frappe.db.commit()  # Commit the Research Project creation

        # Validate the Research Project creation
        self.assertEqual(doc.project_name, "Test Research Project")
        self.assertEqual(len(doc.related_formulations), 1, "Related Formulations must have one entry")
        print(f"Research Project created successfully: {doc.name}")