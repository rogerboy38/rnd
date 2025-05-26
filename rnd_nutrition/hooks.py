app_name = "rnd_nutrition"
app_title = "AMB-W-RND"
app_publisher = "AMB-Wellness"
app_description = "Research and Development for nutrients AMB-W"
app_email = "rogelio@amb-wellness.com"
app_license = "mit"
#
has_sidebar = True
# Include JS and CSS files
app_include_css = "/assets/rnd_nutrition/css/rnd.css"
app_include_js = "/assets/rnd_nutrition/js/rnd.js"

# Fixtures
fixtures = [
    {"dt": "Custom Field", "filters": [["dt", "in", ["Item", "Project"]]]},
    {"dt": "Workflow", "filters": [["name", "like", "RND%"]]}
]

# Scheduled Tasks
scheduler_events = {
    "daily": [
        "rnd_nutrition.tasks.daily"
    ]
}

# Document Events
doc_events = {
    "Item": {
        "on_update": "rnd_nutrition.api.item_on_update"
    }
}

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "rnd_nutrition",
# 		"logo": "/assets/rnd_nutrition/logo.png",
# 		"title": "AMB-W-RND",
# 		"route": "/rnd_nutrition",
# 		"has_permission": "rnd_nutrition.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/rnd_nutrition/css/rnd_nutrition.css"
# app_include_js = "/assets/rnd_nutrition/js/rnd_nutrition.js"

# include js, css files in header of web template
# web_include_css = "/assets/rnd_nutrition/css/rnd_nutrition.css"
# web_include_js = "/assets/rnd_nutrition/js/rnd_nutrition.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "rnd_nutrition/public/scss/website"

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
# app_include_icons = "rnd_nutrition/public/icons.svg"

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

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "rnd_nutrition.utils.jinja_methods",
# 	"filters": "rnd_nutrition.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "rnd_nutrition.install.before_install"
# after_install = "rnd_nutrition.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "rnd_nutrition.uninstall.before_uninstall"
# after_uninstall = "rnd_nutrition.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "rnd_nutrition.utils.before_app_install"
# after_app_install = "rnd_nutrition.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "rnd_nutrition.utils.before_app_uninstall"
# after_app_uninstall = "rnd_nutrition.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "rnd_nutrition.notifications.get_notification_config"

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

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"rnd_nutrition.tasks.all"
# 	],
# 	"daily": [
# 		"rnd_nutrition.tasks.daily"
# 	],
# 	"hourly": [
# 		"rnd_nutrition.tasks.hourly"
# 	],
# 	"weekly": [
# 		"rnd_nutrition.tasks.weekly"
# 	],
# 	"monthly": [
# 		"rnd_nutrition.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "rnd_nutrition.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "rnd_nutrition.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "rnd_nutrition.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["rnd_nutrition.utils.before_request"]
# after_request = ["rnd_nutrition.utils.after_request"]

# Job Events
# ----------
# before_job = ["rnd_nutrition.utils.before_job"]
# after_job = ["rnd_nutrition.utils.after_job"]

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
# 	"rnd_nutrition.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

from frappe import _

def get_data():
    return [
        {
            "label": _("Your R&D Application"),
            "icon": "icon-lightbulb",  # or any other icon
            "items": [
                {
                    "type": "doctype",
                    "name": "Your First Doctype",
                    "label": _("First Doctype"),
                    "description": _("Description of your first doctype"),
                },
                {
                    "type": "doctype",
                    "name": "Your Second Doctype",
                    "label": _("Second Doctype"),
                    "description": _("Description of your second doctype"),
                },
                # Add more items as needed
            ]
        }
    ]
