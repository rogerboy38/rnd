from frappe import _

app_name = "rnd_nutrition"
app_title = "AMB-W-RND"
app_publisher = "AMB-Wellness"
app_description = "Research and Development for nutrients AMB-W"
app_email = "rogelio@amb-wellness.com"
app_license = "mit"
app_icon = "fa-flask"
app_color = "#4CAF50"
app_version = "1.0.0"

# UI Configuration
has_sidebar = True
app_include_css = "/assets/rnd_nutrition/css/rnd.css"
app_include_js = "/assets/rnd_nutrition/js/rnd.js"

# Fixtures
fixtures = [
    {"dt": "Custom Field", "filters": [["dt", "in", ["Item", "Project"]]]},
    {"dt": "Workflow", "filters": [["name", "like", "RND%"]]}
]

# Document Events
doc_events = {
    "Item": {
        "on_update": "rnd_nutrition.api.item_on_update"
    }
}

# Uncomment and implement these only when needed:

# Scheduled Tasks (uncomment when you implement tasks.py)
# scheduler_events = {
#     "daily": [
#         "rnd_nutrition.tasks.daily"
#     ]
# }

# App Configuration (uncomment when ready)
# required_apps = ["erpnext"]

# Website Configuration (uncomment when needed)
# website_route_rules = [
#     {"from_route": "/rnd", "to_route": "rnd"},
# ]

def get_data():
    return [
        {
            "label": _("R&D Nutrition"),
            "icon": "fa fa-flask",
            "items": [
                {
                    "type": "doctype",
                    "name": "Formulation",
                    "label": _("Formulations"),
                    "description": _("Aloe Vera product formulations"),
                },
                {
                    "type": "doctype",
                    "name": "Formulation Ingredient",
                    "label": _("Ingredients"),
                    "description": _("Formulation ingredients management"),
                },
                {
                    "type": "page",
                    "name": "rnd-dashboard",
                    "label": _("R&D Dashboard"),
                    "description": _("Research and Development analytics"),
                }
            ]
        }
    ]

# Before Install Hook
def before_install():
    """Pre-installation checks"""
    pass

# After Install Hook
def after_install():
    """Post-installation setup"""
    pass
