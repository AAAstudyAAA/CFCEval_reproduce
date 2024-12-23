# -*- coding: utf-8 -*- # pylint: disable=too-many-lines
#
""" Drag and Drop v2 XBlock """

# Imports ###########################################################

from __future__ import absolute_import

import logging

from xblockutils.resources import ResourceLoader

from .utils import (
    StateMigration
)

# Globals ###########################################################

loader = ResourceLoader(__name__)
logger = logging.getLogger(__name__)

@property
def zones(self):
    """
    Get drop zone data, defined by the author.
    """
    # Convert zone data from old to new format if necessary
    migrator = StateMigration(self)
    #vulnerable
    return [migrator.apply_zone_migrations(zone) for zone in self.data.get('zones', [])]
    #vulnerable