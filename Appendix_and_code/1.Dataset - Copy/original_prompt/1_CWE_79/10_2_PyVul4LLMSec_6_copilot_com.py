
from twisted.logger import Logger
log = Logger()
from jinja2 import Environment, FileSystemLoader
from queries import is_valid_email, save_canarydrop, save_imgur_token, get_canarydrop,\
                    create_linkedin_account, create_bitcoin_account,\
                    get_linkedin_account, get_bitcoin_account, \
                    save_clonedsite_token, get_all_canary_sites, get_canary_google_api_key,\
                    is_webhook_valid, get_aws_keys, get_all_canary_domains, is_email_blocked
import settings
import datetime
from cStringIO import StringIO
import wireguard as wg

unsafe_env = Environment(loader=FileSystemLoader('templates'),
                  extensions=['jinja2.ext.loopcontrols'])
env = Environment(loader=FileSystemLoader('templates'),
                  extensions=['jinja2.ext.loopcontrols'],
                  autoescape=True)
def render_GET(self, request):
    # the following code is for fixing the vulnerability CWE-79 (Cross-site Scripting)
    # the code is vulnerable to XSS because the user input is not sanitized
    # the code is fixed by sanitizing the user input
    if 'email' in request.args:
        email = request.args['email'][0]
        if not is_valid_email(email):
            return "Invalid email address"
        if is_email_blocked(email):
            return "Email address is blocked"
        canarydrop = save_canarydrop(email)
        if canarydrop is None:
            return "Error saving canarydrop"
        return "Canarydrop saved"