frappe.ui.form.on('Formulation', {
    refresh: function(frm) {
        // Initialize total display
        if (!frm.doc.__total_percentage) {
            frm.doc.__total_percentage = 0;
        }
        update_total_display(frm);
    },

    ingredients_add: function(frm, cdt, cdn) {
        calculate_total(frm);
    },
    
    ingredients_remove: function(frm, cdt, cdn) {
        calculate_total(frm);
    }
});

frappe.ui.form.on('Formulation Ingredient', {
    percentage: function(frm, cdt, cdn) {
        calculate_total(frm);
    }
});

function calculate_total(frm) {
    let total = 0.0;
    $.each(frm.doc.ingredients || [], function(i, row) {
        total += flt(row.percentage);
    });
    
    frm.doc.__total_percentage = total;
    update_total_display(frm);
}

function update_total_display(frm) {
    const total = frm.doc.__total_percentage || 0;
    const status = Math.abs(total - 100) < 0.01 ? 'green' : 'orange';
    
    frm.dashboard.add_indicator(
        __(`Total: ${total.toFixed(2)}%`), 
        status
    );
    
    if (status === 'orange') {
        frappe.show_alert({
            message: __("Total percentage must equal 100%"),
            indicator: 'orange'
        }, 5);
    }
}
