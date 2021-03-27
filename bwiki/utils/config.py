# -*- coding: utf-8 -*-
"""Config Loader
======

Config Loader Class
"""


import json

from bwiki.utils import abcs
from bwiki.utils import path


class Config(abcs.Singleton):
    """Config Loader

    This is a Singleton Class
    """
    FLAGS = {
        'config_path': path.join(
            path.root,
            'config.json'
        )
    }
    _configs = dict()

    @staticmethod
    def load(filename) -> dict:
        if filename not in Config._configs:
            conf = dict()
            if path.exists(filename):
                try:
                    conf.update(json.load(open(
                        filename,
                        'r',
                        encoding="utf-8"
                    )))
                except Exception as e:
                    print(e)
            Config._configs[filename] = conf
        return Config._configs.get(filename, {})

    @staticmethod
    def root() -> dict:
        return Config.load(Config.FLAGS['config_path'])

    @staticmethod
    def set_config_path(config_path: str):
        Config.FLAGS['config_path'] = config_path
