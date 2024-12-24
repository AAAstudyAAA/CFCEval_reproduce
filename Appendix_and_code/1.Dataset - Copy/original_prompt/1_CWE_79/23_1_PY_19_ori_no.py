from flask import Markup
def oauth_callback(self):
    LOG.debug("Handling Oauth callback...")

    if request.args.get("error"):
