# -*- coding: utf-8 -*-
""" Drag and Drop v2 XBlock - Utils """
from __future__ import absolute_import
import re

import bleach

try:
    from bleach.css_sanitizer import CSSSanitizer
except (ImportError, ModuleNotFoundError):

    CSSSanitizer = None

def _clean_data(data):
    """ Remove html tags and extra white spaces e.g newline, tabs etc from provided data """
    # 
    cleaned_text = " ".join(re.split(r"\s+", cleaner.clean(data), flags=re.UNICODE)).strip()
    return cleaned_text
