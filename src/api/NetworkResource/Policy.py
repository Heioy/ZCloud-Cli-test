#!/usr/bin/env python3
# -*- coding:utf-8 -*- 

from typing import Union, Dict
from logging import Logger
from src.api.client import ZStackClient
from src.config import commands
from src.utils.errors import ParameterIsNoneError


class PolicyRouteRuleSet(ZStackClient):

    def __init__(self, logger: Logger = None):
        super(PolicyRouteRuleSet, self).__init__(logger=logger)

    def createPolicyRouteRuleSet(self, name: str, vRouterUuid: str, description: str = None, rule_type: str = None,
                                 resourceUuid: str = None) -> Union[Dict, str]:
        """
        创建策略路由规则集
        :param name: 资源名称
        :param description: 资源的详细描述
        :param vRouterUuid: 路由器uuid
        :param rule_type: ["User", "EgressWhereComeFrom"]
        :param resourceUuid:
        """
        if not name or not vRouterUuid:
            raise ParameterIsNoneError(name=name, vRouterUuid=vRouterUuid)
        command = f"{self.zstack_cli} {commands.ZStack_Create_PolicyRouteRuleSet.format(name=name, vRouterUuid=vRouterUuid)}"
        if description:
            command = f"{command} description={description}"
        if rule_type:
            command = f"{command} type={rule_type}"
        if resourceUuid:
            command = f"{command} resourceUuid={resourceUuid}"
        response = self.client.run_command(command)
        return response['stdout']

    def deletePolicyRouteRuleSet(self, uuid: str, deleteMode: str = None) -> Union[Dict, str]:
        """
        删除策略路由规则集
        :param uuid: 资源的UUID，唯一标示该资源
        :param deleteMode: 删除模式
        """
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)
        command = f"{self.zstack_cli} {commands.ZStack_Delete_PolicyRouteRuleSet.format(uuid=uuid)}"
        if deleteMode:
            command = f"{command} deleteMode={deleteMode}"
        response = self.client.run_command(command)
        return response['stdout']

    def updatePolicyRouteRuleSet(self, uuid: str, name: str, description: str = None) -> Union[Dict, str]:
        """
        更新策略路由规则集属性
        :param uuid: 资源的UUID，唯一标示该资源
        :param name: 资源名称
        :param description: 资源的详细描述
        """
        if not uuid or not name:
            raise ParameterIsNoneError(uuid=uuid, name=name)
        command = f"{self.zstack_cli} {commands.ZStack_Update_PolicyRouteRuleSet.format(uuid=uuid, name=name)}"
        if description:
            command = f"{command} description={description}"
        response = self.client.run_command(command)
        return response['stdout']

    def queryPolicyRouteRuleSet(self) -> Union[Dict, str]:
        """
        查询策略路由规则集
        """
        command = f"{self.zstack_cli} {commands.ZStack_Query_PolicyRouteRuleSet}"
        response = self.client.run_command(command)
        return response['stdout']

    def queryPolicyRouteRuleSetL3Ref(self) -> Union[Dict, str]:
        """
        查询策略路由规则集网络关联
        """
        command = f"{self.zstack_cli} {commands.ZStack_Query_PolicyRouteRuleSetL3Ref}"
        response = self.client.run_command(command)
        return response['stdout']

    def queryPolicyRouteRuleSetVRouterRef(self) -> Union[Dict, str]:
        """
        查询策略路由规则集与单节点路由器关联
        """
        command = f"{self.zstack_cli} {commands.ZStack_Query_PolicyRouteRuleSetVRouterRef}"
        response = self.client.run_command(command)
        return response['stdout']

    def createPolicyRouteRule(self, ruleSetUuid: str, tableUuid: str, ruleNumber: str, destIp: str = None,
                              sourceIp: str = None, destPort: str = None, sourcePort: str = None, protocol: str = None,
                              resourceUuid: str = None) -> Union[Dict, str]:
        """
        创建策略路由规则集规则
        :param ruleSetUuid: 策略路由规则集uuid
        :param tableUuid: 策略路由表uuid
        :param ruleNumber: 规则优先级
        :param destIp: 目标ip
        :param sourceIp: 源ip
        :param destPort: 目标端口
        :param sourcePort: 源端口
        :param protocol: 协议
        :param resourceUuid:
        """
        if not ruleSetUuid or not tableUuid or not ruleNumber:
            raise ParameterIsNoneError(ruleSetUuid=ruleSetUuid, tableUuid=tableUuid, ruleNumber=ruleNumber)
        command = f"{self.zstack_cli} {commands.ZStack_Create_PolciyRouteRule.format(ruleSetUuid=ruleSetUuid, ruleNumber=ruleNumber, tableUuid=tableUuid)}"
        if destIp:
            command = f"{command} destIp={destIp}"
        if destPort:
            command = f"{command} destPort={destPort}"
        if sourceIp:
            command = f"{command} sourceIp={sourceIp}"
        if sourcePort:
            command = f"{command} sourcePort={sourcePort}"
        if protocol:
            command = f"{command} protocol={protocol}"
        if resourceUuid:
            command = f"{command} resourceUuid={resourceUuid}"
        response = self.client.run_command(command)
        return response['stdout']

    def deletePolicyRouteRule(self, uuid: str, deleteMode: str = None) -> Union[Dict, str]:
        """
        删除策略路由规则集规则
        :param uuid: 资源的UUID，唯一标示该资源
        :param deleteMode: 删除资源模式
        """
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)
        command = f"{self.zstack_cli} {commands.ZStack_Delete_PolciyRouteRule.format(uuid=uuid)}"
        if deleteMode:
            command = f"{command} deleteMode={deleteMode}"
        response = self.client.run_command(command)
        return response['stdout']

    def createPolicyRouteTable(self, vRouterUuid: str, number: str, description: str = None, resourceUuid: str = None) -> Union[Dict, str]:
        """
        创建策略路由表
        :param vRouterUuid: 路由器uuid
        :param number: 表名
        :param description: 资源的详细描述
        :param resourceUuid:
        """
        if not vRouterUuid or not number:
            raise ParameterIsNoneError(vRouterUuid=vRouterUuid, number=number)
        command = f"{self.zstack_cli} {commands.ZStack_Create_PolciyRouteTable.format(vRouterUuid, number)}"
        if description:
            command = f"{command} description={description}"
        if resourceUuid:
            command = f"{command} resourceUuid={resourceUuid}"
        response = self.client.run_command(command)
        return response['stdout']

    def deletePolicyRouteTable(self, uuid: str, deleteMode: str = None) -> Union[Dict, str]:
        """
        删除策略路由表
        :param uuid: 资源的UUID，唯一标示该资源
        :param deleteMode: 删除资源模式
        """
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)
        command = f"{self.zstack_cli} {commands.ZStack_Delete_PolciyRouteTable.format(uuid)}"
        if deleteMode:
            command = f"{command} deleteMode={deleteMode}"
        response = self.client.run_command(command)
        return response['stdout']

    def queryPolicyRouteTable(self) -> Union[Dict, str]:
        """
        查询策略路由表
        """
        command = f"{self.zstack_cli} {commands.ZStack_Query_PolciyRouteTable}"
        response = self.client.run_command(command)
        return response['stdout']

    def queryPolicyRouteTableVRouterRef(self) -> Union[Dict, str]:
        """
        查询策略路由表与单节点路由器关联
        """
        command = f"{self.zstack_cli} {commands.ZStack_Query_PolciyRouteTableVRouterRef}"
        response = self.client.run_command(command)
        return response['stdout']

    def createPolicyRouteTableRouteEntry(self, tableUuid: str, destinationCidr: str, nextHopIp: str, distance: str = None,
                                         resourceUuid: str = None) -> Union[Dict, str]:
        """
        创建策略路由
        :param tableUuid: 策略路由表uuid
        :param destinationCidr: 目标ip cidr
        :param nextHopIp: 下一跳ip
        :param distance: 优先级
        :param resourceUuid:
        """
        if not tableUuid or not destinationCidr or not nextHopIp:
            raise ParameterIsNoneError(tableUuid=tableUuid, destinationCidr=destinationCidr, nextHopIp=nextHopIp)
        command = f"{self.zstack_cli} {commands.ZStack_Create_PolicyRouteTableRouteEntry.format(tableUuid, destinationCidr, nextHopIp)}"
        if distance:
            command = f"{command} distance={distance}"
        if resourceUuid:
            command = f"{command} resourceUuid={resourceUuid}"
        response = self.client.run_command(command)
        return response['stdout']

    def deletePolicyRouteTableRouteEntry(self, uuid: str, deleteMode: str = None) -> Union[Dict, str]:
        """
        删除策略路由
        :param uuid: 资源的UUID，唯一标示该资源
        :param deleteMode:
        """
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)
        command = f"{self.zstack_cli} {commands.ZStack_Delete_PolicyRouteTableRouteEntry.format(uuid)}"
        if deleteMode:
            command = f"{command} deleteMode={deleteMode}"
        response = self.client.run_command(command)
        return response['stdout']

    def queryPolicyRouteTableRouteEntry(self) -> Union[Dict, str]:
        """
        查询策略路由
        """
        command = f"{self.zstack_cli} {commands.ZStack_Query_PolicyRouteTableRouteEntry}"
        response = self.client.run_command(command)
        return response['stdout']

    def queryPolicyRouteRule(self) -> Union[Dict, str]:
        """
        查询策略路由规则
        """
        command = f"{self.zstack_cli} {commands.ZStack_Query_PolicyRouteRule}"
        response = self.client.run_command(command)
        return response['stdout']

    def attachPolicyRouteRuleSetToL3(self, l3Uuid: str, ruleSetUuid: str) -> Union[Dict, str]:
        """
        对网络加载策略路由规则集
        :param l3Uuid: 三层网络uuid
        :param ruleSetUuid: 策略路由规则集uuid
        """
        if not l3Uuid or not ruleSetUuid:
            raise ParameterIsNoneError(l3Uuid=l3Uuid, ruleSetUuid=ruleSetUuid)
        command = f"{self.zstack_cli} {commands.ZStack_Attach_PolicyRouteRuleSet_to_L3.format(l3uuid=l3Uuid, ruleSetUuid=ruleSetUuid)}"
        response = self.client.run_command(command)
        return response['stdout']

    def detachPolicyRouteRuleSetFromL3(self, l3Uuid: str, ruleSetUuid: str) -> Union[Dict, str]:
        """
        对网络解绑策略路由
        :param l3Uuid: 三层网络uuid
        :param ruleSetUuid: 策略规则集uuid
        """
        if not l3Uuid or not ruleSetUuid:
            raise ParameterIsNoneError(l3Uuid=l3Uuid, ruleSetUuid=ruleSetUuid)
        command = f"{self.zstack_cli} {commands.ZStack_Detach_PolicyRouteRuleSet_from_L3.format(l3uuid=l3Uuid, ruleSetUuid=ruleSetUuid)}"
        response = self.client.run_command(command)
        return response['stdout']

    def getPolicyRouteRuleSetFromVirtualRouter(self, vmInstanceUuid: str) -> Union[Dict, str]:
        """
        获取虚拟路由器的策略路由集合
        :param vmInstanceUuid: 云主机UUID
        """
        if not vmInstanceUuid:
            raise ParameterIsNoneError(vmInstanceUuid=vmInstanceUuid)
        command = f"{self.zstack_cli} {commands.ZStack_Get_PolicyRouteRuleSet_from_VirtualRouter.format(vuuid=vmInstanceUuid)}"
        response = self.client.run_command(command)
        return response['stdout']
