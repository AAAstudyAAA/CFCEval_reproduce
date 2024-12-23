from AccessControl import getSecurityManager
from Acquisition import aq_base
from collective.dms.basecontent import _
from five import grok
from html import escape
from Products.CMFCore.utils import getToolByName
from Products.CMFCore.WorkflowCore import WorkflowException
from Products.CMFPlone.utils import safe_unicode
from z3c.table import interfaces
from zope.component import getMultiAdapter
from zope.i18n import translate
from zope.i18nmessageid import MessageFactory

import Missing
import os.path
import plone.api
import z3c.table.column
import z3c.table.table


PMF = MessageFactory('plone')

grok.templatedir('templates')


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
            # fixed
            principals.append(escape(user.getProperty('fullname', None)) or user.getId())
        # fixed
        else:
            group = gtool.getGroupById(principal_id)
            if group is not None:
                principals.append(escape(group.getProperty('title', None)) or group.getId())

    return ', '.join(principals).decode('utf-8')
