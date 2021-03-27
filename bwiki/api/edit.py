# -*- coding: utf-8 -*-
"""API edit
======

SEE https://wiki.biligame.com/wiki/api.php?action=help&modules=edit
"""

from typing import Sequence

from bwiki.api.base import BaseAPI
from bwiki.api.utils import arg
from bwiki.auth.token import Token


class Edit(BaseAPI):
    def __init__(self,
                 title: str = None,
                 pageid: int = None,
                 section: str = None,
                 sectiontitle: str = None,
                 text: str = None,
                 summary: str = None,
                 tags: Sequence[str] = None,
                 minor: bool = None,
                 notminor: bool = None,
                 bot: bool = None,
                 basetimestamp: str = None,
                 starttimestamp: str = None,
                 recreate: bool = None,
                 createonly: bool = None,
                 nocreate: bool = None,
                 watchlist: str = None,
                 md5: str = None,
                 prependtext: str = None,
                 appendtext: str = None,
                 undo: int = None,
                 undoafter: int = None,
                 redirect: bool = None,
                 contentformat: str = None,
                 contentmodel: str = None,
                 captchaword: str = None,
                 captchaid: str = None):
        super().__init__()
        self.set_params([
            {'action': 'edit'},
            arg.select_one({'title': title, 'pageid': pageid}),
            arg.select_not_none('section', section),
            arg.select_not_none('sectiontitle', sectiontitle),
            arg.select_not_none('text', text),
            arg.select_not_none('summary', summary),
            arg.select_list('tags', tags),
            arg.select_not_none('minor', minor),
            arg.select_not_none('notminor', notminor),
            arg.select_not_none('bot', bot),
            arg.select_not_none('basetimestamp', basetimestamp),
            arg.select_not_none('starttimestamp', starttimestamp),
            arg.select_not_none('createonly', createonly),
            arg.select_not_none('nocreate', nocreate),
            arg.select_watchlist(watchlist),
            arg.select_not_none('md5', md5),
            arg.select_not_none('prependtext', prependtext),
            arg.select_not_none('appendtext', appendtext),
            arg.select_not_none('undo', undo),
            arg.select_not_none('redirect', redirect),
            arg.select_contentformat(contentformat),
            arg.select_contentmodel(contentformat),
            arg.select_not_none('captchaword', captchaword),
            arg.select_not_none('captchaid', captchaid)
        ])

