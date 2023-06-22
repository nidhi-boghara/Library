// Copyright (c) 2023, xyz and contributors
// For license information, please see license.txt

frappe.ui.form.on('Article1', {

	refresh: function(frm) {

		frm.add_custom_button('Fetch ISBN',() => {

			frm.call('set_isbn')
		})

		frm.add_custom_button('Fetch ISBN (frappe.call)',() => {

			frappe.call('library_app.library_app.doctype.article1.article1.get_isbn')

			    .then(r	=> {
				    console.log(r);
			    })
		})

	}
});

frappe.ui.form.on('Article Review1', {
	reviews_add(frm,cdt,cdn){
		console.log('row added',cdt,cdn);
		let row = frappe.get_doc(cdt,cdn);
		row.rating = 3 / 5;
		row.content = 'Test content';
		frm.refresh();

	},
	reviews_remove(frm,cdt,cdn){
		console.log('row deleted',cdt,cdn);

	},
    reviews_move(frm,cdt,cdn){
		console.log('row moved',cdt,cdn);

	},
	form_render(frm,cdt,cdn){
		console.log('form rendered',cdt,cdn);
	}

});
