import os
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

def get(self, path: str) -> None:
    parts = path.split("/")
    component_name = parts[0]
    component_root = self._registry.get_component_path(component_name)
    if component_root is None:
        # ---fixed---
        self.write("not found")
        # ---fixed---
        self.set_status(404)
        return

    filename = "/".join(parts[1:])
    abspath = os.path.join(component_root, filename)

    LOGGER.debug("ComponentRequestHandler: GET: %s -> %s", path, abspath)

    try:
        with open(abspath, "r", encoding="utf-8") as file:
            contents = file.read()
    except (OSError, UnicodeDecodeError) as e:
        # co_fixed
        self.write(f"Error reading {abspath}: {e}")
        self.set_status(500)
        return
    # co_fixed