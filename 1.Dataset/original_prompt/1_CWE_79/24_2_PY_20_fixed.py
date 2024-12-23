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
        # fixed
        return f"<h1>Error: {Markup.escape(request.args.get('error'))}</h1>"
    # fixed
    code = request.args.get("code")
    try:
        access_token = self._fetch_access_token(code)
        username, email, fullname = self._get_user_profile(access_token)
        with DBSession() as session:
            flask_login.login_user(
                AuthUser(
                    self.login_user(username, email, fullname, session=session)
                )
            )
    except AuthenticationError as e:
        LOG.error("Failed authenticate oauth user", e)
        abort_unauthorized()

    next_url = QuerybookSettings.PUBLIC_URL
    if "next" in flask_session:
        next_url = flask_session["next"]
        del flask_session["next"]

    return redirect(next_url)