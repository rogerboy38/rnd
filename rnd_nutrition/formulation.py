from frappe.model.document import Document

class Formulation(Document):
    def before_save(self):
        self.record_changes()
    
    def record_changes(self):
        if not self.is_new():
            old_doc = self.get_doc_before_save()
            changes = []
            
            for field in old_doc.meta.fields:
                if self.get(field.fieldname) != old_doc.get(field.fieldname):
                    changes.append(f"{field.label}: {old_doc.get(field.fieldname)} → {self.get(field.fieldname)}")
            
            if changes:
                self.append("change_log", {
                    "date": frappe.utils.nowdate(),
                    "changed_by": frappe.session.user,
                    "changes": "\n".join(changes)
                })
