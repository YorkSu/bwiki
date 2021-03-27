# -*- coding: utf-8 -*-
"""API upload
======

SEE https://wiki.biligame.com/wiki/api.php?action=help&modules=upload
"""

from typing import Sequence

from bwiki.api.base import BaseAPI
from bwiki.api.utils import arg


class Upload(BaseAPI):
    def __init__(self,
                 localfile: str,
                 filename: str,
                 comment: str = None,
                 tags: Sequence[str] = None,
                 text: str = None,
                 watchlist: str = None,
                 ignorewarnings: bool = None,
                 url: str = None,
                 filekey: str = None,
                 stash: bool = None,
                 filesize: int = None,
                 offset: int = None,
                 chunk: int = None,
                 _async: bool = None,
                 checkstatus: bool = None):
        super().__init__()
        self.set_params([
            {'action': 'upload'},
            arg.select_not_none('filename', filename),
            arg.select_not_none('comment', comment),
            arg.select_list('tags', tags),
            arg.select_not_none('text', text),
            arg.select_not_none('watchlist', watchlist),
            arg.select_not_none('ignorewarnings', ignorewarnings),
            arg.select_not_none('url', url),
            arg.select_not_none('filekey', filekey),
            arg.select_not_none('stash', stash),
            arg.select_not_none('filesize', filesize),
            arg.select_not_none('offset', offset),
            arg.select_not_none('chunk', chunk),
            arg.select_not_none('async', _async),
            arg.select_not_none('checkstatus', checkstatus),
        ])
        self.set_extra_params({
            'file': (filename, open(localfile, 'rb'))
        })
