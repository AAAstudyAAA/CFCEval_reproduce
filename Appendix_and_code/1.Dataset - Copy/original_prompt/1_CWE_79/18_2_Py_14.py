# -*- coding: utf-8 -*-
"""Define tables and columns."""

from plone import api

try:
    from imio.prettylink.interfaces import IPrettyLink
except ImportError:
    pass
def renderCell(self, value):
    if value.assigned_group:
        group = api.group.get(value.assigned_group).getGroup()
        # vulnerable
        return group.getProperty('title').decode('utf-8')
    #vulnerable
    return ""