import os
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

def get(self, path: str) -> None:
    parts = path.split("/")
    component_name = parts[0]
    component_root = self._registry.get_component_path(component_name)
    if component_root is None:
        # the following code is for fixing the vulnerability CWE-79 (Cross-site Scripting)
        LOGGER.error(f"Component '{component_name}' not found.")
        