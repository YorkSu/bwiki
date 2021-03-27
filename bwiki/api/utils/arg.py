# -*- coding: utf-8 -*-
"""Arg

Functions that handle the arguments
"""

from typing import Any, Sequence


def _select_in_values(key: str, values: Sequence, default=None):
    def select_function(value):
        params = dict()
        if value not in values:
            value = default
        if value is not None:
            params[key] = value
        return params

    return select_function


def select_not_none(key: str, value: Any):
    params = dict()
    if value is not None:
        params[key] = value
    return params


def select_one(dictionary: dict):
    params = dict()
    for k, v in dictionary.items():
        if v is not None:
            params[k] = v
            return params
    raise TypeError("at least provide one of them: " + ','.join(dictionary.keys()))


def select_list(key, sequence: Sequence[str]):
    params = dict()
    if sequence is not None:
        params[key] = '|'.join(sequence)
    return params


select_watchlist = _select_in_values(
    'watchlist',
    [
        'watch',
        'unwatch',
        'preferences',
        'nochange'
    ],
    'preferences')
select_contentformat = _select_in_values(
    'contentformat',
    [
        'application/json',
        'text/plain',
        'text/x-wiki',
        'text/javascript',
        'text/css'
    ])
select_contentmodel = _select_in_values(
    'contentmodel',
    [
        'GadgetDefinition',
        'Scribunto',
        'flow-board',
        'wikitext',
        'javascript',
        'json',
        'css',
        'text',
        'smw/schema'
    ])
