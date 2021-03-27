# -*- coding: utf-8 -*-
"""API parse
======

SEE https://wiki.biligame.com/wiki/api.php?action=help&modules=parse
"""

from typing import Sequence

from bwiki.api.base import BaseAPI
from bwiki.api.utils import arg
from bwiki.auth.token import Token


class Parse(BaseAPI):
    def __init__(self,
                 title: str = None,
                 text: str = None,
                 revid: int = None,
                 summary: str = None,
                 page: str = None,
                 pageid: int = None,
                 redirects: bool = None,
                 oldid: int = None,
                 prop: Sequence[str] = None,
                 wrapoutputclass: str = None,
                 pst: bool = None,
                 onlypst: bool = None,
                 section: str = None,
                 sectiontitle: str = None,
                 disablelimitreport: bool = None,
                 disableeditsection: bool = None,
                 disablestylededuplication: bool = None,
                 preview: bool = None,
                 sectionpreview: bool = None,
                 disabletoc: bool = None,
                 useskin: str = None,
                 contentformat: str = None,
                 contentmodel: str = None,
                 mobileformat: bool = None,
                 noimages: bool = None,
                 mainpage: bool = None):
        super().__init__()
        self._use_token = False
        self.set_params([
            {'action': 'parse'},
            arg.select_not_none('title', title),
            arg.select_not_none('text', text),
            arg.select_not_none('revid', revid),
            arg.select_not_none('summary', summary),
            arg.select_not_none('page', page),
            arg.select_not_none('pageid', pageid),
            arg.select_not_none('redirects', redirects),
            arg.select_not_none('oldid', oldid),
            arg.select_list('prop', prop),
            arg.select_not_none('wrapoutputclass', wrapoutputclass),
            arg.select_not_none('pst', pst),
            arg.select_not_none('onlypst', onlypst),
            arg.select_not_none('section', section),
            arg.select_not_none('sectiontitle', sectiontitle),
            arg.select_not_none('disablelimitreport', disablelimitreport),
            arg.select_not_none('disableeditsection', disableeditsection),
            arg.select_not_none('disablestylededuplication', disablestylededuplication),
            arg.select_not_none('preview', preview),
            arg.select_not_none('sectionpreview', sectionpreview),
            arg.select_not_none('disabletoc', disabletoc),
            arg.select_not_none('useskin', useskin),
            arg.select_contentformat(contentformat),
            arg.select_contentmodel(contentformat),
            arg.select_not_none('mobileformat', mobileformat),
            arg.select_not_none('noimages', noimages),
            arg.select_not_none('mainpage', mainpage),
        ])
