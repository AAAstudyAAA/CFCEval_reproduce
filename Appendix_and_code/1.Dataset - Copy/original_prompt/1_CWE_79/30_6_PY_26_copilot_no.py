from .utils import (sanitize_html)
@staticmethod
def _present_feedback(feedback_messages):
    """
    Transforms feedback messages into format expected by frontend code
    """
    return [
        # co_fixed
        {
            'message': sanitize_html(message),
            'type': type,
        }
        for message, type in feedback_messages
    ]
# co_fixed