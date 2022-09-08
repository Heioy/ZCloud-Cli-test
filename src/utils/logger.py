#!/usr/bin/env python3
# -*- coding:utf-8 -*- 


import os
import logging
from logging import handlers


def get_logger(filename: str = None,
               name: str = None,
               ):
    """
    输出日志到终端和日志文件
    :param name:
    :param filename:
    """
    Format_str = "%(asctime)s [%(filename)s:%(funcName)s] lines:%(lineno)d::%(levelname)s- : %(message)s"
    forMat = logging.Formatter(Format_str)
    if not name:
        name = "ZStack-Cli"

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # if not logger.handlers:
    #     # 终端记录日志
    #     console_handler = logging.StreamHandler()
    #     # console_handler.setLevel(logging.INFO)
    #     Format = logging.Formatter(Format_str)
    #     console_handler.setFormatter(Format)
    #     logger.addHandler(console_handler)
    #
    #     # 日志记录文件
    #     if filename:
    #         file_handler = logging.FileHandler(filename)
    #         console_handler.setLevel(logging.DEBUG)
    #         file_handler.setFormatter(Format)
    #         logger.addHandler(file_handler)

    if filename not in [handle.name for handle in logger.handlers]:
        file = logging.FileHandler(filename=filename)  # 文件日志
        file.setFormatter(forMat)
        file.set_name(filename)
        logger.addHandler(file)

        # 打印控制台日志和文件日志
    if "stream" not in [handle.name for handle in logger.handlers]:
        stream = logging.StreamHandler()  # 控制台打印日志
        stream.setFormatter(forMat)
        stream.set_name("stream")
        logger.addHandler(stream)

    return logger

