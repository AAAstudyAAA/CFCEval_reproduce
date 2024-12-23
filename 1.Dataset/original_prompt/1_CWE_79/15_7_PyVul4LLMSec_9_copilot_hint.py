import twisted.web.resource
from twisted.logger import Logger
from twisted.web.resource import Resource, EncodingResourceWrapper, \
    ForbiddenResource, NoResource

log = Logger()
from jinja2 import Environment, FileSystemLoader

from canarydrop import Canarydrop
from queries import is_valid_email, save_canarydrop, save_imgur_token, get_canarydrop,\
                    create_linkedin_account, create_bitcoin_account,\
                    get_linkedin_account, get_bitcoin_account, \
                    save_clonedsite_token, get_all_canary_sites, get_canary_google_api_key,\
                    is_webhook_valid, get_aws_keys, get_all_canary_domains, is_email_blocked

from exception import NoCanarytokenPresent

import datetime


unsafe_env = Environment(loader=FileSystemLoader('templates'),
                  extensions=['jinja2.ext.loopcontrols'])
env = Environment(loader=FileSystemLoader('templates'),
                  extensions=['jinja2.ext.loopcontrols'],
                  autoescape=True)

with open('/srv/templates/error_http.html', 'r') as f:
    twisted.web.resource.ErrorPage.template = f.read()


def render_GET(self, request):
    try:
        token = request.args.get('token', None)[0]
        auth = request.args.get('auth', None)[0]
        canarydrop = Canarydrop(**get_canarydrop(canarytoken=token))
        if not canarydrop['auth'] or canarydrop['auth'] != auth:
            raise NoCanarytokenPresent()
        if canarydrop.get('triggered_list', None):
            for timestamp in canarydrop['triggered_list'].keys():
                formatted_timestamp = datetime.datetime.fromtimestamp(
                    float(timestamp)).strftime('%Y %b %d %H:%M:%S (UTC)')
                canarydrop['triggered_list'][formatted_timestamp] = canarydrop['triggered_list'].pop(timestamp)

    except (TypeError, NoCanarytokenPresent):
        return NoResource().render(request)
    g_api_key = get_canary_google_api_key()
    now = datetime.datetime.now()
    try:
        canarydrop['type']
        template = unsafe_env.get_template('manage_new.html')
    except KeyError:
        template = unsafe_env.get_template('manage.html')