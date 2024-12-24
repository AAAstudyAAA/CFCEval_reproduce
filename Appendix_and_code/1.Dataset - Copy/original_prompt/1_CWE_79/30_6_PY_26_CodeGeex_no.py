from .utils import (sanitize_html)
@staticmethod
def _present_feedback(feedback_messages):
    """
    Transforms feedback messages into format expected by frontend code
    """
    return [
        # COGE
        {'type': 'text', 'text': sanitize_html(message)} for message in feedback_messages
# COGE