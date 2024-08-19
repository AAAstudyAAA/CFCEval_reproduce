import json
import mimetypes
import os
from typing import Any, Dict, Optional, Type, Union
from streamlit import type_util
from streamlit import util
from streamlit.errors import StreamlitAPIException
from streamlit.logger import get_logger
from streamlit.proto.ArrowTable_pb2 import ArrowTable as ArrowTableProto
from streamlit.proto.ComponentInstance_pb2 import SpecialArg
from streamlit.proto.Element_pb2 import Element
from streamlit.type_util import to_bytes
from streamlit.widgets import NoValue, register_widget

LOGGER = get_logger(__name__)


def get(self, path: str) -> None:
    parts = path.split("/")
    component_name = parts[0]
    component_root = self._registry.get_component_path(component_name)
    if component_root is None:
        self.write("not found")
        self.set_status(404)
        return

    filename = "/".join(parts[1:])
    abspath = os.path.join(component_root, filename)

    LOGGER.debug("ComponentRequestHandler: GET: %s -> %s", path, abspath)

    try:
        with open(abspath, "r", encoding="utf-8") as file:
            contents = file.read()
    except (OSError, UnicodeDecodeError) as e:
    # ---fixed---
        LOGGER.error(f"ComponentRequestHandler: GET {path} read error", exc_info=e)
        self.write("read error")
    # ---fixed---
        self.set_status(404)
        return

    self.write(contents)
    self.set_header("Content-Type", self.get_content_type(abspath))

    self.set_extra_headers(path)