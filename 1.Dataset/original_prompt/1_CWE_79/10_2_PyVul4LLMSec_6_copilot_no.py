
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
    # co_fixed
    parts = request.path.split("/")
    if parts[1] == "canarydrop":
        if len(parts) == 3:
            canarydrop_id = parts[2]
            canarydrop = get_canarydrop(canarydrop_id)
            if canarydrop:
                template = env.get_template('canarydrop.html')
                return template.render(canarydrop=canarydrop)
            else:
                request.setResponseCode(404)
                return "Not Found"
        else:
            canarydrops = get_all_canary_sites()
            template = env.get_template('canarydrops.html')
            return template.render(canarydrops=canarydrops)
    elif parts[1] == "canarydropimg":
        canarydrop_id = parts[2]
        canarydrop = get_canarydrop(canarydrop_id)
        if canarydrop:
            request.setHeader('Content-Type', 'image/png')
            return canarydrop['img']
        else:
            request.setResponseCode(404)
            return "Not Found"
    elif parts[1] == "linkedin":
        if len(parts) == 3:
            linkedin_id = parts[2]
            linkedin = get_linkedin_account(linkedin_id)
            if linkedin:
                template = env.get_template('linkedin.html')
                return template.render(linkedin=linkedin)
            else:
                request.setResponseCode(404)
                return "Not Found"
        else:
            linkedins = get_all_canary_domains()
            template = env.get_template('linkedins.html')
            return template.render(linkedins=linkedins)
    elif parts[1] == "bitcoin":
        if len(parts) == 3:
            bitcoin_id = parts[2]
            bitcoin = get_bitcoin_account(bitcoin_id)
            if bitcoin:
                template = env.get_template('bitcoin.html')
                return template.render(bitcoin=bitcoin)
            else:
                request.setResponseCode(404)
                return "Not Found"
        else:
            bitcoins = get_all_canary_domains()
            template = env.get_template('bitcoins.html')
            return template.render(bitcoins=bitcoins)
    elif parts[1] == "imgur":
        if len(parts) == 3:
            imgur_id = parts[2]
            imgur = get_imgur_account(imgur_id)
            if imgur:
                template = env.get_template('imgur.html`
# co_fixed