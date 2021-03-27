# -*- coding: utf-8 -*-
"""Base

Base API Class
"""


from bwiki.auth.token import Token


class BaseAPI:
    def __init__(self, token: Token, *args, **kwargs):
        self._params = dict()
        self._token = token
        self.session = token.session
        self.url = token.url
        self.cookies = token.cookies
        self.token = token.token
        self._params.update(token.params)

    def set_params(self, params: dict):
        self._params.update(params)

    def send(self, **kwargs):
        return self.session.post(
            url=self.url,
            cookies=self.cookies,
            data=self._params,
            **kwargs
        ).json()

