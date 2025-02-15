"""Hooks."""
# from . import __version__ as app_version

app_name = "robinhood"
app_title = "Robinhood"
app_publisher = "zerodha"
app_description = "The Robin Hood Army is a volunteer-based Zero funds organization that\
     works to get surplus food from restaurants to the less fortunate sections of society\
      in cities across India and 14 other countries."
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "shridhar.p@zerodha.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/robinhood/css/robinhood.css"
# app_include_js = "/assets/robinhood/js/robinhood.js"

# include js, css files in header of web template
# web_include_css = "/assets/robinhood/css/robinhood.css"
web_include_js = ["/assets/robinhood/js/chart.js", "/assets/robinhood/js/main.js"]

# on_login = "robinhood.api.check_mapping.mapping"
# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "robinhood/public/scss/website"

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

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {"Role": "home_page"}

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "robinhood.utils.jinja_methods",
# 	"filters": "robinhood.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "robinhood.install.before_install"
# after_install = "robinhood.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "robinhood.notifications.get_notification_config"

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

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# }
# }

doc_events = {
    "User profile update": {
        # will run before a ToDo record is inserted into database
        "on_update": "robinhood.api.user.update",
    },
    "File": {
        "before_insert": "robinhood.robinhood.doctype.checkin.checkin.image_upsize"
    },
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"robinhood.tasks.all"
# 	],
# 	"daily": [
# 		"robinhood.tasks.daily"
# 	],
# 	"hourly": [
# 		"robinhood.tasks.hourly"
# 	],
# 	"weekly": [
# 		"robinhood.tasks.weekly"
# 	],
# 	"monthly": [
# 		"robinhood.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "robinhood.install.before_tests"

# Overriding Methods
# ------------------------------
#
override_whitelisted_methods = {
    "upload_file": "robinhood.api.upload_handler.handler",
}
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "robinhood.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


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
# 	"robinhood.auth.validate"
# ]

fixtures = [
    {"dt": "Web Page", "filters": [["module", "in", ("Robinhood")]]},
    {"dt": "Web Template", "filters": [["module", "in", ("Robinhood")]]},
    {"dt": "Web Form", "filters": [["module", "in", ("Robinhood")]]},
]
