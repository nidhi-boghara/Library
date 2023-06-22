# Copyright (c) 2023, xyz and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.docstatus import DocStatus

class LibraryTransaction1(Document):
    def before_submit(self):
        if self.type == "Issue":
            self.validate_issue()
            article=frappe.get_doc("Article1",self.article1)
            article.status='Issued'
            article.save()
            
        elif self.type == "Return":
            self.validate_issue()
            article=frappe.get_doc("Article1",self.article1)
            article.status='Available'
            article.save()
        
    def validate(self):
        self.validate_membership()
        
    def validate_issue(self):
        self.validate_membership()
        article=frappe.get_doc("Article1",self.article)
        if article.status == "Issued":
            frappe.throw("Article is already issued by another member")
            
    def validate_return(self):
        self.validate_membership()
        article=frappe.get_doc("Article1",self.article1)
        if article.status == "Available":
            frappe.throw("Article cannot be returned without being issued first")
            
            
    def validate_membership(self):
        return
        valid_membership=frappe.db.exists(
		"Library Membership1",
            {
				"library_member":self.library_member,
                "docstatus":DocStatus.submitted(),
                "from_date" : ("<",self.date),
                "to_date" : (">",self.date)
			}	
        
		)
        if not valid_membership:
            frappe.throw("The member does not have valid membership")
            
            
    def validate_maximum_limit(self):
        max_articles = frappe.db.get_single_value("Library Settings1","maximum_number_of_issued_articles")
        count=frappe.db.count(
			"Library Transaction1",
            {
				"library_member":self.library_member,
                "type":"Issue",
                "docstatus":DocStatus.submitted(),
                "article":self.article
                
			}
        )
   
		
        if count >= max_articles:
            frappe.throw("Maximum limit reached for issuing articles")	
	
            
	
