# -*- coding: utf-8 -*-
"""Config Loader
======

Config Loader Class
"""


import json

from bwiki.utils import abcs
from bwiki.utils import path


class ConfigLoader(abcs.Singleton):
    """Config Loader

    This is a Singleton Class
    """
    _configs = dict()

    @staticmethod
    def load(filename) -> dict:
        if filename not in ConfigLoader._configs:
            conf = dict()
            if path.exists(filename):
                try:
                    conf.update(json.load(open(
                        filename,
                        'r',
                        encoding="urf-8"
                    )))
                except Exception as e:
                    print(e)
        return ConfigLoader._configs[filename]

    @staticmethod
    def root() -> dict:
        filename = path.join(
            path.root,
            'config.json'
        )
        return ConfigLoader.load(filename)
