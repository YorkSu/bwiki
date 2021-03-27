# -*- coding: utf-8 -*-
"""API checktoken
======

SEE https://wiki.biligame.com/wiki/api.php?action=help&modules=checktoken
"""


from bwiki.api.base import BaseAPI
from bwiki.auth.token import Token


class Checktoken(BaseAPI):
    def __init__(self, token: Token, type: str, maxtokenage: int=None):
        super().__init__(token)
        params = {
            'action': 'checktoken',
            'type': type,
            'token': self.token,
        }
        if maxtokenage is not None:
            params['maxtokenage'] = maxtokenage
        self.set_params(params)

