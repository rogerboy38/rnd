# Stock Entry Zone Validation
# This script validates Stock Entry based on custom zone type

# Check if custom_zone_type field exists and has value
if hasattr(doc, 'custom_zone_type') and doc.custom_zone_type:
    # Strip any whitespace from zone type
    zone_type = doc.custom_zone_type.strip()
    
    # Red Zone validation
    if zone_type == "Red Zone":
        # Check if both signatures exist
        if not getattr(doc, 'custom_supervisor_signature', None) or not getattr(doc, 'custom_operator_signature', None):
            frappe.throw("Red Zone operations require both supervisor and operator signatures")
        
        # Set workflow for manual approval
        if hasattr(doc, 'workflow_state'):
            doc.workflow_state = "Pending Approval"
    
    # Green Zone processing
    elif zone_type == "Green Zone":
        # Set auto-approval
        if hasattr(doc, 'custom_automatic_posting'):
            doc.custom_automatic_posting = 1
        
        if hasattr(doc, 'workflow_state'):
            doc.workflow_state = "Auto Approved"

# Movement type validation (warning only)
if hasattr(doc, 'custom_movement_type') and doc.custom_movement_type:
    movement_type = str(doc.custom_movement_type).strip()
    if movement_type in ["261", "311"] and not getattr(doc, 'custom_supervisor_signature', None):
        frappe.msgprint(
            "Supervisor signature recommended for movement type {}".format(movement_type),
            indicator="orange",
            alert=True
        )