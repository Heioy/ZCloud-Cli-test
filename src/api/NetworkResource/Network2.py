#!/usr/bin/env python3
# -*- coding:utf-8 -*- 

from typing import Union, Dict
from logging import Logger
from src.api.client import ZStackClient
from src.config import commands
from src.utils.errors import ParameterIsNoneError


class L2VxlanNetworkPool(ZStackClient):

    def __init__(self, logger: Logger = None):
        super(L2VxlanNetworkPool, self).__init__(logger=logger)

    def create_L2VxlanNetworkPool(self, name: str, zoneUuid: str, physicalInterface: str, description: str = None,
                                  net_type: str = None, resourceUuid: str = None) -> Union[Dict, str]:
        """
        创建VXLAN网络池
        :param name: VXLAN网络池名称
        :param zoneUuid: 区域uuid
        :param physicalInterface: 物理网卡
        :param description: VXLAN网络池的详细描述
        :param net_type: 类型
        :param resourceUuid: 资源uuid。若指定，镜像会使用该字段值作为uuid
        """
        if not name or not zoneUuid or not physicalInterface:
            raise ParameterIsNoneError(name=name, zoneUuid=zoneUuid, physicalInterface=physicalInterface)
        command = f"{self.zstack_cli} {commands.ZStack_Create_L2_Vxlan_Network_Pool.format(name=name, zoneUuid=zoneUuid, interface=physicalInterface)}"
        if description:
            command = f"{command} description={description}"
        if net_type:
            command = f"{command} type={net_type}"
        if resourceUuid:
            command = f"{command} resourceUuid={resourceUuid}"
        response = self.client.run_command(command)
        return response['stdout']

    def query_L2VxlanNetworkPool(self, uuid: str = None, zoneUuid: str = None) -> Union[Dict, str]:
        """
        查询VXLAN网络池
        :param uuid:
        :param zoneUuid:
        """
        command = f"{self.zstack_cli} {commands.ZStack_Query_L2_Vxlan_Network_Pool}"
        if uuid:
            command = f"{command} uuid={uuid}"
        if zoneUuid:
            command = f"{command} zone.uuid={zoneUuid}"
        response = self.client.run_command(command)
        return response['stdout']

    def create_L2VxlanNetwork(self, name: str, zoneUuid: str, physicalInterface: str, poolUuid: str, description: str = None,
                              vni: str = None, net_type: str = None, resourceUuid: str = None) -> Union[Dict, str]:
        """
        创建VXLAN网络
        :param name: 普通二层网络名称
        :param zoneUuid: 区域uuid
        :param physicalInterface: 物理网卡
        :param poolUuid: Vxlan网络资源池uuid
        :param description: 普通二层网络的详细描述
        :param vni: Vxlan网络ID
        :param net_type: 类型
        :param resourceUuid: 资源uuid。若指定，镜像会使用该字段值作为uuid
        """
        if not name or not zoneUuid or not physicalInterface or not poolUuid:
            raise ParameterIsNoneError(name=name, zoneUuid=zoneUuid, physicalInterface=physicalInterface, poolUuid=poolUuid)
        command = f"{self.zstack_cli} {commands.ZStack_Create_L2_Vxlan_Network.format(name=name, zoneUuid=zoneUuid, interface=physicalInterface, poolUuid=poolUuid)}"
        if description:
            command = f"{command} description={description}"
        if vni:
            command = f"{command} vni={vni}"
        if net_type:
            command = f"{command} type={net_type}"
        if resourceUuid:
            command = f"{command} resourceUuid={resourceUuid}"
        response = self.client.run_command(command)
        return response['stdout']

    def query_L2VxlanNetwork(self, uuid: str = None, zoneUuid: str = None) -> Union[Dict, str]:
        """
        查询VXLAN网络
        :param uuid:
        :param zoneUuid:
        """
        command = f"{self.zstack_cli} {commands.ZStack_Query_L2_Vxlan_Network}"
        if uuid:
            command = f"{command} uuid={uuid}"
        if zoneUuid:
            command = f"{command} zoneUuid={zoneUuid}"
        response = self.client.run_command(command)
        return response['stdout']

    def create_L2NoVlanNetwork(self, name: str, zoneUuid: str, physicalInterface: str, description: str = None,
                               net_type: str = None, resourceUuid: str = None) -> Union[Dict, str]:
        """
        创建普通二层网络
        :param name: 普通二层网络名称
        :param zoneUuid: 区域uuid
        :param physicalInterface: 物理网卡
        :param description: 普通二层网络的详细描述
        :param net_type: 类型
        :param resourceUuid: 资源uuid。若指定，镜像会使用该字段值作为uuid
        """
        if not name or not zoneUuid or not physicalInterface:
            raise ParameterIsNoneError(name=name, zoneUuid=zoneUuid, physicalInterface=physicalInterface)
        command = f"{self.zstack_cli} {commands.ZStack_Create_L2_NoVlan_Network.format(name=name, zoneUuid=zoneUuid, physicalInterface=physicalInterface)}"
        if description:
            command = f"{command} description={description}"
        if net_type:
            command = f"{command} type={net_type}"
        if resourceUuid:
            command = f"{command} resourceUuid={resourceUuid}"
        response = self.client.run_command(command)
        return response['stdout']


