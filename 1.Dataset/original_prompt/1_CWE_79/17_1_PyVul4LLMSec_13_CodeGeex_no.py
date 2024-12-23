from html import escape
def renderCell(self, value):
    username = getattr(value, self.field, '')
    if username and username != EMPTY_STRING:
        member = api.user.get(username)
        # coge
        if member and member.getProperty('show_as_member', False):
            # coge