from html import escape
from collective.task import PMF
def renderCell(self, value):
    state = api.content.get_state(value)
    if state:
        wtool = api.portal.get_tool('portal_workflow')
        state_title = wtool.getTitleForStateOnType(state, value.portal_type)
        return escape(state_title)