#!/usr/bin/env python3
# -*- coding:utf-8 -*- 

from typing import Union, Dict
from logging import Logger
from src.api.client import ZStackClient
from src.config import commands
from src.utils.errors import ParameterIsNoneError


class VPCRouter(ZStackClient):

    def __init__(self, logger: Logger = None):
        super(VPCRouter, self).__init__(logger=logger)

    def create_vpcVRouter(self, name: str, virtualRouterOfferingUuid: str, description: str = None, \
                          resourceUuid: str = None) -> Union[Dict, str]:
        """
        创建VPC路由器
        :param name: VPC路由器名称
        :param virtualRouterOfferingUuid: 路由器规格
        :param description: VPC路由器的详细描述
        :param resourceUuid: 资源UUID。若指定，VPC路由器会使用该字段值作为UUID
        """
        if not name or not  virtualRouterOfferingUuid:
            raise ParameterIsNoneError(name=name, virtualRouterOfferingUuid=virtualRouterOfferingUuid)
        command = f"{self.zstack_cli} {commands.ZStack_Create_VpcVRouter.format(name=name, virtualRouterOfferingUuid=virtualRouterOfferingUuid)}"
        if description:
            command = f"{command} description={description}"
        if resourceUuid:
            command = f"{command} resourceUuid={resourceUuid}"
        response = self.client.run_command(command)
        return response['stdout']

    def query_vpcRouter(self) -> Union[Dict, str]:
        """
        查询VPC路由器
        """
        command = f"{self.zstack_cli} {commands.ZStack_Query_VpcRouter}"
        response = self.client.run_command(command)
        return response['stdout']

    def get_attachable_vpc_L3Network(self, uuid: str) -> Union[Dict, str]:
        """
        获取VPC路由器可加载的三层网络
        :param uuid: VPC路由器UUID
        """
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)
        command = f"{self.zstack_cli} {commands.ZStack_Get_Attachable_VPC_L3Network.format(uuid=uuid)}"
        response = self.client.run_command(command)
        return response['stdout']

    def get_vpcVRouter_distributed_routing_connections(self, uuid: str) -> Union[Dict, str]:
        """
        获取VPC路由器实时流量状态
        :param uuid: VPC路由器UUID。需要开启分布式路由，才能获取到VPC路由器实时流量状态
        """
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)
        command = f"{self.zstack_cli} {commands.ZStack_Get_VPCVRouter_Distributed_Routing_Connections.format(uuid=uuid)}"
        response = self.client.run_command(command)
        return response['stdout']

    def get_vpcVRouter_distributed_routing_enabled(self, uuid: str) -> Union[Dict,str]:
        """
        获取分布式路由是否打开
        :param uuid: VPC路由器UUID
        """
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)
        command = f"{self.zstack_cli} {commands.ZStack_Get_VPCVRouter_Distributed_Routing_Enabled.format(uuid=uuid)}"
        response = self.client.run_command(command)
        return response['stdout']

    def set_vpcVRouter_distributed_routing_enabled(self, uuid: str, stateEvent: str) -> Union[Dict, str]:
        """
        设置分布式路由开关
        :param uuid: VPC路由器UUID
        :param stateEvent: 资源的可用状态 ["enable", "disable"]
        """
        if not uuid or not stateEvent:
            raise ParameterIsNoneError(uuid=uuid, stateEvent=stateEvent)
        command = f"{self.zstack_cli} {commands.ZStack_Set_VPCVRouter_Distributed_Routing_Enabled.format(uuid=uuid, state=stateEvent)}"
        response = self.client.run_command(command)
        return response['stdout']

    def add_dns_to_vpcRouter(self, uuid: str, dns: str, resourceUuid: str = None) -> Union[Dict, str]:
        """
        向VPC路由器添加DNS
        :param uuid: VPC路由器UUID
        :param dns:
        :param resourceUuid: 资源UUID
        """
        if not uuid or not dns:
            raise ParameterIsNoneError(uuid=uuid, dns=dns)
        command = f"{self.zstack_cli} {commands.ZStack_Add_DNS_to_VPCRouter.format(uuid=uuid, dns=dns)}"
        if resourceUuid:
            command = f"{command} resourceUuid={resourceUuid}"
        response = self.client.run_command(command)
        return response['stdout']

    def remove_dns_from_vpcRouter(self, uuid: str, dns: str) -> Union[Dict, str]:
        """
        从VPC路由器移除DNS
        :param uuid: VPC路由器UUID
        :param dns:
        """
        if not uuid or not dns:
            raise ParameterIsNoneError(uuid=uuid, dns=dns)
        command = f"{self.zstack_cli} {commands.ZStack_Remove_DNS_from_VPCRouter.format(uuid=uuid, dns=dns)}"
        response = self.client.run_command(command)
        return response['stdout']

    def get_vpcVRouter_networkService_state(self, uuid: str, networkService: str = "SNAT") -> Union[Dict, str]:
        """
        获取VPC路由器的网络服务状态
        :param uuid: 资源的UUID，唯一标示该资源
        :param networkService: 路由器提供的网络服务
        """
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)
        command = f"{self.zstack_cli} {commands.ZStack_Get_VPCVRouter_NetworkService_State.format(uuid=uuid, service=networkService)}"
        response = self.client.run_command(command)
        return response['stdout']

    def set_vpcVRouter_networkService_state(self, uuid: str, state: str, networkService: str = 'SNAT') -> Union[Dict, str]:
        """
        设置VPC路由器的网络服务
        :param uuid: 资源的UUID，唯一标示该资源
        :param networkService: 路由器提供的网络服务
        :param state: 服务状态
        """
        if not uuid or not state:
            raise ParameterIsNoneError(uuid=uuid, state=state)
        command = f"{self.zstack_cli} {commands.ZStack_Set_VPCVRouter_NetworkService_State.format(uuid=uuid, state=state, service=networkService)}"
        response = self.client.run_command(command)
        return response['stdout']

    def change_vpc_HAGroup_monitorIps(self, uuid: str, monitorIps: str = None) -> Union[Dict, str]:
        """
        更新高可用组仲裁ip
        :param uuid: 资源的UUID，唯一标示该资源
        :param monitorIps:
        """
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)
        command = f"{self.zstack_cli} {commands.ZStack_Change_VPC_HAGroup_Monitorlps.format(uuid=uuid)}"
        if monitorIps:
            command = f"{command} monitorIps={monitorIps}"
        response = self.client.run_command(command)
        return response['stdout']

    def create_vpc_haGroup(self, name: str, description: str = None, monitorIps: str = None, resourceUuid: str = None) -> Union[Dict, str]:
        """
        创建高可用组
        :param name: 资源名称
        :param description: 资源的详细描述
        :param monitorIps:
        :param resourceUuid:
        """
        if not name:
            raise ParameterIsNoneError(name=name)
        command = f"{self.zstack_cli} {commands.ZStack_Create_VPC_HAGroup.format(name=name)}"
        if description:
            command = f"{command} description={description}"
        if monitorIps:
            command = f"{command} monitorIps={monitorIps}"
        if resourceUuid:
            command = f"{command} resourceUuid={resourceUuid}"
        response = self.client.run_command(command)
        return response['stdout']

    def delete_vpc_haGroup(self, uuid: str, deleteMode: str = None) -> Union[Dict, str]:
        """
        删除高可用组
        :param uuid: 资源的UUID，唯一标示该资源
        :param deleteMode:
        """
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)
        command = f"{self.zstack_cli} {commands.ZStack_Delete_VPC_HAGroup.format(uuid=uuid)}"
        if deleteMode:
            command = f"{command} deleteMode={deleteMode}"
        response = self.client.run_command(command)
        return response['stdout']

    def update_vpc_haGroup(self, uuid: str, name: str = None, description: str = None) -> Union[Dict, str]:
        """
        更新高可用组
        :param uuid: 资源的UUID，唯一标示该资源
        :param name: 资源名称
        :param description: 资源的详细描述
        """
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)
        command = f"{self.zstack_cli} {commands.ZStack_Update_VPC_HAGroup.format(uuid=uuid)}"
        if name:
            command = f"{command} name={name}"
        if description:
            command = f"{command} description={description}"
        response = self.client.run_command(command)
        return response['stdout']

    def query_vpc_haGroup(self) -> Union[Dict, str]:
        """
        查询高可用组
        """
        command = f"{self.zstack_cli} {commands.ZStack_Query_VPC_HAGroup}"
        response = self.client.run_command(command)
        return response['stdout']

    def update_virtual_router(self, vmInstanceUuid: str, defaultRouteL3NetworkUuid: str = None) -> Union[Dict, str]:
        """
        更新虚拟路由器
        :param vmInstanceUuid: 资源的UUID，唯一标示该资源
        :param defaultRouteL3NetworkUuid:
        """
        if not vmInstanceUuid:
            raise ParameterIsNoneError(vmInstanceUuid=vmInstanceUuid)
        command = f"{self.zstack_cli} {commands.ZStack_Update_Virtual_Router.format(vuuid=vmInstanceUuid)}"
        if defaultRouteL3NetworkUuid:
            command = f"{command} defaultRouteL3NetworkUuid={defaultRouteL3NetworkUuid}"
        response = self.client.run_command(command)
        return response['stdout']
