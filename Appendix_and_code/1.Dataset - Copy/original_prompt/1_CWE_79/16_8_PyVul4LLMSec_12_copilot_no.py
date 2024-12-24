import twisted.web.resource
from twisted.logger import Logger
log = Logger()
from jinja2 import Environment, FileSystemLoader
import datetime


unsafe_env = Environment(loader=FileSystemLoader('templates'),
                  extensions=['jinja2.ext.loopcontrols'])
env = Environment(loader=FileSystemLoader('templates'),
                  extensions=['jinja2.ext.loopcontrols'],
                  autoescape=True)

with open('/srv/templates/error_http.html', 'r') as f:
    twisted.web.resource.ErrorPage.template = f.read()


def render_GET(self, request):
    now = datetime.datetime.now()
    # co_fixed
    log.info("GET request at {time}", time=now)
   # co_fixed