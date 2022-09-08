#!/usr/bin/env python3
# -*- coding:utf-8 -*- 

"""
#========================================================
# FileName     : error.py
# CreatedTime  : 2022/8/29 22:11
# Author       : maoqiang.wu@woqutech.com
# Description  : 
# ChangedTime  :
#=========================================================
"""
from typing import Type, Any


class ConnectionTimeout(Exception):
    pass


class ParameterError(Exception):
    def __init__(self, act_type: Type, exc_val: Any = None):
        self.exc_val = exc_val
        self.exc_type = type(self.exc_val)
        self.act_type = act_type

    def __str__(self):
        return f"参数类型传递错误. 期望类型: {self.exc_type}, 传入类型: {self.act_type}"


class ParameterIsNoneError(Exception):

    def __init__(self, *args, **kwargs):
        self.msg = ""
        if args:
            for arg in args:
                if arg is None:
                    self.msg += f"{arg} "
        elif kwargs:
            for key, arg in kwargs.items():
                if arg is None:
                    self.msg += f"{key} "

    def __str__(self):
        return f"参数传递不合法.部分参数为空. {self.msg}"


class RunCommandTimeoutError(Exception):
    def __init__(self, command: Any, timeout: int, remote_ip: Any = None, local: bool = False):
        self.command = command
        self.local = local
        self.remote_ip = remote_ip
        self.timeout = timeout

    def __str__(self):
        if self.local:
            return f"本地执行命令<{self.command}>超时{self.timeout}s"
        else:
            return f"远端执行命令<{self.remote_ip} {self.command}>超时{self.timeout}s"


class SSHConnectingError(Exception):
    pass


class ChannelError(Exception):

    def __init__(self, command: Any, remote_ip: Any = None):
        self.command = command
        self.remote_ip = remote_ip

    def __str__(self):
        return f"远程<{self.remote_ip}>执行命令<{self.command}>异常."


class RemoteCommandError(Exception):

    def __init__(self, command: str, exc_val: Any):
        self.command = command
        self.exc_val = exc_val

    def __str__(self):
        return f"执行<{self.command}>失败. 失败详情: \n{self.exc_val}"
