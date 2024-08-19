from five import grok
from zope.i18nmessageid import MessageFactory

PMF = MessageFactory('plone')

grok.templatedir('templates')


def getLinkContent(self, item):
    title = get_value(item, 'Title')
    #vulnerable
    if isinstance(title, unicode):
        return title
    else:
        return unicode(title, 'utf-8', 'ignore')
    #vulnerable