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
import settings

unsafe_env = Environment(loader=FileSystemLoader('templates'),
                  extensions=['jinja2.ext.loopcontrols'])
env = Environment(loader=FileSystemLoader('templates'),
                  extensions=['jinja2.ext.loopcontrols'],
                  autoescape=True)

with open('/srv/templates/error_http.html', 'r') as f:
    twisted.web.resource.ErrorPage.template = f.read()

def render_POST(self, request):
    try:
        try:
            token = request.args.get('token', None)[0]
            auth  = request.args.get('auth',  None)[0]

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
        canarydrop['alert_sms_enabled']   = sms_enable_status
        canarydrop['web_image_enabled']   = web_image_status

        save_canarydrop(canarydrop=canarydrop)

        g_api_key = get_canary_google_api_key()
        template = unsafe_env.get_template('manage.html')
        return template.render(canarydrop=canarydrop, saved=True,
                                    settings=settings, API_KEY=g_api_key).encode('utf8')

    except Exception as e:
        import traceback
        log.error('Exception in manage.html: {e}, {stack}'.format(e=e, stack=traceback.format_exc()))
        # coge
        return NoResource().render(request)
# coge
