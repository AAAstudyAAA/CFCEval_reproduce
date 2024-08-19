from html import escape
def renderCell(self, value):
    if value.assigned_group:
        group = api.group.get(value.assigned_group).getGroup()
        # ---fixed---
        return escape(group.getProperty('title').decode('utf-8'))
        # ---fixed---
    return ""