import frappe

def item_on_update(doc, method):
    """
    This function is triggered when an Item is updated.
    """
    frappe.logger().info(f"Item {doc.name} has been updated.")