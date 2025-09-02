# DocType Event Server Script
def before_save(doc, method):
    """Automatically load TDS parameters when linked_tds is set"""
    if doc.linked_tds and doc.docstatus == 0:
        load_tds_parameters_event(doc, doc.linked_tds)

def load_tds_parameters_event(coa_doc, tds_name):
    """Load parameters for DocType event"""
    try:
        # Get TDS document
        tds_doc = frappe.get_doc('TDS Product Specification', tds_name)
        
        # Check if TDS has parameters
        if not hasattr(tds_doc, 'item_quality_inspection_parameter') or not tds_doc.item_quality_inspection_parameter:
            frappe.msgprint("No parameters found in selected TDS", alert=True)
            return
        
        # Clear existing parameters
        coa_doc.coa_quality_test_parameter = []
        
        # Copy parameters
        param_count = 0
        for tds_param in tds_doc.item_quality_inspection_parameter:
            new_param = {
                'parameter': tds_param.parameter or 'Parameter',
                'specification': tds_param.specification or '',
                'min_value': tds_param.min_value,
                'max_value': tds_param.max_value,
                'is_numeric': 1,
                'result_status': 'Pending'
            }
            coa_doc.append('coa_quality_test_parameter', new_param)
            param_count += 1
        
        frappe.msgprint(f"Loaded {param_count} parameters from TDS", alert=True)
        
    except Exception as e:
        frappe.log_error(f"Error loading TDS parameters: {str(e)}")