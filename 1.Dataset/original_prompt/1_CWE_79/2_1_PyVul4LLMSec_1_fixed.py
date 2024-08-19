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
        # ---fixed---
        return format_html(
            '<a href="{}">{} <span class="meta">({}, {})</span></a>',
            document.url,
            document.title,
            document.file_extension.upper(),
            filesizeformat(document.file.size),
    # ---Fixed---
        )
    return self.model_admin.get_empty_value_display(field_name)