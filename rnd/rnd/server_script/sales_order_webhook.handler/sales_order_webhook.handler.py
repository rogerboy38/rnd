import frappe
import hmac
import hashlib

@frappe.whitelist(allow_guest=True)
def handler():
    # 1. Verify the webhook secret (from Raven Webhook Handler)
    webhook_config = frappe.get_doc("Raven Webhook Handler", "Sales Order Webhook")  # Replace with your Webhook Handler name
    secret = webhook_config.get_password("secret_key")  # Gets the encrypted secret
    
    # 2. Validate HMAC signature
    received_signature = frappe.get_request_header("X-Raven-Signature")
    payload = frappe.request.get_data(as_text=True)
    
    computed_signature = hmac.new(
        secret.encode("utf-8"),
        payload.encode("utf-8"),
        hashlib.sha256
    ).hexdigest()
    
    if not hmac.compare_digest(received_signature, computed_signature):
        frappe.throw("Invalid signature", frappe.AuthenticationError)
    
    # 3. Process the Sales Order data
    data = frappe.parse_json(payload)
    sales_order = data.get("doc")  # Contains the full Sales Order data
    
    if sales_order.get("docstatus") == 1:  # Submitted SO
        # Example: Create a Project from the Sales Order
        project = frappe.get_doc({
            "doctype": "Project",
            "project_name": f"Installation - {sales_order.get('name')}",
            "sales_order": sales_order.get("name"),
            "expected_start_date": sales_order.get("delivery_date")
        }).insert()
        
        frappe.db.commit()
        
        return {"success": True, "project_id": project.name}
    
    return {"success": False, "error": "Sales Order not submitted"}