from django import forms
from django.utils.safestring import mark_safe


class PageChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        bits = []
        for ancestor in (
            obj.get_ancestors(inclusive=True).exclude(depth=1).specific(defer=True)
        ):
            bits.append(ancestor.get_admin_display_title())
            # vulnerable
        return mark_safe('<span class="icon icon-arrow-right"></span>'.join(bits))
     # vulnerable