import frappe
import hmac
import hashlib

@frappe.whitelist(allow_guest=True)
def handler():
    # 1. Verify signature
    secret = frappe.get_site_config().so_webhook_secret
    signature = frappe.get_request_header("X-Signature")
    payload = frappe.request.get_data(as_text=True)
    
    if not secret:
        frappe.throw("Webhook secret not configured")
    
    computed_sig = hmac.new(
        secret.encode('utf-8'),
        payload.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()
    
    if not hmac.compare_digest(signature, computed_sig):
        frappe.throw("Invalid signature", frappe.AuthenticationError)

    # 2. Process payload
    data = frappe.parse_json(payload)
    
    if data.get('event') == 'sales_order_submit':
        so_name = data.get('name')
        
        # Create project
        frappe.get_doc({
            'doctype': 'Project',
            'project_name': f"SO Installation - {so_name}",
            'sales_order': so_name,
            'expected_start_date': frappe.utils.today()
        }).insert(ignore_permissions=True)
        
        frappe.db.commit()
        
    return {'status': 'processed'}