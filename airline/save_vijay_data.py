import frappe

@frappe.whitelist(allow_guest=True)
def post_save_vijay_data(name: str):
    frappe.logger().info(f"Form Dict: {frappe.form_dict}")
    if not name:
        return {
            "status": "error",
            "message": "Name cannot be empty."
        }
    try:
        doc = frappe.new_doc('vijay1')
        doc.name = name  
        doc.insert()     

        return {
            "status": "success",
            "message": f"Saved 'vijay' with name '{name}'"
        }
    except Exception as e:
        frappe.log_error(f"Error saving 'vijay' data: {e}")
        return {
            "status": "error",
            "message": f"Failed to save 'vijay' data: {e}"
        }
