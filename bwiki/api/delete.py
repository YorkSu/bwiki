# -*- coding: utf-8 -*-
"""API delete
======

SEE https://wiki.biligame.com/wiki/api.php?action=help&modules=delete
"""

from typing import Sequence

from bwiki.api.base import BaseAPI
from bwiki.api.utils import arg
from bwiki.auth.token import Token


class Delete(BaseAPI):
    def __init__(self,
                 title: str = None,
                 pageid: int = None,
                 reason: str = None,
                 tags: Sequence[str] = None,
                 watchlist: str = None,
                 oldimage: str = None):
        super().__init__()
        self.set_params([
            {'action': 'delete'},
            arg.select_one({'title': title, 'pageid': pageid}),
            arg.select_not_none('reason', reason),
            arg.select_list('tags', tags),
            arg.select_watchlist(watchlist),
            arg.select_not_none('oldimage', oldimage)
        ])
