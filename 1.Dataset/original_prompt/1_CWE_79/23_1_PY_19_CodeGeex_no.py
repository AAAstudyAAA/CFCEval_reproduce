from flask import Markup
def oauth_callback(self):
    LOG.debug("Handling Oauth callback...")

    if request.args.get("error"):
        # coge
        LOG.error("Error in Oauth callback: %s", request.args["error"])
        return redirect(url_for("index"))
# coge