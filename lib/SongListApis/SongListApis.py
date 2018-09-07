# -*- coding: utf-8 -*-

import re
import sys
from collections import OrderedDict
from .SongListEnvData import SongListEnvData

class SongInfo():

    ANALYZE_REGEX = re.compile(r'(?:【(.+?)】)?(?:【(.+?)】)?『(.+?)(?:／(.+?))?(?:（(.+?)「(.+?)」(.+?)）|（(.+?)）)?』(.+)')
    DATA_HEADERS = [
        'src_line',
        'cover_or_origin',
        'header',
        'title',
        'singer',
        'category1',
        'category2',
        'category3',
        'category4',
        'smileys',
    ]

    def __init__(self, src_line):
        self.__analyze_song_line(src_line.strip())

    def __analyze_song_line(self, src_line):
        self.data = OrderedDict()
        m = self.ANALYZE_REGEX.match(src_line)
        if m:
            self.data[self.DATA_HEADERS[0]] = src_line
            for i, value in enumerate(m.groups(), start=1):
                self.data[self.DATA_HEADERS[i]] = value

    def toTsvData(self):
        return '\t'.join([str(v) for v in self.data.values()])

    def toTsvHeader(self):
        return '\t'.join([str(s) for s in self.data.keys()])

    def isEmpty(self):
        if self.data:
            return False
        else:
            return True

class SongListApis():
    def __init__(self, config_file):
        self.__initialize(config_file)

    def __initialize(self, config_file):

        # 設定初期化
        self._env = SongListEnvData(config_file)
        self.common_section = self._env.common
        self.song_list_section = self._env.song_list

    def get_song_info_list(self):
        song_list = list()
        with self.song_list_section.open_all_file() as song_stream:
            for line in (song_stream):
                song_list.append(SongInfo(line))
        return song_list

    def get_song_list(self):
        with self.song_list_section.open_all_file() as song_stream, \
            self.common_section.open_output_file() as out:
            for line in (song_stream):
                song_info = SongInfo(line)
                if not song_info.isEmpty():
                    print(song_info.toTsvData(), file=out)

#    def get__song_list(self):
#        with open(self.config.all_song_file_path, 'r') as song_stream:
#            for line in (song_stream):
#                line = line.strip()
#                m = re.match(r'(?:【(.+?)】)?(?:【(.+?)】)?『(.+?)(?:／(.+?))?(?:（(.+?)「(.+?)」(.+?)）|（(.+?)）)?』(.+)', line)
#                result = list()
#                result.append(line)
#                if m:
#                    result.extend([str(s) for s in m.groups()])
#                    print('\t'.join(result))
#
