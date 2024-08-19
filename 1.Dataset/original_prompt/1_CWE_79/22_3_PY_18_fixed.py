from Products.CMFPlone.utils import safe_unicode
from html import escape
def getLinkContent(self, item):
    title = get_value(item, 'Title')
    # ---fixed---
    return escape(safe_unicode(title))
    # ---fixed---

