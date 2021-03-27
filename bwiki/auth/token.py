# -*- coding: utf-8 -*-
"""Token

Get Bwiki Token with Cookies
"""


import requests

from bwiki.auth.cookies import Cookies
from bwiki.utils import abcs
from bwiki.utils.config_loader import ConfigLoader


class Token(abcs.Singleton):
    """Token

    This is a Singleton Class
    """
    def __init__(self):
        self._conf = _conf = ConfigLoader.root()
        self._host = _conf['host']
        self._root_host = _conf['root_host']
        self._site = _conf['site']
        self._browser = _conf['browser']

        self.url = f"https://{self._host}/{self._site}/api.php"
        self.cookies = dict()
        self.token = ''
        self.session = requests.Session()

        # Init cookies
        if 'Cookies' in _conf:
            self.cookies = _conf['Cookies']
        else:
            self.get_cookies()

    def get_cookies(self):
        self.cookies.update(Cookies(
            self._host,
            '/' + self._site,
            self._browser
        ).get())
        self.cookies.update(Cookies(
            self._root_host,
            '/',
            self._browser
        ).get())
        return self.cookies

    def get_token(self):
        params = {
            'action': 'query',
            'meta': 'tokens',
            'format': 'json'
        }
        resp = self.session.get(
            url=self.url,
            cookies=self.cookies,
            params=params
        ).json()
        self.token = resp['query']['tokens']['csrftoken']
        return self.token

    @property
    def params(self):
        return {
            'format': 'json',
            'utf8': 1,
            'token': self.token
        }
