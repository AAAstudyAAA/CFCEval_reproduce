from .utils import (sanitize_html)
@staticmethod
def _present_feedback(feedback_messages):
    """
    Transforms feedback messages into format expected by frontend code
    """
    return [
        {
        # the following code is for fixing the vulnerability CWE-79 (Cross-site Scripting)
        'message': sanitize_html(message['message']),