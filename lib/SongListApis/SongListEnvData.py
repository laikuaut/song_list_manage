# -*- coding: utf-8 -*-

import toml

class BaseSection():

    # セクション名
    # 継承元クラスにて値を入れること
    SECTION_NAME = ""

    def __init__(self, env):
        """
        コンストラクタ

        @param env 環境データオブジェクト
        """
        self.env = env
        self.section = env.config[self.SECTION_NAME]

class CommonSestion(BaseSection):

    SECTION_NAME = 'common'

    def __init__(self, env):
        """
        コンストラクタ

        @param env 環境データオブジェクト
        """
        super(CommonSestion, self).__init__(env)

    @property
    def input_encode(self):
        """
        @return 入力エンコード（必須）
        """
        return self.section['input_encode']

    @property
    def output_encode(self):
        """
        @return 出力エンコード（必須）
        """
        return self.section['output_encode']

    @property
    def output_file(self):
        """
        @return 出力ファイルパス（任意: 省略時はNone）
        """
        return self.section.get('output_file')

    def open_output_file(self):
        """
        出力ファイルオープン（上書きモード）
        with文での利用を想定

        @return 出力ファイルのストリーム(省略時はNone)
        """
        if self.output_file:
            return open(self.output_file, 'w',
                encoding=self.output_encode)
        else:
            return None

class SongListSection(BaseSection):

    SECTION_NAME = 'song_list'

    def __init__(self, env):
        """
        コンストラクタ

        @param env 環境データオブジェクト
        """
        super(SongListSection, self).__init__(env)

    @property
    def all_file_path(self):
        """
        @return 曲リストファイルパス（任意: 省略時はNone）
        """
        return self.section.get('all_file_path')

    def open_all_file(self):
        """
        曲リストファイルオープン（読み込みモード）
        with文での利用を想定

        @return 曲リストのストリーム(省略時はNone)
        """
        return open(self.all_file_path, 'r',
            encoding=self.env.common.input_encode)

class SongListEnvData():
    def __init__(self, config_path):
        self._config_path = config_path
        self._config_load()

    def _config_load(self):
        self.config = toml.load(self._config_path)

    @property
    def common(self):
        return CommonSestion(self)

    @property
    def song_list(self):
        return SongListSection(self)
