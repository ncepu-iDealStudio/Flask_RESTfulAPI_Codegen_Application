#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:loggings.py.py
# author:Nathan
# datetime:2021/8/22 16:28
# software: PyCharm

"""
    Operation log record
"""

import sys

from loguru import logger


class Loggings(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(Loggings, cls).__new__(cls, *args, **kwargs)

        return cls.__instance

    def info(self, location, msg, session_id=None, ip=None):
        Loggings.log_filter(location, session_id, ip)
        return logger.info(msg)

    def debug(self, location, msg, session_id=None, ip=None):
        Loggings.log_filter(location, session_id, ip)
        return logger.debug(msg)

    def warning(self, location, msg, session_id=None, ip=None):
        Loggings.log_filter(location, session_id, ip)
        return logger.warning(msg)

    def error(self, location, msg, session_id=None, ip=None):
        Loggings.log_filter(location, session_id, ip, wrong=True)
        return logger.error(msg)

    def exception(self, location, msg, session_id=None, ip=None):
        Loggings.log_filter(location, session_id, ip, wrong=True)
        return logger.exception(msg)

    @staticmethod
    def log_filter(location, session_id=None, ip=None, wrong=False):
        if ip and session_id:
            if wrong:
                log_path = "logs/log_error_info/codegen_log_{session_id}.log".format(session_id=session_id)
            else:
                log_path = "logs/log_user_info/codegen_log_{user_ip}_{session_id}.log".format(
                    user_ip=ip, session_id=session_id)
        elif session_id:
            log_path = "logs/codegen_log_{session_id}.log".format(session_id=session_id)
        else:
            log_path = "logs/codegen_log.log"

        location = 2
        # 日志和控制台都出现
        if location == 1:
            logger.remove()
            logger.add(sys.stdout)
            logger.add(log_path, encoding="utf-8", enqueue=True, rotation="100 KB")

        # 只在日志中出现
        elif location == 2:
            logger.remove()
            logger.add(log_path, encoding="utf-8", enqueue=True, rotation="100 KB")


loggings = Loggings()
