# -*- coding: utf-8 -*-
"""API purge
======

SEE https://wiki.biligame.com/wiki/api.php?action=help&modules=purge
"""

from typing import Sequence

from bwiki.api.base import BaseAPI
from bwiki.api.utils import arg


class Purge(BaseAPI):
    def __init__(self,
                 forcelinkupdate: bool = None,
                 forcerecursivelinkupdate: bool = None,
                 _continue: int = None,
                 titles: Sequence[str] = None,
                 pageids: Sequence[int] = None,
                 revids: Sequence[int] = None,
                 generator: int = None,
                 redirects: bool = None,
                 converttitles: bool = None):
        super().__init__()
        self._use_token = False
        if not isinstance(titles, (list, tuple)):
            titles = [titles]
        self.set_params([
            {'action': 'purge'},
            arg.select_not_none('forcelinkupdate', forcelinkupdate),
            arg.select_not_none('forcerecursivelinkupdate', forcerecursivelinkupdate),
            arg.select_not_none('continue', _continue),
            arg.select_list('titles', titles),
            arg.select_list('pageids', pageids),
            arg.select_list('revids', revids),
            arg.select_not_none('generator', generator),
            arg.select_not_none('redirects', redirects),
            arg.select_not_none('converttitles', converttitles)
        ])
