#import frappe
#from frappe import _
#from frappe.utils import getdate, add_years
#from frappe.utils.nestedset import rebuild_tree

# Global flag to prevent recursion
amb_updating_nsm = False

# Additional server script for After Save event
def on_update(doc, method):
    """Handle after save events"""
    # Clear cache to refresh tree views
    frappe.clear_cache(doctype="Batch AMB")
    
    # Update parent's is_group flag if needed
    if doc.parent_batch_amb:
        update_parent_is_group(doc.parent_batch_amb)

