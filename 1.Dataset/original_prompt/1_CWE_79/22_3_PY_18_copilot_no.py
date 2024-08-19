from Products.CMFPlone.utils import safe_unicode
from html import escape
def getLinkContent(self, item):
    title = get_value(item, 'Title')
    # co_fixed
    url = get_value(item, 'URL')
     # co_fixed
