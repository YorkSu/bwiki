# -*- coding: utf-8 -*-
"""API expandtemplates
======

SEE https://wiki.biligame.com/wiki/api.php?action=help&modules=expandtemplates
"""

from typing import Sequence

from bwiki.api.base import BaseAPI
from bwiki.api.utils import arg


class Expandtemplates(BaseAPI):
    def __init__(self,
                 title: str = None,
                 text: str = None,
                 revid: int = None,
                 prop: Sequence[str] = None,
                 includecomments: bool = None):
        super().__init__()
        self._use_token = False
        self.set_params([
            {'action': 'expandtemplates'},
            arg.select_not_none('title', title),
            arg.select_not_none('text', text),
            arg.select_not_none('revid', revid),
            arg.select_list('prop', prop),
            arg.select_not_none('includecomments', includecomments)
        ])
