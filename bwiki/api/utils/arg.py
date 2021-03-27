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


def select_title_pageid(title: str, pageid: int):
    params = dict()
    if title is not None:
        params['title'] = title
    elif pageid is not None:
        params['pageid'] = pageid
    else:
        raise TypeError("title and pageid provide at least one of them")
    return params


def select_tags(tags: Sequence[str]):
    params = dict()
    if tags is not None:
        params['tags'] = '|'.join(tags)
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
