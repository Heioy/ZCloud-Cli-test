#!/usr/bin/env python3
# -*- coding:utf-8 -*- 

from typing import Union, Dict
from logging import Logger
from src.api.client import ZStackClient
from src.config import commands
from src.utils.errors import ParameterIsNoneError

"""亲和组资源类"""


class AffinityGroup(ZStackClient):

    def __init__(self, logger: Logger = None):
        super(AffinityGroup, self).__init__(logger=logger)

    def create_affinitygroup(self, name: str, policy: str, description: str = None, afftype: str = None,
                             resourceUuid: str = None) -> Union[Dict, str]:
        """
        创建亲和组
        :param name: 亲和组名称
        :param policy: 亲和组规则 "antiSoft"
        :param description: 亲和组的详细描述
        :param afftype: 亲和组类型。目前支持物理主机亲和，未来将增加网络亲和、路由器亲和、数据中心或机架亲和等多种类型。 "host"
        :param resourceUuid: 资源uuid
        """
        if not name or not policy:
            raise ParameterIsNoneError(name=name, policy=policy)
        command = f"{self.zstack_cli} {commands.ZStack_Create_AffinityGroup.format(name=name, policy=policy)}"
        if description:
            command = f"{command} description={description}"
        if afftype:
            command = f"{command} type={afftype}"
        if resourceUuid:
            command = f"{command} resourceUuid={resourceUuid}"
        response = self.client.run_command(command)
        return response['stdout']

    def delete_affinitygroup(self, uuid: str, deleteMode: str = None) -> Union[Dict, str]:
        """
        删除亲和组
        :param uuid: 亲和组uuid
        :param deleteMode: 删除模式
        """
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)
        command = f"{self.zstack_cli} {commands.ZStack_Delete_AffinityGroup.format(uuid=uuid)}"
        if deleteMode:
            command = f"{command} deleteMode={deleteMode}"
        response = self.client.run_command(command)
        return response['stdout']

    def query_affinitygroup(self, appliance: str = None, resourceUuid: str = None, **kwargs) -> Union[Dict, str]:
        """
        查询亲和组
        :param appliance: 应用名称
        :param resourceUuid: 资源uuid
        :param kwargs:
        """
        command = f"{self.zstack_cli} {commands.ZStack_Query_AffinityGroup}"
        if appliance:
            command = f"{command} appliance={appliance}"
        if resourceUuid:
            command = f"{command} resourceUuid={resourceUuid}"
        if kwargs:
            for key, value in kwargs.items():
                command += f"{key}={value}"
        response = self.client.run_command(command)
        return response['stdout']

    def update_affinitygroup(self, uuid: str, name: str = None, description: str = None) -> Union[Dict, str]:
        """
        更新亲和组
        :param uuid: 亲和组uuid
        :param name: 亲和组名称
        :param description: 亲和组的详细描述
        """
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)
        command = f"{self.zstack_cli} {commands.ZStack_Update_AffinityGroup.format(uuid=uuid)}"
        if name:
            command = f"{command} name={name}"
        if description:
            command = f"{command} description={description}"
        response = self.client.run_command(command)
        return response['stdout']

    def add_vm_to_affinitygroup(self, affinityGroupUuid: str, uuid: str) -> Union[Dict, str]:
        """
        添加云主机到亲和组
        :param affinityGroupUuid: 亲和组uuid
        :param uuid: 资源的uuid
        """
        if not affinityGroupUuid or not uuid:
            raise ParameterIsNoneError(affinityGroupUuid=affinityGroupUuid, uuid=uuid)
        command = f"{self.zstack_cli} {commands.ZStack_Add_Vm_to_AffinityGroup.format(affUuid=affinityGroupUuid, uuid=uuid)}"
        response = self.client.run_command(command)
        return response['stdout']

    def remove_vm_from_affinitygroup(self, affinityGroupUuid: str, uuid: str) -> Union[Dict, str]:
        """
        从亲和组移除云主机
        :param affinityGroupUuid: 亲和组uuid
        :param uuid: 资源的uuid
        """
        if not affinityGroupUuid or not uuid:
            raise ParameterIsNoneError(affinityGroupUuid=affinityGroupUuid, uuid=uuid)
        command = f"{self.zstack_cli} {commands.ZStack_Remove_Vm_from_AffinityGroup.format(affUuid=affinityGroupUuid, uuid=uuid)}"
        response = self.client.run_command(command)
        return response['stdout']

    def change_affinity_state(self, uuid: str, stateEvent: str) -> Union[Dict, str]:
        """
        改变亲和组的使用状态
        :param uuid: 资源的uuid
        :param stateEvent: 资源使用状态 ["disable", "enable"]
        """
        if not uuid or not stateEvent:
            raise ParameterIsNoneError(uuid=uuid, stateEvent=stateEvent)
        command = f"{self.zstack_cli} {commands.ZStack_Change_AffinityGroup_State.format(uuid=uuid, state=stateEvent)}"
        response = self.client.run_command(command)
        return response['stdout']

    def get_candidate_affinitygroup_for_attaching_vm(self, vmUuid: str) -> Union[Dict, str]:
        """
        获取可绑定云主机的亲和组
        :param vmUuid: 云主机UUID
        """
        if not vmUuid:
            raise ParameterIsNoneError(vmUuid=vmUuid)
        command = f"{self.zstack_cli} {commands.ZStack_Get_Candidate_AffinityGroup_for_Attaching_Vm.format(vuuid=vmUuid)}"
        response = self.client.run_command(command)
        return response['stdout']

    def get_candidate_vm_for_attaching_affinitygroup(self, affinityGroupUuid: str) -> Union[Dict, str]:
        """
        获取可绑定亲和组的云主机
        :param affinityGroupUuid: 亲和组uuid
        """
        if not affinityGroupUuid:
            raise ParameterIsNoneError(affinityGroupUuid=affinityGroupUuid)
        command = f"{self.zstack_cli} {commands.ZStack_Get_Candidate_VM_for_Attaching_AffinityGroup.format(affUuid=affinityGroupUuid)}"
        response = self.client.run_command(command)
        return response['stdout']

    def get_candidate_affinitygroup_for_creating_vm(self, zoneUuid: str, clusterUuid: str = None,
                                                    hostUuid: str = None) -> Union[Dict, str]:
        """
        在创建云主机时获取当前状态下可加入的非亲和组
        :param zoneUuid: 区域UUID
        :param clusterUuid: 集群UUID
        :param hostUuid: 物理机UUID
        """
        if not zoneUuid:
            raise ParameterIsNoneError(zoneUuid=zoneUuid)
        command = f"{self.zstack_cli} {commands.ZStack_Get_Candidate_AffinityGroup_for_Creating_Vm.format(zoneUuid=zoneUuid)}"
        if clusterUuid:
            command = f"{command} clusterUuid={clusterUuid}"
        if hostUuid:
            command = f"{command} hostUuid={hostUuid}"
        response = self.client.run_command(command)
        return response['stdout']
