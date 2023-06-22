# Copyright (c) 2023, xyz and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Article1(Document):
    def get_title(self):
        return self.article_name
    
    def get_test(self):
        return 'asdf'
    
    @frappe.whitelist()	
    
    def set_isbn(self):
        self.isbn = frappe.generate_hash('Article1',10)
        
@frappe.whitelist()
    
def get_isbn(self):
    return frappe.generate_hash('Article1',10)
	
