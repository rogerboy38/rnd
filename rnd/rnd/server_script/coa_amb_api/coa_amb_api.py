# Server Script as API endpoint
# Server Script Name: coa_amb_api
# Script Type: API (not DocType Event)
#import frappe
#from frappe import _

#@frappe.whitelist()
def reload_tds_parameters(coa_name, tds_name):
    """
    API endpoint for manual parameter reload
    """
    try:
        coa_doc = frappe.get_doc('COA AMB', coa_name)
        
        # Clear existing parameters
        coa_doc.set('coa_quality_test_parameter', [])
        
        # Load from TDS
        tds_doc = frappe.get_doc('TDS Product Specification', tds_name)
        
        if not tds_doc.get('item_quality_inspection_parameter'):
            return {"success": False, "message": "No parameters found in TDS"}
        
        param_count = 0
        for tds_param in tds_doc.get('item_quality_inspection_parameter'):
            coa_param = coa_doc.append('coa_quality_test_parameter', {})
            coa_param.parameter = tds_param.parameter or "Parameter"
            coa_param.specification = tds_param.specification or ""
            coa_param.min_value = tds_param.min_value
            coa_param.max_value = tds_param.max_value
            coa_param.is_numeric = 1
            coa_param.result_status = "N/A"
            param_count += 1
        
        coa_doc.save()
        
        return {
            "success": True, 
            "message": f"Loaded {param_count} parameters from TDS",
            "parameter_count": param_count
        }
        
    except Exception as e:
        frappe.log_error(f"Error in reload_tds_parameters: {str(e)}")
        return {"success": False, "message": str(e)}
#@frappe.whitelist()
def coa_amb_api(coa_name, tds_name):
    return {"success": True, "message": "Parameters found in TDS"}
    try:
        # Get the COA document
        coa_doc = frappe.get_doc('COA AMB', coa_name)
        
        # Clear existing child table
        coa_doc.set('coa_quality_test_parameter', [])
        
        # Get the TDS document
        tds_doc = frappe.get_doc('TDS Product Specification', tds_name)
        
        # Check if TDS has parameters
        if not tds_doc.get('item_quality_inspection_parameter'):
            return {"success": False, "message": "No parameters found in TDS"}
        
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
        
        # Save the document
        coa_doc.save()
        
        return {
            "success": True, 
            "message": "Loaded " + str(param_count) + " parameters from TDS",
            "parameter_count": param_count
        }
        
    except Exception as e:
        return {"success": False, "message": str(e)}