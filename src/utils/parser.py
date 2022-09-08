#!/usr/bin/env python3
# -*- coding:utf-8 -*- 

from operator import methodcaller
from typing import Dict


class ParseZStackControl(object):

    def parseUiConfig(self, response) -> Dict[str, str]:
        result = {}
        if response['stderr']:
            print(f"命令执行异常. 异常信息: {response['stderr']}")
        else:
            for line in response['stdout'].strip('\n').split('\n'):
                if line.strip():
                    result[line.strip().split('=')[0].strip()] = line.strip().split('=')[1].strip()
        return result

    def ParseDropSession(self, response) -> str:
        return response['stdout'].strip('\n')


    def parseShowSessions(self, response) -> Dict[str, str]:
        result = {}
        if response['stderr']:
            print(f"命令执行异常. 异常信息: {response['stderr']}")
        else:
            for line in response['stdout'].strip('\n').split('\n'):
                if 'account sessions' in line or '---' in line or 'total' in line:
                    pass
                elif line.strip():
                    result[line.strip().split()[0]] = line.strip().split()[1]
        return result

    def parse_one(self, response):
        return response


class ParseZStackClient(object):

    def parseLogin(self, response):
        if isinstance(response['stdout'], str) and response['returncode'] != 0:
            raise AssertionError(f"登录失败. 失败详情: {response['stdout']}")
        elif isinstance(response['stdout'], dict):
            return response['stdout']


class ParseController(object):

    def __init__(self, name, response, className, *args, **kwargs):
        """Extract Function Name to Parse"""
        if not response:
            raise ValueError(f"传入的<response: {response}>不合法!")
        self.name = name
        self.response = response
        self.className = className

    def parse(self):
        return methodcaller(self.name, self.response)(self.className())


# if __name__ == '__main__':
#     print(ParseController('parse_one', 111, ParseZStackControl).parse())
