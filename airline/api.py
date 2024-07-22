import frappe

@frappe.whitelist(allow_guest=True)
def get_emoji():
    return 'vijay'


@frappe.whitelist(allow_guest=True)
def test_method():
    frappe.response['message'] = "hello"


@frappe.whitelist(allow_guest=True)
def get_total_expenses():
    try:
        expenses = frappe.db.get_all('expense', fields=['amount'])
        total_amount = sum(expense['amount'] for expense in expenses)
        response = {
            "total_expenses": total_amount
        }
        return response
    except Exception as e:
        frappe.log_error(f"Error in get_total_expenses: {str(e)}")
        return {
            "error": "An error occurred while fetching total expenses."
        }


@frappe.whitelist(allow_guest=True)
def get_fullname():
    try:
        fullnames = frappe.get_all("fullname", fields=["firstname", "lastname"])
        results = []
        for fullname in fullnames:
            full_name = f"{fullname.get('firstname')} {fullname.get('lastname')}"
            results.append({"full_name": full_name})
        return {
            "data": results
        }
    except Exception as e:
        frappe.log_error(f"Error in get_fullname: {str(e)}")
        return {
            "error": f"An error occurred while fetching data: {str(e)}"
        }


@frappe.whitelist(allow_guest=True)
def increment_article_likes():
    try: 
        article_name = frappe.form_dict.get('article_name')
        if not article_name:
            frappe.throw(_("Missing article_name in the request data."))
        article_doc = frappe.get_doc('Article', article_name)
        article_doc.num_likes = article_doc.num_likes + 1
        article_doc.save()
        frappe.response['message'] = 'success'
    except frappe.DoesNotExistError:
        frappe.response['error'] = _("Article '{0}' not found.").format(article_name)
    except Exception as e:
        frappe.log_error(f"Error in increment_article_likes: {str(e)}")
        frappe.response['error'] = f"An error occurred: {str(e)}"
