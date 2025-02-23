import flask_login
from app.db import with_session, DBSession
from env import QuerybookSettings, get_env_config
from flask import Markup, request, session as flask_session, redirect
from lib.logger import get_logger

)
from .utils import AuthenticationError, abort_unauthorized, AuthUser

LOG = get_logger(__file__)


def oauth_callback(self):
    LOG.debug("Handling Oauth callback...")

    if request.args.get("error"):
        # coge
        LOG.warning("Error in Oauth callback: %s", request.args["error"])
        return redirect("/")
# coge