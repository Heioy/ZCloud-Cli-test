#!/usr/bin/env python3
# -*- coding:utf-8 -*- 

from typing import Union, Dict
from logging import Logger
from src.api.client import ZStackClient
from src.config import commands
from src.utils.errors import ParameterIsNoneError


class VirtualRouter(ZStackClient):

    def __init__(self, logger: Logger = None):
        super(VirtualRouter, self).__init__(logger=logger)

    def query_virtualRouter_vm(self, uuid: str = None, hostUuid: str = None) -> Union[Dict, str]:
        """
        查询路由器
        :param uuid:
        :param hostUuid:
        """
        command = f"{self.zstack_cli} {commands.ZStack_Query_VirtualRouter}"
        if uuid:
            command = f"{command} uuid={uuid}"
        if hostUuid:
            command = f"{command} host.uuid={hostUuid}"
        response = self.client.run_command(command)
        return response['stdout']

    def reconnect_virtualRouter(self, vmInstanceUuid: str) -> Union[Dict, str]:
        """
        重连路由器
        :param vmInstanceUuid: 路由器设备uuid
        """
        if not vmInstanceUuid:
            raise ParameterIsNoneError(vmInstanceUuid=vmInstanceUuid)
        command = f"{self.zstack_cli} {commands.ZStack_Reconnect_VirtualRouter.format(vuuid=vmInstanceUuid)}"
        response = self.client.run_command(command)
        return response['stdout']

    def create_virtualRouter_offering(self, managementNetworkUuid: str, zoneUuid: str, imageUuid: str, name: str,
                                      memorySize: str, cpuNum: str, publicNetworkUuid: str = None, isDefault: str = None,
                                      description: str = None, allocatorStrategy: str = None, sortKey: str = None,
                                      offering_type: str = None, resourceUuid: str = None) -> Union[Dict, str]:
        """
        创建路由器规格
        :param managementNetworkUuid: 管理L3网络uuid
        :param zoneUuid: 区域uuid
        :param imageUuid: 镜像uuid
        :param name: 资源名称
        :param memorySize: 内存大小
        :param cpuNum: CPU数量
        :param publicNetworkUuid: 公有L3网络uuid
        :param isDefault: 默认
        :param description: 资源的详细描述
        :param allocatorStrategy: 分配策略 ["DefaultHostAllocatorStrategy", "LastHostPreferredAllocatorStrategy", "LeastVmPreferredHostAllocatorStrategy",
                                           "MinimumCPUUsageHostAllocatorStrategy", "MinimumMemoryUsageHostAllocatorStrategy",
                                           "MaxInstancePerHostHostAllocatorStrategy", "DesignatedHostAllocatorStrategy"]
        :param sortKey: 排序主键
        :param offering_type: 类型 ["UserVm", "ApplianceVm"]
        :param resourceUuid: 资源uuid
        """
        if not managementNetworkUuid or not zoneUuid or not imageUuid or not name or not memorySize or not cpuNum:
            raise ParameterIsNoneError(managementNetworkUuid=managementNetworkUuid, zoneUuid=zoneUuid, imageUuid=imageUuid,
                                       name=name, memorySize=memorySize, cpuNum=cpuNum)
        command = f"{self.zstack_cli} {commands.ZStack_Create_VirtualRouter_Offering.format(name=name, zoneUuid=zoneUuid, netUuid=managementNetworkUuid, iuuid=imageUuid, memorySize=memorySize, cpuNum=cpuNum)}"
        if publicNetworkUuid:
            command = f"{command} publicNetworkUuid={publicNetworkUuid}"
        if isDefault:
            command = f"{command} isDefault={isDefault}"
        if description:
            command = f"{command} description={description}"
        if allocatorStrategy:
            command = f"{command} allocatorStrategy={allocatorStrategy}"
        if offering_type:
            command = f"{command} type={offering_type}"
        if resourceUuid:
            command = f"{command} resourceUuid={resourceUuid}"
        response = self.client.run_command(command)
        return response['stdout']

    def query_virtualRouter_offering(self, imageUuid: str = None, L3NetworkUuid: str = None) -> Union[Dict, str]:
        """
        查询路由器规格
        :param imageUuid:
        :param L3NetworkUuid:
        """
        command = f"{self.zstack_cli} {commands.ZStack_Query_VirtualRouter_Offering}"
        if imageUuid:
            command = f"{command} imageUuid={imageUuid}"
        if L3NetworkUuid:
            command = f"{command} managementL3Network.uuid=={L3NetworkUuid}"
        response = self.client.run_command(command)
        return response['stdout']

    def update_virtualRouter_offering(self, uuid: str, name: str, isDefault: str = None, imageUuid: str = None,
                                      description: str = None, allocatorStrategy: str = None) -> Union[Dict, str]:
        """
        更新路由器规格
        :param uuid: 资源的UUID，唯一标示该资源
        :param name: 资源名称
        :param isDefault: 默认
        :param imageUuid: 镜像UUID
        :param description: 资源的详细描述
        :param allocatorStrategy: 分配策略 ["DefaultHostAllocatorStrategy", "LastHostPreferredAllocatorStrategy", "LeastVmPreferredHostAllocatorStrategy",
                                           "MinimumCPUUsageHostAllocatorStrategy", "MinimumMemoryUsageHostAllocatorStrategy",
                                           "MaxInstancePerHostHostAllocatorStrategy", "DesignatedHostAllocatorStrategy"]
        """
        if not uuid or not name:
            raise ParameterIsNoneError(uuid=uuid, name=name)
        command = f"{self.zstack_cli} {commands.ZStack_Update_VirtualRouter_Offering.format(uuid=uuid, name=name)}"
        if isDefault:
            command = f"{command} isDefault={isDefault}"
        if imageUuid:
            command = f"{command} imageUuid={imageUuid}"
        if description:
            command = f"{command} description={description}"
        if allocatorStrategy:
            command = f"{command} allocatorStrategy={allocatorStrategy}"
        response = self.client.run_command(command)
        return response['stdout']

    def query_applicance_vm(self, uuid: str = None, vmInstanceUuid: str = None) -> Union[Dict, str]:
        """
        查询路由器设备
        :param uuid:
        :param vmInstanceUuid:
        """
        command = f"{self.zstack_cli} {commands.ZStack_Query_Applicance_VM}"
        if uuid:
            command = f"{command} uuid={uuid}"
        if vmInstanceUuid:
            command = f"{command} vmNics.vmInstanceUuid={vmInstanceUuid}"
        response = self.client.run_command(command)
        return response['stdout']

    def get_attachable_public_l3_for_vRouter(self, vmInstanceUuid: str) -> Union[Dict, str]:
        """
        获取路由器可加载的公有网络和系统网络，将自动排除地址冲突的网络
        :param vmInstanceUuid: 路由器设备uuid
        """
        if not vmInstanceUuid:
            raise ParameterIsNoneError(vmInstanceUuid=vmInstanceUuid)
        command = f"{self.zstack_cli} {commands.ZStack_Get_Attachable_Public_L3_for_VRouter.format(vuuid=vmInstanceUuid)}"
        response = self.client.run_command(command)
        return response['stdout']

    # 路由器路由表
    def createVRouterRouteTable(self, name: str, description :str = None, resourceUuid: str = None) -> Union[Dict, str]:
        """
        创建路由器路由表
        :param name: 资源名称
        :param description: 资源的详细描述
        :param resourceUuid: 资源uuid
        """
        if not name:
            raise ParameterIsNoneError(name=name)
        command = f"{self.zstack_cli} {commands.ZStack_Create_VRouterRoute_Table.format(name=name)}"
        if description:
            command = f"{command} description={description}"
        if resourceUuid:
            command = f"{command} resourceUuid={resourceUuid}"
        response = self.client.run_command(command)
        return response['stdout']

    def deleteVRouterRouteTable(self, uuid: str, deleteMode: str = None) -> Union[Dict, str]:
        """
        删除路由器路由表
        :param uuid: 路由器路由表uuid
        :param deleteMode: 资源删除模式 ["Permissive", "Enforcing"]
        """
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)
        command = f"{self.zstack_cli} {commands.ZStack_Delete_VRouterRoute_Table.format(uuid=uuid)}"
        if deleteMode:
            command = f"{command} deleteMode={deleteMode}"
        response = self.client.run_command(command)
        return response['stdout']

    def queryVRouterRouteTable(self, uuid: str = None, virtualRouterVmUuid: str = None) -> Union[Dict, str]:
        """
        查询路由器路由表
        :param uuid:
        :param virtualRouterVmUuid:
        """
        command = f"{self.zstack_cli} {commands.ZStack_Query_VRouterRoute_Table}"
        if uuid:
            command = f"{command} uuid={uuid}"
        if virtualRouterVmUuid:
            command = f"{command} attachedRouterRef.virtualRouterVmUuid={virtualRouterVmUuid}"
        response = self.client.run_command(command)
        return response['stdout']

    def getVRouterRouteTable(self, virtualRouterVmUuid: str) -> Union[Dict, str]:
        """
        获取路由器实时路由表
        :param virtualRouterVmUuid: 路由器设备uuid
        """
        if not virtualRouterVmUuid:
            raise ParameterIsNoneError(virtualRouterVmUuid=virtualRouterVmUuid)
        command = f"{self.zstack_cli} {commands.ZStack_Get_VRouterRoute_Table.format(virtualRouterVmUuid=virtualRouterVmUuid)}"
        response = self.client.run_command(command)
        return response['stdout']

    def addVRouterRouteEntry(self, routeTableUuid: str, destination: str, description: str = None, route_type: str = None,
                             target: str = None, distance: str = None, resourceUuid: str = None) -> Union[Dict, str]:
        """
        添加路由器路由条目
        :param routeTableUuid: 路由器路由表uuid
        :param destination: 目标网络地址，使用网络地址CIDR格式，如果用户填写的不是标准CIDR格式，系统会自动转换
        :param description: 资源的详细描述
        :param route_type: 类型，允许用户添加“静态路由”、“黑洞路由”两种类型，系统会根据是否填下一条地址自动判断类型 ["UserStatic", "UserBlackhole"]
        :param target: 下一条地址，为一个路由器设备目前可以直接到达的IP地址，如果不可以直接到达，将会进行递归路由
        :param distance: 路由优先级，在最小匹配下如果有多条路由规则匹配，优先级数字小的规则将会被匹配
        :param resourceUuid: 资源uuid
        """
        if not routeTableUuid or not destination:
            raise ParameterIsNoneError(routeTableUuid=routeTableUuid, destination=destination)
        command = f"{self.zstack_cli} {commands.ZStack_Add_VRouterRoute_Entry.format(routeUuid=routeTableUuid, destination=destination)}"
        if description:
            command = f"{command} description={description}"
        if route_type:
            command = f"{command} type={route_type}"
        if target:
            command = f"{command} target={target}"
        if distance:
            command = f"{command} distance={distance}"
        if resourceUuid:
            command = f"{command} resourceUuid={resourceUuid}"
        response = self.client.run_command(command)
        return response['stdout']

    def deleteVRouterRouteEntry(self, uuid: str, routeTableUuid: str, deleteMode: str = None) -> Union[Dict, str]:
        """
        删除路由器路由条目
        :param uuid: 路由器路由条目uuid
        :param routeTableUuid: 路由器路由表uuid
        :param deleteMode: 资源删除模式 ["Permissive", "Enforcing"]
        """
        if not uuid or not routeTableUuid:
            raise ParameterIsNoneError(uuid=uuid, routeTableUuid=routeTableUuid)
        command = f"{self.zstack_cli} {commands.ZStack_Delete_VRouterRoute_Entry.format(uuid=uuid, routeUuid=routeTableUuid)}"
        if deleteMode:
            command = f"{command} deleteMode={deleteMode}"
        response = self.client.run_command(command)
        return response['stdout']

    def queryVRouterRouteEntry(self, uuid: str = None, vrouterRouteTableUuid: str = None) -> Union[Dict, str]:
        """
        查询路由器路由条目
        :param uuid:
        :param vrouterRouteTableUuid:
        """
        command = f"{self.zstack_cli} {commands.ZStack_Query_VRouterRoute_Entry}"
        if uuid:
            command = f"{command} uuid={uuid}"
        if vrouterRouteTableUuid:
            command = f"{command} vrouterRouteTable.uuid={vrouterRouteTableUuid}"
        response = self.client.run_command(command)
        return response['stdout']

    def attachVRouterRouteEntrytoRouter(self, routeTableUuid: str, virtualRouterVmUuid: str) -> Union[Dict, str]:
        """
        绑定路由表到路由器设备
        :param routeTableUuid: 路由表uuid
        :param virtualRouterVmUuid: 路由器设备uuid
        """
        if not routeTableUuid or not virtualRouterVmUuid:
            raise ParameterIsNoneError(routeTableUuid=routeTableUuid, virtualRouterVmUuid=virtualRouterVmUuid)
        command = f"{self.zstack_cli} {commands.ZStack_Attach_VRouterRoute_Entry_to_Router.format(routeUuid=routeTableUuid, vrouteUuid=virtualRouterVmUuid)}"
        response = self.client.run_command(command)
        return response['stdout']

    def detachVRouterRouteEntryfromVRouter(self, routeTableUuid: str, virtualRouterVmUuid: str) -> Union[Dict, str]:
        """
        解绑路由器路由表
        :param routeTableUuid: 路由器路由表uuid
        :param virtualRouterVmUuid: 路由器设备uuid
        """
        if not routeTableUuid or not virtualRouterVmUuid:
            raise ParameterIsNoneError(routeTableUuid=routeTableUuid, virtualRouterVmUuid=virtualRouterVmUuid)
        command = f"{self.zstack_cli} {commands.ZStack_Detach_VRouterRoute_Entry_from_VRouter.format(routeUuid=routeTableUuid, vrouteUuid=virtualRouterVmUuid)}"
        response = self.client.run_command(command)
        return response['stdout']

    def queryVirtualRouterVRouterRouteTableRef(self, routeTableUuid: str = None, vrouterRouteTableUuid: str = None) -> Union[Dict, str]:
        """
        f查询绑定关系
        :param routeTableUuid:
        :param vrouterRouteTableUuid:
        """
        command = f"{self.zstack_cli} {commands.ZStack_Query_VirtualRouter_VRouterRoute_Table_Ref}"
        if routeTableUuid:
            command = f"{command} routeTableUuid={routeTableUuid}"
        if vrouterRouteTableUuid:
            command = f"{command} vrouterRouteTable.uuid={vrouterRouteTableUuid}"
        response = self.client.run_command(command)
        return response['stdout']
