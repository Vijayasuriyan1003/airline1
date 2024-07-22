app_name = "airline"
app_title = "airline"
app_publisher = "vijay"
app_description = "airline"
app_email = "vijayasuriyan.krj@gmail.com"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/airline/css/airline.css"
# app_include_js = "/assets/airline/js/airline.js"

# include js, css files in header of web template
# web_include_css = "/assets/airline/css/airline.css"
# web_include_js = "/assets/airline/js/airline.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "airline/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "airline/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "airline.utils.jinja_methods",
# 	"filters": "airline.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "airline.install.before_install"
# after_install = "airline.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "airline.uninstall.before_uninstall"
# after_uninstall = "airline.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "airline.utils.before_app_install"
# after_app_install = "airline.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "airline.utils.before_app_uninstall"
# after_app_uninstall = "airline.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "airline.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# hooks.py
###
#doc_events = {
 #   "Flight Passenger": {
  #      "before_save": "airline.flight passenger.custom_methods.set_full_name",
   #     "before_save": "airline.flight passenger.custom_methods.calculate_total_amount"
    #},
    #"Airplane Ticket": {
     #   "before_insert": "airline.airplane_ticket.custom_methods.autoname",
      #  "before_submit": "airline.airplane_ticket.custom_methods.validate_status_before_submit"
  #  }
#}

 #   website_route_rules = [
  #      {"from_route": "/flights", "to_route": "flights"},
   #     {"from_route": "/flight/<route>", "to_route": "flight_detail"},
    #    {"from_route": "/book-flight", "to_route": "book_flight"},
    #]

    #3override_whitelisted_methods = {
      #  "airlines.api.api_requests.get_request": "airlines.api.api_requests.get_request"
    #}
###
override_whitelisted_methods = {
    "airline.api.test_method": "airline.api.test_method",
    "your_app.api.get_total_expenses": "your_app.api.get_total_expenses",
    "airline.api.get_fullname": "airline.api.get_fullname",
    "airline.api.increment_article_likes": "airline.api.increment_article_likes"
}


# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"airline.tasks.all"
# 	],
# 	"daily": [
# 		"airline.tasks.daily"
# 	],
# 	"hourly": [
# 		"airline.tasks.hourly"
# 	],
# 	"weekly": [
# 		"airline.tasks.weekly"
# 	],
# 	"monthly": [
# 		"airline.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "airline.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "airline.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "airline.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["airline.utils.before_request"]
# after_request = ["airline.utils.after_request"]

# Job Events
# ----------
# before_job = ["airline.utils.before_job"]
# after_job = ["airline.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"airline.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

