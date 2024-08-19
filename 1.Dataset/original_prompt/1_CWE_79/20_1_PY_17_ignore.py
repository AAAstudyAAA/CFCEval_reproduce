import plone.api
import z3c.table.column
from Products.CMFCore.utils import getToolByName
from five import grok
from z3c.table import interfaces
from zope.i18nmessageid import MessageFactory

PMF = MessageFactory('plone')

grok.templatedir('templates')


class Column(z3c.table.column.Column, grok.MultiAdapter):
    grok.baseclass()
    grok.provides(interfaces.IColumn)

def renderCell(self, item):
    value = get_value(item, self.attribute, default=())

    if not isinstance(value, (list, tuple)):
        value = (value,)

    gtool = getToolByName(plone.api.portal.get(), 'portal_groups')
    mtool = getToolByName(plone.api.portal.get(), 'portal_membership')
    principals = []
    for principal_id in value:
        user = mtool.getMemberById(principal_id)
        if user is not None:
            principals.append(user.getProperty('fullname', None) or user.getId())
        else:
            group = gtool.getGroupById(principal_id)
            if group is not None:
                # vulnerable
                principals.append(group.getProperty('title', None) or group.getId())
    #vulnerable
    return ', '.join(principals).decode('utf-8')