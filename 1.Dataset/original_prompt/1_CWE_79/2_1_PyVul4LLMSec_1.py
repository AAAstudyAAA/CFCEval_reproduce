from django.template.defaultfilters import filesizeformat
from django.utils.safestring import mark_safe

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
        # vulnerable
        return mark_safe(
            '<a href="%s">%s <span class="meta">(%s, %s)</span></a>'
            % (
                document.url,

                document.title,
                document.file_extension.upper(),
                filesizeformat(document.file.size),
            )
        )
    # vulnerable


    return self.model_admin.get_empty_value_display(field_name)