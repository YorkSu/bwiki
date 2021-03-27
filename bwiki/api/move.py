# -*- coding: utf-8 -*-
"""API move
======

SEE https://wiki.biligame.com/wiki/api.php?action=help&modules=move
"""

from typing import Sequence

from bwiki.api.base import BaseAPI
from bwiki.api.utils import arg
from bwiki.auth.token import Token


class Move(BaseAPI):
    def __init__(self,
                 fm: str = None,
                 fromid: int = None,
                 to: str = None,
                 reason: str = None,
                 movetalk: bool = None,
                 movesubpages: bool = None,
                 noredirect: bool = None,
                 watchlist: str = None,
                 ignorewarnings: bool = None,
                 tags: Sequence[str] = None):
        super().__init__()
        self.set_params([
            {'action': 'move'},
            arg.select_one({'from': fm, 'fromid': fromid}),
            arg.select_not_none('to', to),
            arg.select_not_none('reason', reason),
            arg.select_not_none('movetalk', movetalk),
            arg.select_not_none('movesubpages', movesubpages),
            arg.select_not_none('noredirect', noredirect),
            arg.select_watchlist(watchlist),
            arg.select_not_none('ignorewarnings', ignorewarnings),
            arg.select_list('tags', tags),
        ])
