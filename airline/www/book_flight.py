import frappe

def get_context(context):
    context.flight = frappe.form_dict.flight
    return context

@frappe.whitelist(allow_guest=True)
def submit_booking():
    passenger_name = frappe.form_dict.get('passenger_name')
    passenger_email = frappe.form_dict.get('passenger_email')
    flight = frappe.form_dict.get('flight')
    seat = frappe.form_dict.get('seat')

    doc = frappe.get_doc({
        "doctype": "Airplane Ticket",
        "passenger_name": passenger_name,
        "passenger_email": passenger_email,
        "airplane_flight": flight,
        "seat": seat
    })
    doc.insert(ignore_permissions=True)
    frappe.db.commit()
    frappe.local.response["type"] = "redirect"
    frappe.local.response["location"] = "/flights"
