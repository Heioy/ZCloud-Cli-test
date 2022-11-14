#!/usr/bin/env python3
# -*- coding:utf-8 -*- 

import os
import sys
import shutil
import unittest
from src.utils.readFile import read_toml
from typing import List
from src.utils.errors import ParameterIsNoneError
from src.scripts.instancePool.createVmInstance import Test_Create_and_Delete_Vm_Instance

base_path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(base_path)

# 读取配置文件
caseConfig = os.path.join(base_path, "config/case.toml")
config = read_toml(caseConfig)


def create_log_dir():
    logDirName = config['TestCase']['loggerDirName']
    logCount = config['TestCase']['loggerCount']
    log_dir = os.path.join(base_path, logDirName)

    if not os.path.exists(log_dir):
        print(f"{log_dir} not exist, Create it!")
        os.makedirs(log_dir)

    remove_logs(log_dir, logCount)


def remove_logs(logPath: str, logCount: int):
    dirs = os.listdir(logPath)
    if not dirs:
        print(f"{logPath} 为空目录!")
    else:
        dir_list = [os.path.join(logPath, _dir) for _dir in dirs if os.path.isdir(os.path.join(logPath, _dir))]
        dir_list.sort()

        if len(dir_list) >= logCount:
            try:
                print(f"remove {dir_list[0]}")
                shutil.rmtree(dir_list[0])
            except Exception:
                pass


def runcases():
    suite = unittest.TestSuite()
    test = [
        Test_Create_Vm_Instance.TestCreateVMInstance('test_query_vm_instance')
    ]
    suite.addTests(test)
    runner = unittest.TextTestRunner()
    runner.run(suite)


def runall(case_modules: List[str], pattern: str = "Test*.py"):
    if not case_modules:
        raise ParameterIsNoneError(case_modules=case_modules)
    if not isinstance(case_modules, list):
        raise ValueError(f"传入的模块参数类型为非列表 <{type(case_modules)}>")

    for module in case_modules:
        module_path = os.path.abspath(module)
        # print(f"module_path:  {module_path}")

        cases = unittest.TestLoader().discover(start_dir=module_path, pattern=pattern, top_level_dir=None)

        runner = unittest.TextTestRunner()
        runner.run(cases)


if __name__ == '__main__':
    create_log_dir()
    modules = ["instancePool"]
    runall(modules)
