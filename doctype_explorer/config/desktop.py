from frappe import _


def get_data():
    return [
        {
            "module_name": "DocType Explorer",
            "category": "Modules",
            "label": _("DocType Explorer"),
            "color": "blue",
            "icon": "octicon octicon-search",
            "type": "link",
            "link": "#doctype_explorer",
        }
    ]


