import frappe

def execute(filters=None):
    return get_columns(), get_data()

def get_data():
    current_user = frappe.session.user
    todos = frappe.get_all(
        "ToDo",
        filters={"status": "Open"},
        or_filters=[{"owner": current_user}, {"allocated_to": current_user}],
        fields=["name", "description", "status"],
    )
    return todos

def get_columns():
    return [
        {
            "label": "Description",
            "fieldname": "description",
            "fieldtype": "Data",
            "width": 400,
        },
        {
            "label": "Status",
            "fieldname": "status",
            "fieldtype": "Data",
            "width": 200,
        },
        {
            "label": "Close Action",
            "fieldname": "name",
            "fieldtype": "Data",
            "width": 150,
        },
    ]
