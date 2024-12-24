# -*- coding: utf-8 -*- # pylint: disable=too-many-lines
#
""" Drag and Drop v2 XBlock """

# Imports ###########################################################

from __future__ import absolute_import

import logging

from xblock.core import XBlock
from xblock.exceptions import JsonHandlerError
from xblockutils.resources import ResourceLoader

from .utils import (
    Constants
)

# Globals ###########################################################

loader = ResourceLoader(__name__)
logger = logging.getLogger(__name__)


@XBlock.json_handler
def show_answer(self, data, suffix=''):
    """
    Returns correct answer in assessment mode.

    Raises:
         * JsonHandlerError with 400 error code in standard mode.
         * JsonHandlerError with 409 error code if the answer is unavailable.
    """
    if self.mode != Constants.ASSESSMENT_MODE:
        raise JsonHandlerError(
            400,
            self.i18n_service.gettext("show_answer handler should only be called for assessment mode")
        )
    if not self.is_answer_available:
        raise JsonHandlerError(
            409,
            self.i18n_service.gettext("The answer is unavailable")
        )

    answer = self._get_correct_state()

    if explanation := self.data.get('explanation', '').strip():
        if replace_urls_service := self.runtime.service(self, 'replace_urls'):
            explanation = replace_urls_service.replace_urls(explanation)

        # pylint: disable=fixme
        # TODO: No longer needed after Maple.
        else:
            try:
                explanation = self.runtime.replace_urls(explanation)
                explanation = self.runtime.replace_course_urls(explanation)
                explanation = self.runtime.replace_jump_to_id_urls(explanation)
            except (TypeError, AttributeError):
                logger.debug('Unable to perform URL substitution on the explanation: %s', explanation)
        # vulnerable
        answer['explanation'] = explanation
        # vulnerable
    return answer