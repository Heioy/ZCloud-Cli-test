#!/usr/bin/env python3
# -*- coding:utf-8 -*- 

from typing import Union, Dict
from logging import Logger
from src.api.client import ZStackClient
from src.config import commands
from src.utils.errors import ParameterIsNoneError

"""云主机快照组类"""


class SnapShot(ZStackClient):

    def __init__(self, logger: Logger = None):
        super(SnapShot, self).__init__(logger=logger)

    def create_volume_snapshot_group(self, rootVolumeUuid: str, name: str, description: str = None,
                                     resourceUuid: str = None, tagUuids: str = None) -> Union[Dict, str]:
        """
        创建快照组
        :param rootVolumeUuid: 根云盘UUID
        :param name: 资源名称
        :param description: 资源的详细描述
        :param resourceUuid: 资源的uuid
        :param tagUuids: 标签UUID列表
        """
        if not rootVolumeUuid or not name:
            raise ParameterIsNoneError(rootVolumeUuid=rootVolumeUuid, name=name)
        command = f"{self.zstack_cli} {commands.ZStack_Create_SnapshotGroup.format(name=name, voluuid=rootVolumeUuid)}"
        if description:
            command = f"{command} description={description}"
        if resourceUuid:
            command = f"{command} resourceUuid={resourceUuid}"
        if tagUuids:
            command = f"{command} tagUuids={tagUuids}"
        response = self.client.run_command(command)
        return response['stdout']

    def delete_volume_snapshot_group(self, uuid: str, deleteMode: str = None) -> Union[Dict, str]:
        """
        删除快照组
        :param uuid: 资源的UUID，唯一标示该资源
        :param deleteMode: 删除模式 ["Permissive", "Enforcing"]
        """
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)
        command = f"{self.zstack_cli} {commands.ZStack_Delete_SnapshotGroup.format(uuid=uuid)}"
        if deleteMode:
            command = f"{command} deleteMode={deleteMode}"
        response = self.client.run_command(command)
        return response['stdout']

    def update_volume_snapshot_group(self, uuid: str, name: str, description: str = None) -> Union[Dict, str]:
        """
        更新快照组信息
        :param uuid: 资源的UUID，唯一标示该资源
        :param name: 资源名称
        :param description: 资源的详细描述
        """
        if not uuid or not name:
            raise ParameterIsNoneError(uuid=uuid, name=name)
        command = f"{self.zstack_cli} {commands.ZStack_Update_SnapshotGroup.format(uuid=uuid, name=name)}"
        if description:
            command = f"{command} description={description}"
        response = self.client.run_command(command)
        return response['stdout']

    def query_volume_snapshot_group(self, **kwargs) -> Union[Dict, str]:
        """
        查询快照组
        :param kwargs:
        """
        command = f"{self.zstack_cli} {commands.ZStack_Query_SnapshotGroup}"
        if kwargs:
            for key, value in kwargs.items():
                command += f"{key}={value}"
        response = self.client.run_command(command)
        return response['stdout']

    def check_volume_snapshot_group_availability(self, uuids: str) -> Union[Dict, str]:
        """
        检查快照组可用性
        :param uuids: 快照组UUIDs
        """
        if not uuids:
            raise ParameterIsNoneError(uuids=uuids)
        command = f"{self.zstack_cli} {commands.ZStack_Check_SnapshotGroup_Availability.format(uuids=uuids)}"
        response = self.client.run_command(command)
        return response['stdout']

    def revert_vm_from_snapshot_group(self, uuid: str) -> Union[Dict, str]:
        """
        恢复快照组
        :param uuid: 快照组的UUID
        """
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)
        command = f"{self.zstack_cli} {commands.ZStack_Revert_Vm_from_SnapshotGroup.format(uuid=uuid)}"
        response = self.client.run_command(command)
        return response['stdout']

    def ungroup_volume_snapshot_group(self, uuid: str) -> Union[Dict, str]:
        """
        解绑快照组
        :param uuid:  快照组的UUID
        """
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)
        command = f"{self.zstack_cli} {commands.ZStack_Ungroup_Volume_SnapshotGroup.format(uuid=uuid)}"
        response = self.client.run_command(command)
        return response['stdout']
