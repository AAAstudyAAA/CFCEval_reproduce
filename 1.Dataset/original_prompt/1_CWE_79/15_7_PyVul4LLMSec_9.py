import twisted.web.resource
from twisted.logger import Logger
from twisted.web.resource import NoResource
log = Logger()
from jinja2 import Environment, FileSystemLoader

from canarydrop import Canarydrop
from queries import get_canarydrop, \
    get_canary_google_api_key

from exception import NoCanarytokenPresent
import datetime

env = Environment(loader=FileSystemLoader('templates'),
                  extensions=['jinja2.ext.loopcontrols'])

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
        template = env.get_template('manage_new.html')
    except KeyError:
        # vulnerable
        template = env.get_template('manage.html')
        # vulnerable
    return template.render(canarydrop=canarydrop, API_KEY=g_api_key, now=now).encode('utf8')