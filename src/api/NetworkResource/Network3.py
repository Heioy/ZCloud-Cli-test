#!/usr/bin/env python3
# -*- coding:utf-8 -*- 

from typing import Union, Dict
from logging import Logger
from src.api.client import ZStackClient
from src.config import commands
from src.utils.errors import ParameterIsNoneError


class L3Network(ZStackClient):

    def __init__(self, logger: Logger = None):
        super(L3Network, self).__init__(logger=logger)

    def create_l3Network(self, name: str, l2NetworkUuid: str, description: str = None, net_type: str = None,
                         system: str = None, dnsDomain: str = None, resourceUuid: str = None, category: str = None) -> Union[Dict, str]:
        """
        创建三层网络
        :param name: 三层网络名称
        :param l2NetworkUuid: 二层网络uuid
        :param description: 三层网络的详细描述
        :param net_type: 三层网络类型
        :param system: 是否用于系统云主机
        :param dnsDomain: DNS域
        :param resourceUuid: 资源uuid。若指定，三层网络会使用该字段值作为uuid
        :param category: 网络类型，需要与system标签搭配使用，system为true时可设置为Pubic、Private ["Public", "Private", "System"]
        """
        if not name or not l2NetworkUuid:
            raise ParameterIsNoneError(name=name, l2NetworkUuid=l2NetworkUuid)
        command = f"{self.zstack_cli} {commands.ZStack_Create_L3_Network.format(name=name, l2uuid=l2NetworkUuid)}"
        if description:
            command = f"{command} description={description}"
        if net_type:
            command = f"{command} type={net_type}"
        if system:
            command = f"{command} system={system}"
        if dnsDomain:
            command = f"{command} dnsDomain={dnsDomain}"
        if resourceUuid:
            command = f"{command} resourceUuid={resourceUuid}"
        if category:
            command = f"{command} category={category}"
        response = self.client.run_command(command)
        return response['stdout']

    def delete_l3Network(self, uuid: str, deleteMode: str = None) -> Union[Dict, str]:
        """
        删除三层网络
        :param uuid: 三层网络uuid
        :param deleteMode: 删除资源 ["Permissive", "Enforcing"]
        """
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)
        command = f"{self.zstack_cli} {commands.ZStack_Delete_L3_Network.format(uuid=uuid)}"
        if deleteMode:
            command = f"{command} deleteMode={deleteMode}"
        response = self.client.run_command(command)
        return response['stdout']

    def query_l3Network(self, uuid: str = None, l3NetworkUuid: str = None) -> Union[Dict, str]:
        """
        查询三层网络
        :param uuid:
        :param l3NetworkUuid:
        """
        command = f"{self.zstack_cli} {commands.ZStack_Query_L3_Network}"
        if uuid:
            command = f"{command} uuid={uuid}"
        if l3NetworkUuid:
            command = f"{command} vmNic.l3NetworkUuid={l3NetworkUuid}"
        response = self.client.run_command(command)
        return response['stdout']

    def update_l3Network(self, uuid: str, name: str, description: str = None, system: str = None, dnsDomain: str = None,
                         category: str = None) -> Union[Dict, str]:
        """
        更新三层网络
        :param uuid: 三层网络uuid
        :param name: 三层网络名称
        :param description: 三层网络的详细描述
        :param system: 是否用于系统云主机
        :param dnsDomain: DNS域
        :param category: 网络类型，需要与system标签搭配使用，system为true时可设置为Pubic、Private
        """
        if not uuid or not name:
            raise ParameterIsNoneError(uuid=uuid, name=name)
        command = f"{self.zstack_cli} {commands.ZStack_Update_L3_Network.format(name=name, uuid=uuid)}"
        if description:
            command = f"{command} description={description}"
        if system:
            command = f"{command} system={system}"
        if dnsDomain:
            command = f"{command} dnsDomain={dnsDomain}"
        if category:
            command = f"{command} category={category}"
        response = self.client.run_command(command)
        return response['stdout']

    def get_l3Netwotk_types(self) -> Union[Dict, str]:
        """
        获取三层网络类型
        """
        command = f"{self.zstack_cli} {commands.ZStack_Get_L3_Network_Types}"
        response = self.client.run_command(command)
        return response['stdout']

    def change_l3Network_state(self, uuid: str, stateEvent: str) -> Union[Dict, str]:
        """
        改变三层网络状态
        :param uuid: 三层网络uuid
        :param stateEvent: 状态
        """
        if not uuid or not stateEvent:
            raise ParameterIsNoneError(uuid=uuid, stateEvent=stateEvent)
        command = f"{self.zstack_cli} {commands.ZStack_Change_L3_Network_State.format(state=stateEvent, uuid=uuid)}"
        response = self.client.run_command(command)
        return response['stdout']

    def get_l3Network_dhcpIpAddress(self, l3NetworkUuid: str) -> Union[Dict, str]:
        """
        获取网络DHCP服务所用地址
        :param l3NetworkUuid: 三层网络uuid
        """
        if not l3NetworkUuid:
            raise ParameterIsNoneError(l3NetworkUuid=l3NetworkUuid)
        command = f"{self.zstack_cli} {commands.ZStack_Get_L3_Network_DHCP.format(l3uuid=l3NetworkUuid)}"
        response = self.client.run_command(command)
        return response['stdout']

    def remove_dns_from_l3Network(self, l3NetworkUuid: str, dns: str) -> Union[Dict, str]:
        """
        从三层网络移除DNS
        :param l3NetworkUuid: 三层网络uuid
        :param dns: DNS地址
        """
        if not l3NetworkUuid or not dns:
            raise ParameterIsNoneError(l3NetworkUuid=l3NetworkUuid, dns=dns)
        command = f"{self.zstack_cli} {commands.ZStack_Remove_Dns_To_L3_Network.format(dns=dns, l3uuid=l3NetworkUuid)}"
        response = self.client.run_command(command)
        return response['stdout']

    def add_dns_to_l3Network(self, l3NetworkUuid: str, dns: str) -> Union[Dict, str]:
        """
        向三层网络添加DNS
        :param l3NetworkUuid: 三层网络uuid
        :param dns: DNS地址
        """
        if not l3NetworkUuid or not dns:
            raise ParameterIsNoneError(l3NetworkUuid=l3NetworkUuid, dns=dns)
        command = f"{self.zstack_cli} {commands.ZStack_Add_Dns_To_L3_Network.format(dns=dns, l3uuid=l3NetworkUuid)}"
        response = self.client.run_command(command)
        return response['stdout']

    def add_host_route_tol3Network(self, l3NetworkUuid: str, nexthop: str, prefix: str) -> Union[Dict, str]:
        """
        向三层网络添加主机路由
        :param l3NetworkUuid: 三层网络uuid
        :param nexthop:
        :param prefix:
        """
        if not l3NetworkUuid or not nexthop or not prefix:
            raise ParameterIsNoneError(l3NetworkUuid=l3NetworkUuid, nexthop=nexthop, prefix=prefix)
        command = f"{self.zstack_cli} {commands.ZSatck_Add_HostRouter_to_L3_Network.format(l3uuid=l3NetworkUuid, ip=nexthop, prefix=prefix)}"
        response = self.client.run_command(command)
        return response['stdout']

    def remove_host_router_from_l3Network(self, l3NetworkUuid: str, prefix: str) -> Union[Dict, str]:
        """
        从三层网络移除主机路由
        :param l3NetworkUuid: 三层网络uuid
        :param prefix:
        """
        if not l3NetworkUuid or not prefix:
            raise ParameterIsNoneError(l3NetworkUuid=l3NetworkUuid, prefix=prefix)
        command = f"{self.zstack_cli} {commands.ZStack_Remove_HostRouter_From_L3_Network.format(l3uuid=l3NetworkUuid, prefix=prefix)}"
        response = self.client.run_command(command)
        return response['stdout']

    def get_free_ip(self, l3NetworkUuid: str = None, ipRangeUuid: str = None, start: str = None, ipRangeType: str = None,
                    ipVersion: str = None, limit: str = None) -> Union[Dict, str]:
        """
        获取空闲IP
        :param l3NetworkUuid: 三层网络uuid，l3NetworkUuid和ipRangeUuid二选一
        :param ipRangeUuid: IP段uuid，l3NetworkUuid和ipRangeUuid二选一
        :param start: 起始值
        :param ipRangeType: 地址类型 ["Normal", "AddressPool"]
        :param ipVersion: IP地址版本号 ["4", "6"]
        :param limit: 数量限制
        """
        if not l3NetworkUuid and not ipRangeUuid:
            raise ParameterIsNoneError(l3NetworkUuid=l3NetworkUuid, ipRangeUuid=ipRangeUuid)
        command = f"{self.zstack_cli} {commands.ZStack_Get_Free_IP}"
        if l3NetworkUuid:
            command = f"{command} l3NetworkUuid={l3NetworkUuid}"
        if ipRangeUuid:
            command = f"{command} ipRangeUuid={ipRangeUuid}"
        if start:
            command = f"{command} start={start}"
        if ipRangeType:
            command = f"{command} ipRangeType={ipRangeType}"
        if ipVersion:
            command = f"{command} ipVersion={ipVersion}"
        if limit:
            command = f"{command} limit={limit}"
        response = self.client.run_command(command)
        return response['stdout']

    def check_ip_availability(self, l3NetworkUuid: str, ip: str) -> Union[Dict, str]:
        """
        检查IP可用性
        :param l3NetworkUuid: 三层网络uuid
        :param ip: IP地址
        """
        if not l3NetworkUuid or not ip:
            raise ParameterIsNoneError(l3NetworkUuid=l3NetworkUuid, ip=ip)
        command = f"{self.zstack_cli} {commands.ZStack_Check_IP_Availability.format(ip=ip, l3uuid=l3NetworkUuid)}"
        response = self.client.run_command(command)
        return response['stdout']

    def get_ipAddress_capacity(self, zoneUuids: str = None, l3NetworkUuids: str = None, ipRangeUuids: str = None,
                               _all: str = None) -> Union[Dict, str]:
        """
        获取IP网络地址容量
        :param zoneUuids: 区域uuid
        :param l3NetworkUuids: 三层网络uuid
        :param ipRangeUuids: IP地址范围uuid。ipRangeUuids，L3NetworkUuids，zoneUuids至少一个不是为空列表，或者全部不为空
        :param _all: 系统全局
        """
        if not ipRangeUuids and not zoneUuids and not l3NetworkUuids:
            raise ParameterIsNoneError(ipRangeUuids=ipRangeUuids, zoneUuids=zoneUuids, l3NetworkUuids=l3NetworkUuids)
        command = f"{self.zstack_cli} {commands.ZStack_Get_IPAddress_Capacity}"
        if zoneUuids:
            command = f"{command} zoneUuids={zoneUuids}"
        if l3NetworkUuids:
            command = f"{command} l3NetworkUuids={l3NetworkUuids}"
        if ipRangeUuids:
            command = f"{command} ipRangeUuids={ipRangeUuids}"
        response = self.client.run_command(command)
        return response['stdout']
