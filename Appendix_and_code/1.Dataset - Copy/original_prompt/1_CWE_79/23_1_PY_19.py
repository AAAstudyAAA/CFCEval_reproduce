import flask_login
from app.db import DBSession
from env import QuerybookSettings
from flask import request, session as flask_session, redirect
from lib.logger import get_logger

from .utils import (
    AuthenticationError,
    AuthUser,
    abort_unauthorized,
)

LOG = get_logger(__file__)

OAUTH_CALLBACK_PATH = "/oauth2callback"

def oauth_callback(self):
    LOG.debug("Handling Oauth callback...")

    if request.args.get("error"):
        # vulnerable
        return f"<h1>Error: {request.args.get('error')}</h1>"
    #vulnerable
    code = request.args.get("code")
    try:
        access_token = self._fetch_access_token(code)
        username, email = self._get_user_profile(access_token)
        with DBSession() as session:
            flask_login.login_user(
                AuthUser(self.login_user(username, email, session=session))
            )
    except AuthenticationError as e:
        LOG.error("Failed authenticate oauth user", e)
        abort_unauthorized()

    next_url = QuerybookSettings.PUBLIC_URL
    if "next" in flask_session:
        next_url = flask_session["next"]
        del flask_session["next"]

    return redirect(next_url)