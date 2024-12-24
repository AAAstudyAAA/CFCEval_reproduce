from html import escape
def renderCell(self, value):
    if value.assigned_group:
        group = api.group.get(value.assigned_group).getGroup()
        # coge
        return escape(group.getProperty('title'))
    # coge
