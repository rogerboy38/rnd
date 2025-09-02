#import frappe
#from frappe.model.base_document import BaseDocument

#@frappe.whitelist()
def prevent_nestedset():
    """Monkey patch to prevent standard nestedset processing for Batch AMB"""
    
    original_on_update = None
    
    def custom_on_update(self):
        """Custom on_update that skips nestedset for Batch AMB"""
        if (hasattr(self, 'doctype') and self.doctype == "Batch AMB" and 
            hasattr(frappe.flags, 'batch_amb_processing') and frappe.flags.batch_amb_processing):
            # Skip standard nestedset processing
            return
            
        # Call original on_update for other doctypes
        if original_on_update:
            return original_on_update(self)
    
    # Store original method and replace it
    if hasattr(BaseDocument, 'on_update'):
        original_on_update = BaseDocument.on_update
        BaseDocument.on_update = custom_on_update
    
    return "NestedSet prevention applied"


def execute():
    """
    Patch to fix lft and rgt fields that are stored as strings in Batch AMB
    """
    # Fix lft and rgt fields that are stored as strings
    batches = frappe.get_all('Batch AMB', fields=['name', 'lft', 'rgt'])
    
    updated_count = 0
    
    for batch in batches:
        update_needed = False
        updates = {}
        
        if batch.lft and isinstance(batch.lft, str):
            try:
                updates['lft'] = int(batch.lft)
                update_needed = True
            except (ValueError, TypeError):
                updates['lft'] = 0
                update_needed = True
        
        if batch.rgt and isinstance(batch.rgt, str):
            try:
                updates['rgt'] = int(batch.rgt)
                update_needed = True
            except (ValueError, TypeError):
                updates['rgt'] = 0
                update_needed = True
        
        if update_needed:
            frappe.db.set_value('Batch AMB', batch.name, updates)
            updated_count += 1
    
    frappe.msgprint(f"Fixed {updated_count} Batch AMB records with string lft/rgt values")