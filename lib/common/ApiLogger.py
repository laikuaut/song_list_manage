# -*- coding: utf-8 -*-

import os
import logging
import logging.config

logging.config.fileConfig(os.path.join(os.path.dirname(__file__), '..', '..', 'resource', 'logging.conf'))
logger = logging.getLogger('songList')

def debugLog(message):
    logger.debug(message)

def infoLog(message):
    logger.info(message)

def warnLog(message):
    logger.warning(message)

def errorLog(message):
    logger.error(message)

def criticalLog(message):
    logger.critical(message)
