# -*- coding: utf-8 -*-
"""API checktoken
======

SEE https://wiki.biligame.com/wiki/api.php?action=help&modules=checktoken
"""

from bwiki.api.base import BaseAPI
from bwiki.api.utils import arg


class Checktoken(BaseAPI):
    def __init__(self,
                 type: str,
                 maxtokenage: int = None):
        super().__init__()
        self.set_params([
            {'action': 'checktoken'},
            {'type': type},
            arg.select_not_none('maxtokenage', maxtokenage)
        ])
