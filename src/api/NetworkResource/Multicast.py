#!/usr/bin/env python3
# -*- coding:utf-8 -*- 

from typing import Union, Dict
from logging import Logger
from src.api.client import ZStackClient
from src.config import commands
from src.utils.errors import ParameterIsNoneError


class MulticastRouter(ZStackClient):

    def __init__(self, logger: Logger = None):
        super(MulticastRouter, self).__init__(logger=logger)

    def create_multicastRouter(self, vpcRouterVmUuid: str, description: str = None, resourceUuid: str = None) -> Union[Dict, str]:
        """
        创建组播路由器
        :param vpcRouterVmUuid:
        :param description: 资源的详细描述
        :param resourceUuid:
        """
        if not vpcRouterVmUuid:
            raise ParameterIsNoneError(vpcRouterVmUuid=vpcRouterVmUuid)
        command = f"{self.zstack_cli} {commands.ZStack_Create_MulticastRouter.format(vpcRouterVmUuid=vpcRouterVmUuid)}"
        if description:
            command = f"{command} description={description}"
        if resourceUuid:
            command = f"{command} resourceUuid={resourceUuid}"
        response = self.client.run_command(command)
        return response['stdout']

    def delete_multicastRouter(self, uuid: str, deleteMode: str = None) -> Union[Dict, str]:
        """
        删除组播路由器
        :param uuid: 资源的UUID，唯一标示该资源
        :param deleteMode: 资源删除模式
        """
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)
        command = f"{self.zstack_cli} {commands.ZStack_Delete_MulticastRouter.format(uuid=uuid)}"
        if deleteMode:
            command = f"{command} deleteMode={deleteMode}"
        response = self.client.run_command(command)
        return response['stdout']

    def query_multicastRouter(self) -> Union[Dict, str]:
        """
        查询组播路由器
        """
        command = f"{self.zstack_cli} {commands.ZStack_Query_MulticastRouter}"
        response = self.client.run_command(command)
        return response['stdout']

    def change_multicastRouter_state(self, uuid: str, stateEvent: str) -> Union[Dict, str]:
        """
        改变组播路由器状态
        :param uuid: 资源的UUID，唯一标示该资源
        :param stateEvent: 事件状态
        """
        if not uuid or not stateEvent:
            raise ParameterIsNoneError(uuid=uuid, stateEvent=stateEvent)
        command = f"{self.zstack_cli} {commands.ZStack_Change_MulticastRouter_State.format(uuid=uuid, state=stateEvent)}"
        response = self.client.run_command(command)
        return response['stdout']

    def get_vpc_multicastRouter(self, uuid: str) -> Union[Dict, str]:
        """
        获取组播路由表
        :param uuid: 资源的UUID，唯一标示该资源
        """
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)
        command = f"{self.zstack_cli} {commands.ZStack_Get_VPC_MulticastRouter.format(uuid=uuid)}"
        response = self.client.run_command(command)
        return response['stdout']

    def add_rendezvous_point_to_multicastRouter(self, uuid: str, rpAddress: str, groupAddress: str, resourceUuid: str = None) -> Union[Dict, str]:
        """
        添加组播路由静态RP地址
        :param uuid: 资源的UUID，唯一标示该资源
        :param rpAddress:
        :param groupAddress:
        :param resourceUuid:
        """
        if not uuid or not rpAddress or not groupAddress:
            raise ParameterIsNoneError(uuid=uuid, rpAddress=rpAddress, groupAddress=groupAddress)
        command = f"{self.zstack_cli} {commands.ZStack_Add_Rendezvous_Point_to_MulticastRouter.format(uuid=uuid, rpAddress=rpAddress, groupAddress=groupAddress)}"
        if resourceUuid:
            command = f"{command} resourceUuid={resourceUuid}"
        response = self.client.run_command(command)
        return response['stdout']

    def remove_rendezvous_point_from_multicastRouter(self, uuid: str, rpAddress: str, groupAddress: str, deleteMode: str = None) -> Union[Dict, str]:
        """
        删除组播路由器静态RP地址
        :param uuid: 资源的UUID，唯一标示该资源
        :param rpAddress:
        :param groupAddress:
        :param deleteMode:
        """
        if not uuid or not rpAddress or not groupAddress:
            raise ParameterIsNoneError(uuid=uuid, rpAddress=rpAddress, groupAddress=groupAddress)
        command = f"{self.zstack_cli} {commands.ZStack_Remove_Rendezvous_Point_from_MulticastRouter.format(uuid=uuid, rpAddress=rpAddress, groupAddress=groupAddress)}"
        if deleteMode:
            command = f"{command} deleteMode={deleteMode}"
        response = self.client.run_command(command)
        return response['stdout']
