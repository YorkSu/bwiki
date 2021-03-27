# -*- coding: utf-8 -*-
"""Abstract Classes
======
"""


import abc
import threading


class SingletonMetaclass(type):
    """Metaclass for defining Singleton Classes

    Use this metaclass to create a Singleton Class.

    Usage:
    ```python
    class Singleton(metaclass=SingletonMetaclass): ...
    ```
    """
    __instance_lock = threading.RLock()
    __instance = None
    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            with cls.__instance_lock:
                if cls.__instance is None:
                    cls.__instance = super(SingletonMetaclass, cls).\
                        __call__(*args, **kwargs)
        return cls.__instance


class AbstractSingletonMetaclass(abc.ABCMeta, SingletonMetaclass):
    """Abstract Singleton Metaclass

    Use this metaclass to create a Abstract Singleton Class.
    """


class Singleton(metaclass=SingletonMetaclass):
    """Parent Class for a Singleton

    Inherit this class to Create a Singleton Class

    SubClasses SHALL NOTE `This is a Singleton Class`
    """
    _lock = threading.RLock()


class AbstractSingleton(metaclass=AbstractSingletonMetaclass):
    """Abstract Singleton Class

    Inherit this class to Create a Abstract Singleton Class

    SubClasses SHALL NOTE `This is an Abstract Singleton Class`
    """
    _lock = threading.RLock()
