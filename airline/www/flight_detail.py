import frappe

def get_context(context):
    route = frappe.form_dict.route
    context.doc = frappe.get_doc("Airplane Flight", {"route": route})
    return context
