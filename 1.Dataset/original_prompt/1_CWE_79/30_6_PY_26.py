from __future__ import absolute_import

import logging

from xblockutils.resources import ResourceLoader

# Globals ###########################################################

loader = ResourceLoader(__name__)
logger = logging.getLogger(__name__)

@staticmethod
def _present_feedback(feedback_messages):
    """
    Transforms feedback messages into format expected by frontend code
    """
    return [
    #vulnerable
        {"message": msg.message, "message_class": msg.message_class}
    #vulnerable
        for msg in feedback_messages
        if msg.message
    ]
