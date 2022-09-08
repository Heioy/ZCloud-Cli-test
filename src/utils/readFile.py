#!/usr/bin/env python3
# -*- coding:utf-8 -*- 

"""
#========================================================
# FileName     : readFile.py.py
# CreatedTime  : 2022/8/29 18:54
# Author       : maoqiang.wu@woqutech.com
# Description  : 
# ChangedTime  :
#=========================================================
"""

import tomli
from pprint import pprint


def read_toml(file_path: str, mode: str = 'r', encoding: str = "utf-8"):
    with open(file_path, mode=mode, encoding=encoding) as obj:
        content = obj.read()
        text = tomli.loads(content)
    return text


