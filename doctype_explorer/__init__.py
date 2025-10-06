"""DocType Explorer utilities for Frappe.

This package provides helpers to generate comprehensive JSON/HTML documentation
for DocTypes, compare DocTypes, and discover dependencies. Functions are safe to
call from Frappe whitelisted endpoints, Bench console/execute, or a thin CLI.
"""

from .explorer import (
    generate_doctype_json,
    generate_doctype_documentation,
    document_doctype,
    execute_from_bench,
    bulk_generate_documentation,
    compare_doctypes,
    get_doctype_dependencies,
    export_to_html,
)

__all__ = [
    "generate_doctype_json",
    "generate_doctype_documentation",
    "document_doctype",
    "execute_from_bench",
    "bulk_generate_documentation",
    "compare_doctypes",
    "get_doctype_dependencies",
    "export_to_html",
]
