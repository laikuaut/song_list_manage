# -*- coding: utf-8 -*-

import os
import sys
import argparse
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lib'))

from SongListApis.SongListApis import SongListApis
from common import ApiLogger

def args_parser():
    parser = argparse.ArgumentParser('')
    parser.add_argument('config', type=str, help="設定ファイル")
    return parser.parse_args()

def main():
    ApiLogger.infoLog('start')
    args = args_parser()
    SongListApis(args.config).get_song_list()
    ApiLogger.infoLog('end')

if __name__ == "__main__":
    main()
