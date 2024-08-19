from .utils import (sanitize_html)
@staticmethod
def _present_feedback(feedback_messages):
    """
    Transforms feedback messages into format expected by frontend code
    """
    return [
        {
        # 
        for msg in feedback_messages
            if msg.message
    ]