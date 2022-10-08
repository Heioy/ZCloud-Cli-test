#!/usr/bin/env python3
# -*- coding:utf-8 -*- 

from typing import Union, Dict
from logging import Logger
from src.api.client import ZStackClient
from src.config import commands
from src.utils.errors import ParameterIsNoneError


class Cluster(ZStackClient):

    def __init__(self, logger: Logger = None):
        super(Cluster, self).__init__(logger=logger)

    def create_cluster(self, zoneUuid: str, name: str, hypervisorType: str, resourceUuid: str = None,
                       description: str = None, architecture: str = None) -> Union[Dict, str]:
        """
        创建集群
        :param zoneUuid: 父区域的uuid
        :param name: 资源名字
        :param hypervisorType: 虚拟机管理程序类型 ["KVM", "Simulator"]
        :param resourceUuid: 资源uuid
        :param description: 资源描述
        :param architecture: 集群所使用的架构 ["x86_64", "aarch64", "mips64el"]
        """
        if not zoneUuid or not name or not hypervisorType:
            raise ParameterIsNoneError(zoneUuid=zoneUuid, name=name, hypervisorType=hypervisorType)
        command = f"{self.zstack_cli} {commands.ZStack_Create_Cluster.format(zoneUuid=zoneUuid, name=name, hyperType=hypervisorType)}"
        if resourceUuid:
            command = f"{command} resourceUuid={resourceUuid}"
        if description:
            command = f"{command} description={description}"
        if architecture:
            command = f"{command} architecture={architecture}"

        response = self.client.run_command(command)
        return response['stdout']

    def delete_cluster(self, uuid: str, deleteMode: str = None) -> Union[Dict, str]:
        """
        删除集群
        :param uuid: 集群的uuid
        :param deleteMode: 资源删除模式 ["Permissive", "Enforcing"]
        """
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)
        command = f"{self.zstack_cli} {commands.ZStack_Delete_Cluster.format(uuid=uuid)}"
        if deleteMode:
            command = f"{command} deleteMode={deleteMode}"
        response = self.client.run_command(command)
        return response['stdout']

    def query_cluster(self, hypervisorType: str = None, name: str = None) -> Union[Dict, str]:
        """
        查询集群
        :param hypervisorType: 虚拟机管理程序类型 ["KVM", "Simulator"]
        :param name: 集群名称
        """
        command = f"{self.zstack_cli} {commands.ZStack_Query_Cluster}"
        if hypervisorType:
            command = f"{command} hypervisorType={hypervisorType}"
        if name:
            command = f"{command} name={name}"
        response = self.client.run_command(command)
        return response['stdout']

    def update_cluster(self, uuid: str, name: str, description: str = None) -> Union[Dict, str]:
        """
        更新集群信息
        :param uuid: 集群的uuid
        :param name: 资源名字
        :param description: 资源描述
        """
        if not uuid or not name:
            raise ParameterIsNoneError(uuid=uuid, name=name)
        command = f"{self.zstack_cli} {commands.ZStack_Update_Cluster.format(uuid=uuid, name=name)}"
        if description:
            command = f"{command} description={description}"
        response = self.client.run_command(command)
        return response['stdout']

    def change_cluster_state(self, uuid: str, stateEvent: str) -> Union[Dict, str]:
        """
        改变集群的可用状态
        :param uuid: 集群的uuid
        :param stateEvent: 可用状态触发事件 ["enable", "disable"]
        """
        if not uuid or not stateEvent:
            raise ParameterIsNoneError(uuid=uuid, stateEvent=stateEvent)
        command = f"{self.zstack_cli} {commands.ZStack_Change_Cluster_State.format(uuid=uuid, state=stateEvent)}"
        response = self.client.run_command(command)
        return response['stdout']
