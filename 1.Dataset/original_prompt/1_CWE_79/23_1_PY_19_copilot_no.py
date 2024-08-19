from flask import Markup
def oauth_callback(self):
    LOG.debug("Handling Oauth callback...")

    if request.args.get("error"):
        # co_fixed
        return redirect(url_for("index"))
 # co_fixed