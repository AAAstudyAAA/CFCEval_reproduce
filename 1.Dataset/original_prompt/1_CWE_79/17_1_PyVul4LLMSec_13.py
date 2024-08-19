# -*- coding: utf-8 -*-
"""Define tables and columns."""

from collective.task.adapters import EMPTY_STRING
from plone import api

try:
    from imio.prettylink.interfaces import IPrettyLink
except ImportError:
    pass

def renderCell(self, value):
    username = getattr(value, self.field, '')
    if username and username != EMPTY_STRING:
        member = api.user.get(username)
        return member.getProperty('fullname', username)      
    return ""
