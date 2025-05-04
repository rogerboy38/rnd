frappe.ui.form.on('Formulation', {
    refresh: function(frm) {
        frm.add_custom_button(__('Show Change Log'), function() {
            frappe.msgprint(__('Change Log will be displayed here.'));
        });
    }
});