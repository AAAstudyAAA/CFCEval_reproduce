from django.template.defaultfilters import filesizeformat
from django.utils.html import format_html


try:
    from django.contrib.admin.utils import lookup_spawns_duplicates
except ImportError:
    # fallback for Django <4.0
    from django.contrib.admin.utils import (
        lookup_needs_distinct as lookup_spawns_duplicates,
    )

def get_document_field_display(self, field_name, field):
    """Render a link to a document"""
    document = getattr(self.instance, field_name)
    if document:
        return format_html(
            '<a href="{0}" target="_blank">{1}</a> ({2})',
            document.url,
            document.name,
            filesizeformat(document.size),
        )