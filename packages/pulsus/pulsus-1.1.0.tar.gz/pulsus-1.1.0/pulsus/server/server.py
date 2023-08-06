import configparser
import json
import logging
import os
from datetime import datetime

from gevent import monkey
from gevent.queue import Empty
from werkzeug.wrappers import Request, Response

from ..services.apns import APNSService
from ..services.base import BaseNotification
from ..services.gcm import GCMService


monkey.patch_all()

logger = logging.getLogger(__name__)


class APIServer(object):

    def __init__(self, *args, **kwargs):
        self.apns = kwargs.pop('apns')
        self.apns_sandbox = kwargs.pop('apns_sandbox')
        self.gcm = kwargs.pop('gcm')

    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        response = self.dispatch_request(request)
        return response(environ, start_response)

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)

    def dispatch_request(self, request):
        if request.path == '/api/push/' and request.method == 'POST':
            notifications = json.loads(request.data)
            self.push_notifications(notifications)
            resp = Response('')
            resp.status_code = 201
        elif request.path == '/api/feedback/' and request.method == 'POST':
            resp = self.handle_feedback(request)
        else:
            resp = Response('')
            resp.status_code = 400
        return resp

    def handle_feedback(self, request):
        feedback = self._handle_feedback('apns', self.apns, False)
        feedback.extend(self._handle_feedback('apns', self.apns_sandbox, True))
        feedback.extend(self._handle_feedback('gcm', self.gcm, False))
        resp = Response(json.dumps(feedback))
        return resp

    def _handle_feedback(self, type, service, sandbox):
        feedback = []
        try:
            while True:
                epoch, token = service.get_feedback(block=False)
                dt = datetime.utcfromtimestamp(epoch)
                feedback.append(dict(type=type,
                                     sandbox=sandbox,
                                     marked_inactive_at=dt.isoformat(),
                                     token=token))
        except Empty:
            pass
        return feedback

    def push_notifications(self, notifications):
        for data in notifications:
            notification = BaseNotification.deserialize(data)
            if notification.service_type == 'apns':
                if notification.sandbox:
                    logger.debug("Sending APNS notification (to sandbox)")
                    self.apns_sandbox.queue_notification(notification)
                else:
                    logger.debug("Sending APNS notification")
                    self.apns.queue_notification(notification)
            elif notification.service_type == 'gcm':
                logger.debug("Sending GCM notification")
                self.gcm.queue_notification(notification)
            else:
                logger.error("Unknown push type")


def read_config(config_dir):
    config = configparser.ConfigParser()
    config.read([os.path.join(config_dir, 'pulsus.conf')])
    return config


def setup(config):
    # Apple (Production)
    apns_server = APNSService(
        sandbox=False,
        certfile=config.get('apns', 'cert_file_pem'))
    apns_server.start()

    # Apple (Sandbox)
    apns_sandbox_server = APNSService(
        sandbox=True,
        certfile=config.get('apns:sandbox', 'cert_file_pem'))
    apns_sandbox_server.start()

    # GCM
    gcm_server = GCMService(config.get('gcm', 'api_key'))
    gcm_server.start()

    # API
    api_server = APIServer(apns=apns_server,
                           apns_sandbox=apns_sandbox_server,
                           gcm=gcm_server)
    return api_server
