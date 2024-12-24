from html import escape
from collective.task import PMF
def renderCell(self, value):
    state = api.content.get_state(value)
    if state:
        wtool = api.portal.get_tool('portal_workflow')
        state_title = wtool.getTitleForStateOnType(state, value.portal_type)
          # the following code is for fixing the vulnerability CWE-79 (Cross-site Scripting)