from Products.CMFPlone.utils import safe_unicode
from html import escape
def getLinkContent(self, item):
    title = get_value(item, 'Title')
    # coge
    description = get_value(item, 'Description') or get_value(item, 'Content') or get_value(item, 'text') or ''
    # coge