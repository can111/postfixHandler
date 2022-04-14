from aiohttp import web
from aiohttp.web_request import Request
import logging
from systemd.journal import JournalHandler


class QuarantineHandler(web.View):
    def __init__(self, request: Request):
        super().__init__(request)

class NotificationHandler(web.View):


class DatabaseHandler(web.View):


class ConnectionHandler(web.View):


class TransportHandler(web.View):


class MasqHandler(web.View):


class SmtpHandler(web.View):


class ProxyHandler(web.View):


class AliasHandler(web.View):


web_api_init = {
    'route': [{
        'uri': '/postfix/alias',
        'handler': AliasHandler,
        'label': 'Alias'
    }, {
        'uri': '/postfix/proxy',
        'handler': ProxyHandler,
        'label': 'Proxy'
    }, {
        'uri': '/postfix/smtp',
        'handler': SmtpHandler,
        'label': 'Smtp'
    }, {
        'uri': '/postfix/masq',
        'handler': MasqHandler,
        'label': 'masq'
    }, {
        'uri': '/postfix/transport',
        'handler': TransportHandler,
        'label': 'Transport'
    }, {
        'uri': '/postfix/connect',
        'handler': ConnectionHandler,
        'label': 'Connect'
    }, {
        'uri': '/postfix/database',
        'handler': DatabaseHandler,
        'label': 'Database'
    }, {
        'uri': '/postfix/notification',
        'handler': NotificationHandler,
        'label': 'Notification'
    }, {
        'uri': '/postfix/quarantine',
        'handler': QuarantineHandler,
        'label': 'Quarantine'
    }]
}