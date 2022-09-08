#!/usr/bin/env python3
# -*- coding:utf-8 -*- 

from typing import Any
from src.api.base import Base
from src.utils.parser import (
    ParseController,
    ParseZStackControl
)
from src.config.command import *


class ZStackControl(Base):

    def __init__(self):
        super(ZStackControl, self).__init__()
        self.zstack_ctl = self.config['develop']['zstack_ctl']

    def show_ui_config(self):
        """List All UI Config"""
        command = f"{self.zstack_ctl} {ZStack_Show_UI_Config}"
        response = self.client.run_command(command)
        return ParseController('parseUiConfig', response, ParseZStackControl).parse()

    @property
    def version(self):
        """Get ZStack Version"""
        command = f"{self.zstack_ctl} {ZStack_Get_Version}"
        response = self.client.run_command(command)
        return response['stdout']

    def show_sessions(self):
        """Show Current Login Session"""
        command = f"{self.zstack_ctl} {ZStack_show_Session_list}"
        response = self.client.run_command(command)
        return ParseController('parseShowSessions', response, ParseZStackControl).parse()

    def drop_account_session(self, account: str = None):
        """Drop the designated account sessions"""
        if not account:
            print("清除所有session...")
            command = f"{self.zstack_ctl} {ZStack_Drop_Session} --all"
        elif account:
            command = f"{self.zstack_ctl} {ZStack_Drop_Session} --account {account}"
        response = self.client.run_command(command)
        return ParseController('ParseDropSession', response, ParseZStackControl).parse()



# if __name__ == '__main__':
#     zstack = ZStackControl()
#     print(zstack.show_sessions())
#     print(zstack.show_ui_config())