# -*- coding: utf-8 -*-
"""Config Loader
======

Config Loader Class
"""


import json

from bwiki.utils import abcs
from bwiki.utils import path
from bwiki.utils.flags import FLAGS


class Config(abcs.Singleton):
    """Config Loader

    This is a Singleton Class
    """
    @staticmethod
    def load(filename) -> dict:
        if filename not in FLAGS.configs:
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
            FLAGS.configs[filename] = conf
        return FLAGS.configs.get(filename, {})

    @staticmethod
    def root() -> dict:
        return Config.load(FLAGS.config_path)
