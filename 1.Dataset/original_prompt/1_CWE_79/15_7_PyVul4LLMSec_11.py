import twisted.web.resource
from twisted.logger import Logger
from twisted.web.resource import NoResource

log = Logger()
from jinja2 import Environment, FileSystemLoader

from canarydrop import Canarydrop
from queries import save_canarydrop, get_canarydrop, \
    get_canary_google_api_key

from exception import NoCanarytokenPresent
import settings

env = Environment(loader=FileSystemLoader('templates'),
                  extensions=['jinja2.ext.loopcontrols'])

with open('/srv/templates/error_http.html', 'r') as f:
    twisted.web.resource.ErrorPage.template = f.read()

def render_POST(self, request):
    try:
        try:
            token = request.args.get('token', None)[0]
            auth = request.args.get('auth', None)[0]

            canarydrop = Canarydrop(**get_canarydrop(canarytoken=token))
            if not canarydrop['auth'] or canarydrop['auth'] != auth:
                raise NoCanarytokenPresent()

        except (IndexError, TypeError, NoCanarytokenPresent):
            return NoResource().render(request)

        try:
            email_enable_status = request.args.get('email_enable', None)[0] == "on"
        except (TypeError, IndexError):
            email_enable_status = False

        try:
            webhook_enable_status = request.args.get('webhook_enable', None)[0] == "on"
        except (TypeError, IndexError):
            webhook_enable_status = False

        try:
            sms_enable_status = request.args.get('sms_enable', None)[0] == "on"
        except (TypeError, IndexError):
            sms_enable_status = False

        try:
            web_image_status = request.args.get('web_image_enable', None)[0] == "on"
        except (TypeError, IndexError):
            web_image_status = False

        try:
            token_fmt = request.args.get('fmt', None)[0]
        except (TypeError, IndexError):
            token_fmt = ''

        canarydrop['alert_email_enabled'] = email_enable_status
        canarydrop['alert_webhook_enabled'] = webhook_enable_status
        canarydrop['alert_sms_enabled'] = sms_enable_status
        canarydrop['web_image_enabled'] = web_image_status

        save_canarydrop(canarydrop=canarydrop)

        g_api_key = get_canary_google_api_key()
        template = env.get_template('manage.html')
        return template.render(canarydrop=canarydrop, saved=True,
                               settings=settings, API_KEY=g_api_key).encode('utf8')

    except Exception as e:
        import traceback
        log.error('Exception in manage.html: {e}, {stack}'.format(e=e, stack=traceback.format_exc()))
        # vulnerable
        template = env.get_template('manage.html')
        # vulnerable
        return template.render(canarydrop=canarydrop, error=e,
                               settings=settings).encode('utf8')

