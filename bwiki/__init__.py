# -*- coding: utf-8 -*-
"""BWIKI
======


"""


import os as _os

ROOT = _os.path.dirname(_os.path.abspath(__file__))

del _os


from bwiki import api
from bwiki.auth.token import Token
from bwiki.utils.config import Config


FLAGS = Config.FLAGS
set_config_path = Config.set_config_path
