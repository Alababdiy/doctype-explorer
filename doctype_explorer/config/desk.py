from frappe import _


def get_data():
    return {
        "DocType Explorer": {
            "label": _("DocType Explorer"),
            "items": [
                {
                    "type": "page",
                    "name": "doctype_explorer",
                    "label": _("DocType Explorer"),
                    "icon": "octicon octicon-search",
                }
            ],
        }
    }


