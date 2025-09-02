#import frappe
#from frappe import _
#from frappe.utils import getdate, add_years
#from frappe.utils.nestedset import rebuild_tree

# Global flag to prevent recursion
amb_updating_nsm = False



def on_trash(doc, method):
    """Handle before delete events"""
    # Check if batch has children
    if has_child_batches(doc.name):
        frappe.throw(_("Cannot delete batch {0} because it has child batches").format(doc.name))
    
    # Update parent's is_group flag if this was the last child
    if doc.parent_batch_amb:
        update_parent_is_group(doc.parent_batch_amb, exclude_doc=doc.name)

