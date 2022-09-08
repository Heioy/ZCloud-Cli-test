#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import json
from pprint import pprint
from logging import Logger
from typing import Any, List, Dict
from src.utils.ssh import Client
from src.api.base import Base
from src.utils.parser import (
    ParseController,
    ParseZStackClient
)
from src.config.command import *
from src.utils.errors import *

class ZStackClient(Base):

    def __init__(self, logger: Logger = None):
        super(ZStackClient, self).__init__(logger=logger)
        self.zstack_cli = self.config['develop']['zstack_cli']
        self.accountName = self.config['develop']['accountName']
        self.accountPassword = self.config['develop']['accountPassword']
        self.session: bool = False




        if not self.session:
            self.login()

    def login(self):
        """Login ZStack Client Management"""
        # command = [self.zstack_cli, "LogInByAccount", "accountName=%s" % self.username, "password=%s" % self.password]
        command = f"{self.zstack_cli} {ZStack_Login_Account.format(username=self.accountName, password=self.accountPassword)}"
        response = self.client.run_command(command)
        session = response['stdout']

        result = ParseController('parseLogin', response, ParseZStackClient).parse()
        try:
            if 'success' in result.keys() and result.get('success'):
                self.logger.info(f"用户<{self.accountName}>登录成功.")
                self.session = True
            else:
                self.logger.error(f"用户<{self.accountName}>登录失败!")
                raise Exception(f"用户<{self.accountName}>登录失败!")
        except AttributeError:
            pass

    def logOut(self):
        """LogOut"""
        command = f"{self.zstack_cli} {ZStack_LogOut}"
        response = self.client.run_command(command)
        if json.loads(response)['stdout']['success']:
            self.session = False
            # logger.debug("退出")
        else:
            # logger.debug("建立session成功")
            raise Exception("用户退出失败!")

    def query_zone(self, name: str = None):
        """Query ZStack Zone"""
        self.logger.info("查询物理机所在区域...")
        if not name:
            command = f"{self.zstack_cli} {ZStack_Query_Zone}"
        else:
            command = f"{self.zstack_cli} {ZStack_Query_Zone} name={name}"

        response = self.client.run_command(command)
        return response['stdout']





if __name__ == '__main__':
    cli = ZStackClient()
    cli.query_zone()

# print(os.path.dirname(os.getcwd()))