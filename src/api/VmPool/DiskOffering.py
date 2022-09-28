#!/usr/bin/env python3
# -*- coding:utf-8 -*- 

from typing import Union, Dict
from logging import Logger
from src.api.client import ZStackClient
from src.config import commands
from src.utils.errors import ParameterIsNoneError


"""云盘规格资源类"""


class DiskOffering(ZStackClient):

    def __init__(self, logger: Logger = None):
        super(DiskOffering, self).__init__(logger=logger)

    def create_diskoffering(self, name: str, diskSize: str, description: str = None, allocatorStrategy: str = None,
                            sortKey: str = None, offtype: str = None, resourceUuid: str = None) -> Union[Dict, str]:
        """
        创建云盘规格
        :param name: 云盘规格名称
        :param diskSize: 云盘大小
        :param description: 云盘规格的详细描述
        :param allocatorStrategy: 分配策略 ["DefaultHostAllocatorStrategy", "LastHostPreferredAllocatorStrategy",
                                           "LeastVmPreferredHostAllocatorStrategy", "MinimumCPUUsageHostAllocatorStrategy",
                                           "MinimumMemoryUsageHostAllocatorStrategy", "MaxInstancePerHostHostAllocatorStrategy"
                                           ]
        :param sortKey: 排序键
        :param offtype: 类型
        :param resourceUuid: 资源uuid。若指定，镜像会使用该字段值作为uuid
        """
        if not name or not diskSize:
            raise ParameterIsNoneError(name=name, diskSize=diskSize)
        command = f"{self.zstack_cli} {commands.ZStack_Create_DiskOffering.format(name=name, size=diskSize)}"
        if description:
            command = f"{command} description={description}"
        if allocatorStrategy:
            command = f"{command} allocatorStrategy={allocatorStrategy}"
        if sortKey:
            command = f"{command} sortKey={sortKey}"
        if offtype:
            command = f"{command} type={offtype}"
        if resourceUuid:
            command = f"{command} resourceUuid={resourceUuid}"
        response = self.client.run_command(command)
        return response['stdout']

    def delete_diskoffering(self, uuid: str, deleteMode: str = None) -> Union[Dict, str]:
        """
        删除云盘规格
        :param uuid: 删除云盘规格
        :param deleteMode:删除模式 ["Permissive", "Enforcing"]
        """
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)
        command = f"{self.zstack_cli} {commands.ZStack_Delete_DiskOffering.format(uuid=uuid)}"
        if deleteMode:
            command = f"{command} deleteMode={deleteMode}"
        response = self.client.run_command(command)
        return response['stdout']

    def query_diskoffering(self, diskSize: str = None, name: str = None) -> Union[Dict, str]:
        """
        查询云盘规格
        :param diskSize: 云盘大小。支持运算符
        :param name: 云盘名称
        """
        command = f"{self.zstack_cli} {commands.ZStack_Query_DiskOffering}"
        if diskSize:
            command = f"{command} diskSize={diskSize}"
        if name:
            command = f"{command} name={name}"
        response = self.client.run_command(command)
        return response['stdout']

    def change_diskoffering_state(self, uuid: str, stateEvent: str) -> Union[Dict, str]:
        """
        更改云盘规格的启用状态
        :param uuid: 云盘规格uuid
        :param stateEvent: 状态事件 ["enable", "disable"]
        """
        if not uuid or not stateEvent:
            raise ParameterIsNoneError(uuid=uuid, stateEvent=stateEvent)
        command = f"{self.zstack_cli} {commands.ZStack_Change_DiskOffering_State.format(uuid=uuid, state=stateEvent)}"
        response = self.client.run_command(command)
        return response['stdout']

    def update_diskoffering(self, uuid: str, name: str, description: str = None) -> Union[Dict, str]:
        """
        更新云盘规格
        :param uuid: 云盘规格uuid
        :param name: 云盘规格名称
        :param description: 云盘规格的详细描述
        """
        if not uuid or not name:
            raise ParameterIsNoneError(uuid=uuid, name=name)
        command = f"{self.zstack_cli} {commands.ZStack_Update_DiskOffering.format(uuid=uuid, name=name)}"
        if description:
            command = f"{command} description={description}"
        response = self.client.run_command(command)
        return response['stdout']
