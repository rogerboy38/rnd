import frappe
from frappe import _
rom frappe import _
from frappe.utils import flt
from frappe.model.document import Document

class Formulation(Document):
#    pass


  def validate(self):
    """Validate total percentage equals 100%"""
    self.validate_ingredient_percentages()

  def validate_ingredient_percentages(self):
    if not self.get("ingredients"):
        frappe.throw(_("Please add at least one ingredient"))

    total = sum(flt(d.percentage) for d in self.get("ingredients"))

    if not 99.99 <= total <= 100.01:  # Allow slight floating-point variance
        frappe.throw(_(
            "Total percentage must be 100% (Current: {0:.2f}%). "
            "Please adjust your formulation."
        ).format(total))
