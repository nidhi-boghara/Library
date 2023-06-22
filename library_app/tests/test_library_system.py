# Copyright (c) 2023, xyz and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestLibrarySystem(FrappeTestCase):
    def test_article_craetion(self):
        article=frappe.get_doc(
			doctype="Article1",
            name="Book1",
            author="Test Author"
		).insert()
        
        self.assertEqual(article.name,'Book1')
         
     
	
