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

    def create_L2VlanNetwork(self, vlan: str, name: str, zoneUuid: str, physicalInterface: str, description: str = None,
                             net_type: str = None, resourceUuid: str = None) -> Union[Dict, str]:
        """
        创建二层VLAN网络
        :param vlan:
        :param name: 二层Vlan网络名称
        :param zoneUuid: 区域uuid
        :param physicalInterface: 物理网卡
        :param description: 二层Vlan网络的详细描述
        :param net_type: 网络类型
        :param resourceUuid: 资源uuid
        """
        if not name or not zoneUuid or not physicalInterface or not vlan:
            raise ParameterIsNoneError(name=name, zoneUuid=zoneUuid, physicalInterface=physicalInterface)
        command = f"{self.zstack_cli} {commands.ZStack_Create_L2_Vlan_Network.format(name=name, zoneUuid=zoneUuid, physicalInterface=physicalInterface, vlan=vni)}"
        if description:
            command = f"{command} description={description}"
        if net_type:
            command = f"{command} type={net_type}"
        if resourceUuid:
            command = f"{command} resourceUuid={resourceUuid}"
        response = self.client.run_command(command)
        return response['stdout']

    def query_L2VlanNetwork(self, physicalInterface: str = None, zoneUuid: str = None) -> Union[Dict, str]:
        """
        查询二层VLAN网络
        :param physicalInterface:
        :param zoneUuid:
        """
        command = f"{self.zstack_cli} {commands.ZStack_Query_L2_Vlan_Network}"
        if physicalInterface:
            command = f"{command} physicalInterface={physicalInterface}"
        if zoneUuid:
            command = f"{command} zone.cluster.zoneUuid={zoneUuid}"
        response = self.client.run_command(command)
        return response['stdout']

    def delete_L2Network(self, uuid: str, deleteMode: str = None) -> Union[Dict, str]:
        """
        删除二层网络
        :param uuid: 二层网络uuid
        :param deleteMode: 资源删除模式
        """
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)
        command = f"{self.zstack_cli} {commands.ZStack_Delete_L2_Network.format(uuid=uuid)}"
        if deleteMode:
            command = f"{command} deleteMode={deleteMode}"
        response = self.client.run_command(command)
        return response['stdout']

    def query_L2Network(self, physicalInterface: str = None, startIp: str = None) -> Union[Dict, str]:
        """
        查询二层网络
        :param physicalInterface:
        :param startIp:
        """
        command = f"{self.zstack_cli} {commands.ZStack_Query_L2_Network}"
        if physicalInterface:
            command = f"{command} physicalInterface={physicalInterface}"
        if startIp:
            command = f"{command} l3Network.ipRanges.startIp=1={startIp}"
        response = self.client.run_command(command)
        return response['stdout']

    def update_L2Network(self, uuid: str, name: str = None, description: str = None) -> Union[Dict, str]:
        """
        更新二层网络
        :param uuid: 二层网络uuid
        :param name: 普通二层网络名称
        :param description: 普通二层网络的详细描述
        """
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)
        command = f"{self.zstack_cli} {commands.ZStack_Update_L2_Network.format(uuid=uuid)}"
        if name:
            command = f"{command} name={name}"
        if description:
            command = f"{command} description={description}"
        response = self.client.run_command(command)
        return response['stdout']

    def get_L2NetworkTypes(self) -> Union[Dict, str]:
        """
        获取二层网络类型
        """
        command = f"{self.zstack_cli} {commands.ZStack_Get_L2_Network_Types}"
        response = self.client.run_command(command)
        return response['stdout']

    def attach_L2Network_to_Cluster(self, l2NetworkUuid: str, clusterUuid: str) -> Union[Dict, str]:
        """
        挂载二层网络到集群
        :param l2NetworkUuid: 二层网络uuid
        :param clusterUuid: 集群uuid
        """
        if not l2NetworkUuid or not clusterUuid:
            raise ParameterIsNoneError(l2NetworkUuid=l2NetworkUuid, clusterUuid=clusterUuid)
        command = f"{self.zstack_cli} {commands.ZStack_Attach_L2_Network_2_Cluster.format(l2uuid=l2NetworkUuid, clusterUuid=clusterUuid)}"
        response = self.client.run_command(command)
        return response['stdout']

    def detach_L2Network_from_Cluster(self, l2NetworkUuid: str, clusterUuid: str) -> Union[Dict, str]:
        """
        从集群上卸载二层网络
        :param l2NetworkUuid: 二层网络uuid
        :param clusterUuid: 集群uuid
        """
        if not l2NetworkUuid or not clusterUuid:
            raise ParameterIsNoneError(l2NetworkUuid=l2NetworkUuid, clusterUuid=clusterUuid)
        command = f"{self.zstack_cli} {commands.ZStack_Detach_L2_Network_From_Cluster.format(l2uuid=l2NetworkUuid, clusterUuid=clusterUuid)}"
        response = self.client.run_command(command)
        return response['stdout']

    def create_vni_range(self, name: str, startVni: str, endVni: str, l2NetworkUuid: str, description: str = None,
                        resourceUuid: str = None) -> Union[Dict, str]:
        """
        创建VNI Range
        :param name: VNI Range名称
        :param startVni:
        :param endVni:
        :param l2NetworkUuid: Vxlan网络资源池uuid
        :param description: VNI Range的详细描述
        :param resourceUuid: 资源uuid。若指定，镜像会使用该字段值作为uuid
        """
        if not name or not startVni or not endVni or not l2NetworkUuid:
            raise ParameterIsNoneError(name=name, startVni=startVni, endVni=endVni, l2NetworkUuid=l2NetworkUuid)
        command = f"{self.zstack_cli} {commands.ZStack_Create_Vni_Range.format(name=name, startVni=startVni, endVni=endVni, l2uuid=l2NetworkUuid)}"
        if description:
            command = f"{command} description={description}"
        if resourceUuid:
            command = f"{command} resourceUuid={resourceUuid}"
        response = self.client.run_command(command)
        return response['stdout']

    def query_vni_range(self) -> Union[Dict, str]:
        """
        查询VNI Range
        """
        command = f"{self.zstack_cli} {commands.ZStack_Query_Vni_Range}"
        response = self.client.run_command(command)
        return response['stdout']

    def delete_vni_range(self, uuid: str, deleteMode: str = None) -> Union[Dict,str]:
        """
        删除VNI Range
        :param uuid: VNI Range uuid
        :param deleteMode: 资源删除模式
        """
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)
        command = f"{self.zstack_cli} {commands.ZStack_Delete_Vni_Range.format(uuid=uuid)}"
        if deleteMode:
            command = f"{command} deleteMode={deleteMode}"
        response = self.client.run_command(command)
        return response['stdout']

    def update_vni_range(self, uuid: str, name: str) -> Union[Dict, str]:
        """
        修改VNI Range
        :param uuid: Vni Range uuid
        :param name: Vni Range 名称
        """
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)
        command = f"{self.zstack_cli} {commands.ZStack_Update_Vni_Range.format(uuid=uuid)}"
        if name:
            command = f"{command} name={name}"
        response = self.client.run_command(command)
        return response['stdout']
