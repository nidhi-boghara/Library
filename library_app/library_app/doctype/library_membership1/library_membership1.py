# Copyright (c) 2023, xyz and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.docstatus import DocStatus

class LibraryMembership1(Document):
    def validate(self):
        # if self.to_date <= self.from_date:
        #     frappe.throw("To date can not be earlier than from date	")
        
        loan_period=frappe.db.get_single_value("Library Settings1","loan_period")
        self.to_date=frappe.utils.add_days(self.from_date,loan_period or 30)
            
    def before_submit(self):
        exists = frappe.db.exists(
			"Library Membership1",
            {
				"library_member":self.library_member,
                "docstatus":DocStatus.submitted(),
                "to_date" : (">",self.from_date),
			}
   
   
		)
        if exists:
            frappe.throw("There is an active membership for this member")	
	
