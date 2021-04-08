# -*- coding: utf-8 -*-
"""Flags
======

Global Parameters Manager
"""


from bwiki.utils import path
from bwiki.utils.abcs import Singleton


class Flags(Singleton):
    """This is a Singleton Class"""
    def __init__(self):
        self.config_path = path.join(
            path.root,
            'config.json'
        )
        self.token = None
        self.configs = dict()

    def __getattribute__(self, key, default=None):
        try:
            return super().__getattribute__(key)
        except AttributeError:
            return default

    def get(self, key, default=None):
        """Get the value of an argument

          If not found, return default
        """
        return self.__getattribute__(key, default)

    def set(self, key, value):
        """Set the value of an argument"""
        self.__setattr__(key, value)

    @staticmethod
    def set_config_path(config_path: str):
        """Set Default Config Path"""
        self.config_path = config_path


FLAGS = Flags()
