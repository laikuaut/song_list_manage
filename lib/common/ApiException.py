# -*- coding: utf-8 -*-

class ApiException(Exception):
    def __init__(self, message):
        self._message = message

    def get_message(self):
        return self._message
