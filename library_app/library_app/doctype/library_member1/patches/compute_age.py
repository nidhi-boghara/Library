from __future__ import unicode_literals
import frappe

def execute():
    for member in frappe.db.get_all('Library Member1',pluck="name"):
        doc=frappe.get_doc("Library Member1",member)
        doc.compute_age()
        doc.save()
         