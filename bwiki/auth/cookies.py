# -*- coding: utf-8 -*-
"""Cookies

Get Cookies from the given browser
"""
import base64
import json
import os
import sqlite3

from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from win32crypt import CryptUnprotectData


_LOCALAPPDATA = os.environ['LOCALAPPDATA']
EDGE_LOCAL_STATE = _LOCALAPPDATA + r'\Microsoft\Edge\User Data\Local State'
EDGE_COOKIE_PATH = _LOCALAPPDATA + r'\Microsoft\Edge\User Data\Default\Cookies'
CHROME_LOCAL_STATE = _LOCALAPPDATA + r'\Google\Chrome\User Data\Local State'
CHROME_COOKIE_PATH = _LOCALAPPDATA + r'\Google\Chrome\User Data\Default\Cookies'


class Cookies:
    def __init__(self, host: str, path: str, browser: str):
        self._host = host
        self._path = path
        self._browser = browser
        self._local_state = ''
        self._cookie_path = ''
        if self._browser.lower() == 'edge':
            self._local_state = EDGE_LOCAL_STATE
            self._cookie_path = EDGE_COOKIE_PATH
        elif self._browser.lower() == 'chrome':
            self._local_state = CHROME_LOCAL_STATE
            self._cookie_path = CHROME_COOKIE_PATH

    def _get_string(self, local_state):
        with open(local_state, 'r', encoding='utf-8') as f:
            return json.load(f)['os_crypt']['encrypted_key']

    def _pull_the_key(self, base64_encrypted_key):
        encrypted_key_with_header = base64.b64decode(base64_encrypted_key)
        encrypted_key = encrypted_key_with_header[5:]
        key = CryptUnprotectData(encrypted_key, None, None, None, 0)[1]
        return key

    def _decrypt_string(self, key, data):
        nonce, cipherbytes = data[3:15], data[15:]
        aesgcm = AESGCM(key)
        plainbytes = aesgcm.decrypt(nonce, cipherbytes, None)
        plaintext = plainbytes.decode('utf-8')
        return plaintext

    def get(self):
        sql = f"select host_key,name,encrypted_value from cookies where host_key='{self._host}'"
        if self._path:
            sql += f" and path='{self._path}'"
        with sqlite3.connect(self._cookie_path) as conn:
            cu = conn.cursor()
            res = cu.execute(sql).fetchall()
            cu.close()
            cookies = {}
            key = self._pull_the_key(self._get_string(self._local_state))
            for host_key, name, encrypted_value in res:
                if encrypted_value[0:3] == b'v10':
                    cookies[name] = self._decrypt_string(key, encrypted_value)
                else:
                    cookies[name] = CryptUnprotectData(encrypted_value)[1].decode()
            return cookies
