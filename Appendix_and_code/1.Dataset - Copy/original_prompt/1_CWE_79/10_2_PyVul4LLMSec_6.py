import twisted.web.resource
from jinja2 import Environment, FileSystemLoader
from queries import get_all_canary_sites
import settings
import datetime

env = Environment(loader=FileSystemLoader('templates'),
                  extensions=['jinja2.ext.loopcontrols'])

with open('/srv/templates/error_http.html', 'r') as f:
    twisted.web.resource.ErrorPage.template = f.read()

def render_GET(self, request):
    #vulnerable
    template = env.get_template('generate_new.html')
    #vulnerable
    sites_len = len(get_all_canary_sites())
    now = datetime.datetime.now()
    return template.render(settings=settings, sites_len=sites_len, now=now).encode('utf8')
