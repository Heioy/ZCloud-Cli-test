#!/usr/bin/env python3
# -*- coding:utf-8 -*- 

from typing import Union, Dict
from logging import Logger
from src.api.client import ZStackClient
from src.config import commands
from src.utils.errors import ParameterIsNoneError


class Zone(ZStackClient):

    def __init__(self, logger: Logger = None):
        super(Zone, self).__init__(logger=logger)

    def create_zone(self, name: str, resourceUuid: str = None, description: str = None) -> Union[Dict, str]:
        """
        创建一个新的区域
        :param name: 资源名字
        :param resourceUuid: 资源uuid
        :param description: 资源描述
        """
        if not name:
            raise ParameterIsNoneError(name=name)
        command = f"{self.zstack_cli} {commands.ZStack_Create_Zone.format(name=name)}"
        if resourceUuid:
            command = f"{command} resourceUuid={resourceUuid}"
        if description:
            command = f"{command} description={description}"
        response = self.client.run_command(command)
        return response['stdout']

    def delete_zone(self, uuid: str, deleteMode: str = None) -> Union[Dict, str]:
        """
        删除一个区域
        :param uuid: 区域 uuid
        :param deleteMode: 资源删除模式
        """
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)
        command = f"{self.zstack_cli} {commands.ZStack_Delete_Zone.format(uuid=uuid)}"
        if deleteMode:
            command = f"{command} deleteMode={deleteMode}"
        response = self.client.run_command(command)
        return response['stdout']

    def query_zone(self, name: str = None, vmUuid: str = None) -> Union[Dict, str]:
        """
        查询区域
        :param name: 区域名称
        :param vmUuid: 云主机实例的uuid
        """
        command = f"{self.zstack_cli} {commands.ZStack_Query_Zone}"
        if name:
            command = f"{command} name={name}"
        if vmUuid:
            command = f"{command} vmInstance.uuid={vmUuid}"
        response = self.client.run_command(command)
        return response['stdout']

    def update_zone(self, uuid: str, name: str, description: str = None) -> Union[Dict, str]:
        """
        更新区域的名称、描述和标签
        :param uuid: 区域uuid
        :param name: 资源名字
        :param description: 资源描述
        """
        if not uuid or not name:
            raise ParameterIsNoneError(uuid=uuid, name=name)
        command = f"{self.zstack_cli} {commands.ZStack_Update_Zone.format(uuid=uuid, name=name)}"
        if description:
            command = f"{command} description={description}"
        response = self.client.run_command(command)
        return response['stdout']

    def change_zone_state(self, uuid: str, stateEvent: str) -> Union[Dict, str]:
        """
        改变区域的可用状态
        :param uuid: 区域uuid
        :param stateEvent: 状态触发事件。
                • enable:改变可用状态为启用(Enabled)
                • disable:改变可用状态为禁用(Disabled)
        """
        if not uuid or not stateEvent:
            raise ParameterIsNoneError(uuid=uuid, stateEvent=stateEvent)
        command = f"{self.zstack_cli} {commands.ZStack_Change_Zone_State.format(uuid=uuid, state=stateEvent)}"
        response = self.client.run_command(command)
        return response['stdout']
