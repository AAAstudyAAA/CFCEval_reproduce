from flask import Markup
def oauth_callback(self):
    LOG.debug("Handling Oauth callback...")

    if request.args.get("error"):
        # the following code is for fixing the vulnerability CWE-79 (Cross-site Scripting)
        return Markup(f"Error: {request.args['error']}")