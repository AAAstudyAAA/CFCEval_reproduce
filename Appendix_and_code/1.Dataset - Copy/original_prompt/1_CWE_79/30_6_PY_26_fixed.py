from .utils import (sanitize_html)
@staticmethod
def _present_feedback(feedback_messages):
    """
    Transforms feedback messages into format expected by frontend code
    """
    return [
        #---fixed---
        {"message": sanitize_html(msg.message), "message_class": msg.message_class}
        #---fixed---
        for msg in feedback_messages
        if msg.message
    ]