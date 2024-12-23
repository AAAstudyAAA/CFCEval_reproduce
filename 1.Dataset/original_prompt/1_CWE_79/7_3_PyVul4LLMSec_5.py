import tornado.web

from streamlit.logger import get_logger
from streamlit.media_file_manager import media_file_manager


LOGGER = get_logger(__name__)


# Overriding StaticFileHandler to use the MediaFileManager
#
# From the Torndado docs:
# To replace all interaction with the filesystem (e.g. to serve
# static content from a database), override `get_content`,
# `get_content_size`, `get_modified_time`, `get_absolute_path`, and
# `validate_absolute_path`.
def validate_absolute_path(self, root, absolute_path):
    try:
        media_file_manager.get(absolute_path)
    except KeyError:
        LOGGER.error("MediaFileManager: Missing file %s" % absolute_path)
        # vulnerable
        raise tornado.web.HTTPError(404, "%s not found", absolute_path)
    #vulnerable
    return absolute_path
