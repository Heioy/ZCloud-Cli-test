#!/usr/bin/env python3
# -*- coding:utf-8 -*- 

import os
import sys
import shutil
import datetime
from src.utils.readFile import read_toml

base_path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(base_path)

# 读取配置文件
caseConfig = os.path.join(base_path, "config/case.toml")
config = read_toml(caseConfig)

logDirName = config['TestCase']['loggerDirName']
logCount = config['TestCase']['loggerCount']
log_dir = os.path.join(base_path, logDirName)
date = datetime.datetime.now().strftime('%y%m%d%H%M%S')

def create_log_dir():
    if not os.path.exists(log_dir):
        print(f"{log_dir} not exist, Create it!")
        os.makedirs(log_dir)


def remove_logs():
    dirs = os.listdir(log_dir)
    if not dirs:
        print(f"{log_dir} 为空目录!")
    else:
        dir_list = [os.path.join(log_dir, _dir) for _dir in dirs if os.path.isdir(os.path.join(log_dir, _dir))]
        dir_list.sort()

        if len(dir_list) >= logCount:
            try:
                print(f"remove {dir_list[0]}")
                shutil.rmtree(dir_list[0])
            except Exception:
                pass

create_log_dir()
remove_logs()
