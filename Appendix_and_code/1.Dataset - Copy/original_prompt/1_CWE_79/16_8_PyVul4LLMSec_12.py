import twisted.web.resource

from twisted.logger import Logger
log = Logger()
from jinja2 import Environment, FileSystemLoader

import datetime

env = Environment(loader=FileSystemLoader('templates'),
                  extensions=['jinja2.ext.loopcontrols'])

with open('/srv/templates/error_http.html', 'r') as f:
    twisted.web.resource.ErrorPage.template = f.read()
def render_GET(self, request):
    now = datetime.datetime.now()
    #vulnerable
    template = env.get_template('legal.html')
    #vulnerable
    return template.render(now=now).encode('utf8')