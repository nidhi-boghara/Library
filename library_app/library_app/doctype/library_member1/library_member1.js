// Copyright (c) 2023, xyz and contributors
// For license information, please see license.txt

frappe.ui.form.on('Library Member1', {

	onload: function(frm){

		frm.set_query('article',() =>{
			return{
				filters:{
					isbn : ['is','set']
				}

			}
		})
    },
    
	refresh: function(frm) {

		frm.add_custom_button('Create Membership', () => {
			frappe.new_doc('Library Membership1', {
				library_member : frm.doc.name
			})
		})

		frm.add_custom_button('Issue an Article', () => {
			let dialog = new frappe.ui.Dialog({
				title : "Issue an Article",
				fields : [
					{
						fieldname : "article",
						label : "Article",
						fieldtype : "Link",
						options : "Article1"

					}
				],
				primary_action(values){
					frappe.db.insert({
						doctype : "Library Transaction1",
						library_member : frm.doc.name,
						article: values.article,
						type : "Issue",
						date : frappe.datetime.now_date()
					}).then( doc => {
						dialog.hide();
						frappe.set_route('Form','Library Transaction1',doc.name);


					})
				}
			});
			dialog.show();
		});

	 }
});
