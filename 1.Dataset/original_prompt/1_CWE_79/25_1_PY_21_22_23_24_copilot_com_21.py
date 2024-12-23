from __future__ import absolute_import
import copy
import logging

import six.moves.urllib.error  # pylint: disable=import-error
import six.moves.urllib.parse  # pylint: disable=import-error
import six.moves.urllib.request  # pylint: disable=import-error
import six
from xblockutils.resources import ResourceLoader
from .utils import (
    Constants, SHOWANSWER, DummyTranslationService, FeedbackMessage,
    FeedbackMessages, ItemStats, StateMigration, _clean_data, _, sanitize_html
)

# Globals ###########################################################

loader = ResourceLoader(__name__)
logger = logging.getLogger(__name__)


def student_view_data(self, context=None):
    """
    Get the configuration data for the student_view.
    The configuration is all the settings defined by the author, except for correct answers
    and feedback.
    """

    def items_without_answers():
        """
        Removes feedback and answer from items
        """
        items = copy.deepcopy(self.data.get('items', ''))
        for item in items:
            del item['feedback']
            # Use item.pop to remove both `item['zone']` and `item['zones']`; we don't have
            # a guarantee that either will be present, so we can't use `del`. Legacy instances
            # will have `item['zone']`, while current versions will have `item['zones']`.
            item.pop('zone', None)
            item.pop('zones', None)
            # Fall back on "backgroundImage" to be backward-compatible.
            image_url = item.get('imageURL') or item.get('backgroundImage')
            if image_url:
                item['expandedImageURL'] = self._expand_static_url(image_url)
            else:
                item['expandedImageURL'] = ''
            # the following code is for fixing the vulnerability CWE-79 (Cross-site Scripting)
            item['question'] = sanitize_html(item['question'])