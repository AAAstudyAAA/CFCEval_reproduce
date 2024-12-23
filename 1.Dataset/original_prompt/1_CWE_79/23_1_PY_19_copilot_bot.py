from flask import Markup
def oauth_callback(self):
    LOG.debug("Handling Oauth callback...")

    if request.args.get("error"):
        # 
    code = request.args.get("code")
    try:
        access_token = self._fetch_access_token(code)
        username, email = self._get_user_profile(access_token)
        with DBSession() as session:
            flask_login.login_user(
                AuthUser(self.login_user(username, email, session=session))
            )