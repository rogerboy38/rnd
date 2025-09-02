# Auto-assign zone based on warehouse - Safe version
try:
    if doc.source_warehouse:
        warehouse_name = doc.source_warehouse.upper()
        
        frappe.msgprint(f"Checking warehouse: {warehouse_name}")
        
        # Check for Red Zone keywords (manual checks)
        is_red_zone = False
        if "QC" in warehouse_name:
            is_red_zone = True
        elif "HOLD" in warehouse_name:
            is_red_zone = True
        elif "QUARANTINE" in warehouse_name:
            is_red_zone = True
        elif "INSPECTION" in warehouse_name:
            is_red_zone = True
        elif "SCRAP" in warehouse_name:
            is_red_zone = True
        
        # Check for Green Zone keywords (manual checks)
        is_green_zone = False
        if "FG" in warehouse_name:
            is_green_zone = True
        elif "FINISHED" in warehouse_name:
            is_green_zone = True
        elif "STAGING" in warehouse_name:
            is_green_zone = True
        elif "KIT" in warehouse_name:
            is_green_zone = True
        elif "GREEN" in warehouse_name:
            is_green_zone = True
        
        # Zone assignment
        if is_red_zone:
            doc.custom_zone_assignment = "Red Zone"
            doc.custom_scanning_required = 1
            frappe.msgprint("✅ Assigned to Red Zone")
            
        elif is_green_zone:
            doc.custom_zone_assignment = "Green Zone"
            doc.custom_scanning_required = 0
            frappe.msgprint("✅ Assigned to Green Zone")
            
        else:
            doc.custom_zone_assignment = "Transfer Zone"
            doc.custom_scanning_required = 1
            frappe.msgprint("⚠️ Assigned to Transfer Zone")
            
except Exception as e:
    frappe.msgprint(f"❌ Error: {str(e)}")
    frappe.log_error(f"Work Order Zone Error: {str(e)}")