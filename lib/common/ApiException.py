# -*- coding: utf-8 -*-

class ApiException(Exception):
    """
    API例外クラス
    """
    
    def __init__(self, message):
        self._message = message

    def get_message(self):
        return self._message
