#!/usr/bin/env python3
# -*- coding:utf-8 -*- 

from typing import Union, Dict
from logging import Logger
from src.api.client import ZStackClient
from src.config import commands
from src.utils.errors import ParameterIsNoneError


"""计算规格资源类"""


class InstanceOffering(ZStackClient):

    def __init__(self, logger: Logger = None):
        super(InstanceOffering, self).__init__(logger=logger)

    def create_instance_offering(self, name: str, cpuNum: int, memorySize: int, description: str = None,
                                 allocatorStrategy: str = None, sortKey: str = None, offtype: str = None,
                                 resourceUuid: str = None) -> Union[Dict, str]:
        """
        创建云主机规格
        :param name: 计算规格名称
        :param cpuNum: CPU数目
        :param memorySize: 内存大小，大小Byte
        :param description: 计算规格的详细描述
        :param allocatorStrategy: 分配策略 ["DefaultHostAllocatorStrategy", "LastHostPreferredAllocatorStrategy",
                                           "LeastVmPreferredHostAllocatorStrategy", "MinimumCPUUsageHostAllocatorStrategy",
                                           "MinimumMemoryUsageHostAllocatorStrategy", "MaxInstancePerHostHostAllocatorStrategy"]
        :param sortKey: 排序键
        :param offtype: 类型
        :param resourceUuid: 资源uuid。若指定，镜像会使用该字段值作为uuid
        """
        if not name or not cpuNum or not memorySize:
            raise ParameterIsNoneError(name=name, cpuNum=cpuNum, memorySize=memorySize)
        command = f"{self.zstack_cli} {commands.ZStack_Create_InstanceOffering.format(name=name, num=cpuNum, memSize=memorySize)}"
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

    def delete_instance_offering(self, uuid: str, deleteMode: str = None) -> Union[Dict, str]:
        """
        删除云主机规格
        :param uuid: 计算规格uuid
        :param deleteMode: 删除模式 ["Permissive", "Enforcing"]
        """
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)
        command = f"{self.zstack_cli} {commands.ZStack_Delete_InstanceOffering.format(uuid=uuid)}"
        if deleteMode:
            command = f"{command} deleteMode={deleteMode}"
        response = self.client.run_command(command)
        return response['stdout']

    def query_instance_offering(self, cpuSpeed: str = None, cpuNum: str = None, state: str = None) -> Union[Dict, str]:
        """
        查询云主机规格
        :param cpuSpeed: cpu速率
        :param cpuNum: cpu个数。支持运算符运算
        :param state: 云主机实例状态
        """
        command = f"{self.zstack_cli} {commands.ZStack_Query_InstanceOffering}"
        if cpuSpeed:
            command = f"{command} cpuSpeed={cpuNum}"
        if cpuNum:
            command = f"{command} cpuNum={cpuNum}"
        if state:
            command = f"{command} vmInstance.state={state}"
        response = self.client.run_command(command)
        return response['stdout']

    def change_instance_offering(self, vmInstanceUuid: str, instanceOfferingUuid: str) -> Union[Dict, str]:
        """
        更改云主机规格
        :param vmInstanceUuid: 云主机uuid
        :param instanceOfferingUuid: 计算规格uuid
        """
        if not vmInstanceUuid or not instanceOfferingUuid:
            raise ParameterIsNoneError(vmInstanceUuid=vmInstanceUuid, instanceOfferingUuid=instanceOfferingUuid)
        command = f"{self.zstack_cli} {commands.ZStack_Change_InstanceOffering.format(vuuid=vmInstanceUuid, offUuid=instanceOfferingUuid)}"
        response = self.client.run_command(command)
        return response['stdout']

    def update_instance_offering(self, uuid: str, name: str = None, description: str = None, allocatorStrategy: str = None) -> Union[Dict, str]:
        """
        更新云主机规格
        :param uuid: 计算规格uuid
        :param name: 计算规格名称
        :param description: 计算规格的详细描述
        :param allocatorStrategy: 分配策略 ["DefaultHostAllocatorStrategy", "LastHostPreferredAllocatorStrategy",
                                           "LeastVmPreferredHostAllocatorStrategy", "MinimumCPUUsageHostAllocatorStrategy",
                                           "MinimumMemoryUsageHostAllocatorStrategy", "MaxInstancePerHostHostAllocatorStrategy"
                                           ]
        """
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)
        command = f"{self.zstack_cli} {commands.ZStack_Update_InstanceOffering.format(uuid=uuid)}"
        if name:
            command = f"{command} name={name}"
        if description:
            command = f"{command} description={description}"
        if allocatorStrategy:
            command = f"{command} allocatorStrategy={allocatorStrategy}"
        response = self.client.run_command(command)
        return response['stdout']

    def change_instance_offering_state(self, uuid: str, stateEvent: str) -> Union[Dict, str]:
        """
        更改云主机规格的启用状态
        :param uuid: 计算规格uuid
        :param stateEvent: 状态事件 ["enable", "disable"]
        """
        if not uuid or not stateEvent:
            raise ParameterIsNoneError(uuid=uuid, stateEvent=stateEvent)
        command = f"{self.zstack_cli} {commands.ZStack_Change_InstanceOffering_State.format(uuid=uuid, state=stateEvent)}"
        response = self.client.run_command(command)
        return response['stdout']
