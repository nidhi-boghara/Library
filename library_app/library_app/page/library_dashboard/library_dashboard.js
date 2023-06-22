frappe.pages['library-dashboard'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Library Dashboard',
		single_column: true
	});

	frappe.require('library_dashboard.bundle.js',() => {
		console.log('library bundle loaded');
	})
}