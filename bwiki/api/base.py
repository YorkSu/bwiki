# -*- coding: utf-8 -*-
"""Base

Base API Class
"""

from typing import Sequence

from bwiki.auth.token import Token


class BaseAPI:
    def __init__(self, *args, **kwargs):
        self._params = dict()
        self._extra_params = dict()
        self._token = Token()
        self._use_token = True

        self.session = self._token.session
        self.url = self._token.url
        self.cookies = self._token.cookies
        self.token = self._token.token
        self._params.update(self._token.params)

    def set_params(self, params: Sequence[dict]):
        if not isinstance(params, (list, tuple)):
            params = [params]
        for p in params:
            self._params.update(p)

    def set_extra_params(self, kwargs: dict):
        self._extra_params.update(kwargs)

    def send(self):
        if not self._use_token:
            self._params.pop('token')
        return self.session.post(
            url=self.url,
            cookies=self.cookies,
            data=self._params,
            **self._extra_params
        ).json()

