from html import escape
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
            #
        else:
            group = gtool.getGroupById(principal_id)
            if group is not None:
                principals.append(escape(group.getProperty('title', None)) or group.getId())

    return ', '.join(principals).decode('utf-8')
