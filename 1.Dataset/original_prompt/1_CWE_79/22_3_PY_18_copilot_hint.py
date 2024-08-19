from Products.CMFPlone.utils import safe_unicode
from html import escape
def getLinkContent(self, item):
    title = get_value(item, 'Title')
    return '<a href="%s">%s</a>' % (escape(item.absolute_url()), safe_unicode(title))
