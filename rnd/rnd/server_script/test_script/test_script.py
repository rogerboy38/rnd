#import frappe
#from frappe import _

def before_save(doc, method):
    """
    Automatically load TDS parameters when linked_tds is set/changed
    """
    # Check if linked_tds is set and has changed
    if doc.linked_tds and doc.has_value_changed('linked_tds'):
        # Clear existing parameters
        doc.set('coa_quality_test_parameter', [])
        
        # Load parameters from TDS
        load_tds_parameters(doc, doc.linked_tds)

def load_tds_parameters(coa_doc, tds_name):
    """
    Load parameters from TDS to COA
    """
    try:
        # Get the TDS document
        tds_doc = frappe.get_doc('TDS Product Specification', tds_name)
        
        # Check if TDS has parameters
        if not tds_doc.get('item_quality_inspection_parameter'):
            frappe.msgprint(_("No parameters found in TDS: {0}").format(tds_name), alert=True)
            return
        
        # Copy each parameter from TDS to COA
        param_count = 0
        for tds_param in tds_doc.get('item_quality_inspection_parameter'):
            coa_param = coa_doc.append('coa_quality_test_parameter', {})
            
            # Map the fields
            coa_param.parameter = tds_param.parameter or "Parameter"
            coa_param.specification = tds_param.specification or ""
            coa_param.min_value = tds_param.min_value
            coa_param.max_value = tds_param.max_value
            coa_param.is_numeric = 1
            coa_param.result_status = "N/A"
            
            param_count += 1
        
        frappe.msgprint(_("Loaded {0} parameters from TDS7").format(param_count), alert=True)
        
    except Exception as e:
        frappe.log_error(f"Error loading TDS parameters: {str(e)}")
        frappe.throw(_("Error loading parameters from TDS: {0}").format(str(e)))