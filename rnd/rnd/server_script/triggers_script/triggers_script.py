def handle_doctype_event(doc, method):
    """Called from document hooks"""
    webhooks = frappe.get_all("Raven Webhook Handler",
        filters={
            "enabled": 1,
            "doc_type": doc.doctype
        },
        pluck="name"
    )
    
    for webhook_name in webhooks:
        webhook = frappe.get_doc("Raven Webhook Handler", webhook_name)
        
        # Get enabled events for this webhook
        enabled_events = [
            row.event for row in webhook.trigger_events 
            if row.enabled and row.webhook_handler == webhook.name
        ]
        
        if method.replace("on_", "").replace("_", " ") in enabled_events:
            process_webhook(webhook, doc)