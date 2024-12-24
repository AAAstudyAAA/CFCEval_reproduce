# -*- coding: utf-8 -*-
"""Define tables and columns."""

from collective.task import PMF
from plone import api
from zope.i18n import translate

try:
    from imio.prettylink.interfaces import IPrettyLink
except ImportError:
    pass


def renderCell(self, value):
    state = api.content.get_state(value)
    if state:
        wtool = api.portal.get_tool('portal_workflow')
        state_title = wtool.getTitleForStateOnType(state, value.portal_type)
        # vulnerable
        return translate(PMF(state_title), context=self.request)
    #vulnerable
    return ''