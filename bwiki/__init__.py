# -*- coding: utf-8 -*-
"""BWIKI
======


"""


import os as _os

ROOT = _os.path.dirname(_os.path.abspath(__file__))

del _os


from bwiki import api
from bwiki.auth.token import Token
from bwiki.utils.flags import FLAGS


def init(config_path: str=None):
    """Init Method"""
    if config_path is not None:
        FLAGS.config_path = config_path
    if FLAGS.token is None:
        FLAGS.token = Token()
    FLAGS.token.get_token()
