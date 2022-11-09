#!/usr/bin/env python3
# -*- coding:utf-8 -*- 

from typing import Union, Dict
from logging import Logger
from src.api.client import ZStackClient
from src.config import commands
from src.utils.errors import ParameterIsNoneError


class VRouterOSPF(ZStackClient):

    def __init__(self, logger: Logger = None):
        super(VRouterOSPF, self).__init__(logger=logger)

    def create_vRouter_ospf_area(self, areaId: str, areaAuth: str = None, areaType: str = None, password: str = None,
                                 keyId: str = None, resourceUuid: str = None) -> Union[Dict, str]:
        """
        创建路由区域资源
        :param areaId: 区域Id，区域标识
        :param areaAuth: OSPF区域的认证方式
        :param areaType: 区域类型
        :param password: 认证方式为plaintext时的密码
        :param keyId: 认证方式为MD5时用到的keyid
        :param resourceUuid: 区域资源的唯一标识
        """
        if not areaId:
            raise ParameterIsNoneError(areaId=areaId)
        command = f"{self.zstack_cli} {commands.ZStack_Create_VRouter_OSPF_Area.format(areaId=areaId)}"
        if areaAuth:
            command = f"{command} areaAuth={areaAuth}"
        if areaType:
            command = f"{command} areaType={areaType}"
        if password:
            command = f"{command} password={password}"
        if keyId:
            command = f"{command} keyId={keyId}"
        if resourceUuid:
            command = f"{command} resourceUuid={resourceUuid}"
        response = self.client.run_command(command)
        return response['stdout']

    def delete_vRouter_ospf_area(self, uuid: str, deleteMode: str = None) -> Union[Dict, str]:
        """
        删除OSPF路由区域
        :param uuid: 资源的UUID，唯一标示该资源
        :param deleteMode:
        """
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)
        command = f"{self.zstack_cli} {commands.ZStack_Delete_VRouter_OSPF_Area.format(uuid=uuid)}"
        if deleteMode:
            command = f"{command} deleteMode={deleteMode}"
        response = self.client.run_command(command)
        return response['stdout']

    def get_vRouter_ospf_neighbor(self, vRouterUuid: str) -> Union[Dict, str]:
        """
        获取OSPF的邻居信息
        :param vRouterUuid: 路由器的uuid，唯一标识
        """
        if not vRouterUuid:
            raise ParameterIsNoneError(vRouterUuid=vRouterUuid)
        command = f"{self.zstack_cli} {commands.ZStack_Get_VRouter_OSPF_Neighbor.format(vRouterUuid=vRouterUuid)}"
        response = self.client.run_command(command)
        return response['stdout']

    def query_vRouter_ospf_area(self) -> Union[Dict, str]:
        """
        查询OSPF路由区域信息
        """
        command = f"{self.zstack_cli} {commands.ZStack_Query_VRouter_OSPF_Area}"
        response = self.client.run_command(command)
        return response['stdout']

    def get_vRouter_routerID(self, vRouterUuid: str) -> Union[Dict, str]:
        """
        获取路由器的ID
        :param vRouterUuid:路由器的UUID，唯一标识
        """
        if not vRouterUuid:
            raise ParameterIsNoneError(vRouterUuid=vRouterUuid)
        command = f"{self.zstack_cli} {commands.ZStack_Get_VRouter_RouterID.format(vRouterUuid=vRouterUuid)}"
        response = self.client.run_command(command)
        return response['stdout']

    def set_vRouter_routerID(self, vRouterUuid: str, routerId: str) -> Union[Dict, str]:
        """
        设置路由器的ID
        :param vRouterUuid: 路由器的UUID，唯一标识
        :param routerId: IP地址形式的ID
        """
        if not vRouterUuid or not routerId:
            raise ParameterIsNoneError(vRouterUuid=vRouterUuid, routerId=routerId)
        command = f"{self.zstack_cli} {commands.ZStack_Set_VRouter_RouterID.format(vRouterUuid=vRouterUuid, routerId=routerId)}"
        response = self.client.run_command(command)
        return response['stdout']

    def add_vRouter_networks_to_ospf_area(self, routerAreaUuid: str, vRouterUuid: str, l3NetworkUuids: str, resourceUuid: str = None) -> Union[Dict, str]:
        """
        添加网络到OSPF的区域
        :param routerAreaUuid: 路由区域的id，唯一标识
        :param vRouterUuid: vpc路由器的唯一标识id
        :param l3NetworkUuids: 3层网络的唯一标识id
        :param resourceUuid: 资源的标识id
        """
        if not routerAreaUuid or not vRouterUuid or not l3NetworkUuids:
            raise ParameterIsNoneError(routerAreaUuid=routerAreaUuid, vRouterUuid=vRouterUuid, l3NetworkUuids=l3NetworkUuids)
        command = f"{self.zstack_cli} {commands.ZStack_Add_VRouter_Networks_to_OSPF_Area.format(routerAreaUuid=routerAreaUuid, vRouterUuid=vRouterUuid, l3uuid=l3NetworkUuids)}"
        if resourceUuid:
            command = f"{command} resourceUuid={resourceUuid}"
        response = self.client.run_command(command)
        return response['stdout']

    def remove_vRouter_networks_from_ospf_area(self, uuids: str, deleteMode: str = None) -> Union[Dict, str]:
        """
        从路由区域中移除网络
        :param uuids: 网络区域表中的uuid，全局唯一标识
        :param deleteMode:
        """
        if not uuids:
            raise ParameterIsNoneError(uuids=uuids)
        command = f"{self.zstack_cli} {commands.ZStack_Remove_VRouter_Networks_from_OSPF_Area.format(uuids=uuids)}"
        if deleteMode:
            command = f"{command} deleteMode={deleteMode}"
        response = self.client.run_command(command)
        return response['stdout']

    def update_vRouter_ospf_area(self, uuid: str, areaAuth: str = None, areaType: str = None, password: str = None,
                                 keyId: str = None) -> Union[Dict, str]:
        """
        更改OSPF的路由区域属性
        :param uuid: 资源的UUID，唯一标示该资源
        :param areaAuth: 区域认证方式
        :param areaType: 区域类型
        :param password: 认证需要的password
        :param keyId: 认证需要的KeyID
        """
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)
        command = f"{self.zstack_cli} {commands.ZStack_Update_VRouter_OSPF_Area.format(uuid=uuid)}"
        if areaAuth:
            command = f"{command} areaAuth={areaAuth}"
        if areaType:
            command = f"{command} areaType={areaType}"
        if password:
            command = f"{command} password={password}"
        if keyId:
            command = f"{command} keyId={keyId}"
        response = self.client.run_command(command)
        return response['stdout']

    def query_vRouter_ospf_network(self) -> Union[Dict, str]:
        """
        查询路由加入到区域的网络信息
        """
        command = f"{self.zstack_cli} {commands.ZStack_Query_VRouter_OSPF_Network}"
        response = self.client.run_command(command)
        return response['stdout']
