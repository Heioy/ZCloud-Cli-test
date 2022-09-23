#!/usr/bin/env python3
# -*- coding:utf-8 -*- 

from logging import Logger
from typing import Union, Dict
from src.api.client import ZStackClient
from src.config import commands
from src.utils.errors import ParameterIsNoneError


"""云盘资源类"""


class DataVolume(ZStackClient):

    def __init__(self, logger: Logger = None):
        super(DataVolume, self).__init__(logger=logger)
        self.create_volume_timeout = 10 * 60

    def create_datavolume(self, name: str, description: str = None, diskOfferingUuid: str = None,
                          primaryStorageUuid: str = None, resourceUuid: str = None, tagUuids: str = None
                          ) -> Union[Dict, str]:
        """
        创建云盘
        :param name: 云盘名称
        :param description: 云盘描述
        :param diskOfferingUuid: 云盘规格uuid
        :param primaryStorageUuid: 主存储uuid
        :param resourceUuid: 资源uuid。若指定，镜像会使用该字段值作为uuid
        :param tagUuids: 标签UUID列表
        """
        if not name:
            raise ParameterIsNoneError(name=name)

        command = f"{self.zstack_cli} {commands.ZStack_Create_DataVolume.format(volname=name)}"

        if description:
            command = f"{command} description={description}"
        if diskOfferingUuid:
            command = f"{command} diskOfferingUuid={diskOfferingUuid}"
        if primaryStorageUuid:
            command = f"{command} primaryStorageUuid={primaryStorageUuid}"
        if resourceUuid:
            command = f"{command} resourceUuid={resourceUuid}"
        if tagUuids:
            command = f"{command} tagUuids={tagUuids}"

        response = self.client.run_command(command)
        return response['stdout']

    def delete_datavolume(self, uuid: str, deleteMode: str = None) -> Union[Dict, str]:
        """
        删除云盘
        :param uuid: 云盘uuid
        :param deleteMode: ["Permissive", "Enforcing"]
        """
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)

        command = f"{self.zstack_cli} {commands.ZStack_Delete_DataVolume.format(uuid)}"
        if deleteMode:
            command = f"{command} deleteMode={deleteMode}"
        response = self.client.run_command(command)

        return response['stdout']

    def expunge_datavolume(self, uuid: str) -> Union[Dict, str]:
        """
        彻底删除云盘
        :param uuid: 云盘uuid
        """
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)
        command = f"{self.zstack_cli} {commands.ZStack_Expunge_DataVolume.format(uuid=uuid)}"
        response = self.client.run_command(command)

        return response['stdout']

    def recover_datavolume(self, uuid: str) -> Union[Dict, str]:
        """
        恢复云盘
        :param uuid: 云盘uuid
        """
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)

        command = f"{self.zstack_cli} {commands.ZStack_Recover_DataVolume.format(uuid=uuid)}"
        response = self.client.run_command(command)

        return response['stdout']

    def change_volume_state(self, uuid: str, stateEvent: str) -> Union[Dict, str]:
        """
        开启或关闭云盘
        :param uuid: 云盘uuid
        :param stateEvent: 开启或关闭 ["enable", "disable"]
        """
        if not uuid or not stateEvent:
            raise ParameterIsNoneError(uuid=uuid, stateEvent=stateEvent)

        command = f"{self.zstack_cli} {commands.ZStack_Change_Volume_State.format(uuid=uuid, state=stateEvent)}"
        response = self.client.run_command(command)

        return response['stdout']

    def create_datavolume_from_volume_template(self, imageUuid: str, name: str, primaryStorageUuid: str,
                                               description: str = None, hostUuid: str = None, resourceUuid: str = None
                                               ) -> Union[Dict, str]:
        """
        从镜像创建云盘
        :param imageUuid: 镜像uuid
        :param name: 云盘名称
        :param primaryStorageUuid: 主存储uuid
        :param description: 云盘的详细描述
        :param hostUuid: 物理主机uuid
        :param resourceUuid: 资源uuid
        """
        if not imageUuid or not name or not primaryStorageUuid:
            raise ParameterIsNoneError(imageUuid=imageUuid, name=name, primaryStorageUuid=primaryStorageUuid)

        command = f"{self.zstack_cli} {commands.ZStack_Create_DataVolume_From_Volume_Templat.format(name=name, iuuid=imageUuid, stoUuid=primaryStorageUuid)}"
        response = self.client.run_command(command)

        return response['stdout']

    def create_datavolume_from_volume_snapshot(self, volumeSnapshotUuid: str, name: str, primaryStorageUuid: str,
                                               description: str = None, resourceUuid: str = None) -> Union[Dict, str]:
        """
        从快照创建云盘
        :param volumeSnapshotUuid: 云盘快照uuid
        :param name: 云盘名称
        :param primaryStorageUuid: 主存储uuid
        :param description: 云盘的详细描述
        :param resourceUuid: 资源uuid
        """
        if not volumeSnapshotUuid or not name or not primaryStorageUuid:
            raise ParameterIsNoneError(volumeSnapshotUuid=volumeSnapshotUuid, name=name, primaryStorageUuid=primaryStorageUuid)

        command = f"{self.zstack_cli} {commands.ZStack_Create_DataVolume_From_Volume_Snapshot.format(name=name, snapUuid=volumeSnapshotUuid, stoUuid=primaryStorageUuid)}"
        response = self.client.run_command(command)

        return response['stdout']

    def query_volume(self, vmInstanceUuid: str = None, primaryStorageUuid: str = None, diskOfferingName: str = None,
                     snapshotUuid: str = None, imageUuid: str = None) -> Union[Dict, str]:
        """
        获取云盘清单
        :param vmInstanceUuid: 云盘所挂载的云主机uuid
        :param primaryStorageUuid: 该云盘所在的主存储uuid
        :param diskOfferingName: 从该云盘创建出来的所有云盘规格名称
        :param snapshotUuid: 从该云盘创建出来的所有云盘快照uuid
        :param imageUuid: 从该云盘创建出来的镜像uuid
        """
        command = f"{self.zstack_cli} {commands.ZStack_Query_Volume}"
        if vmInstanceUuid:
            command = f"{command} vmInstanceUuid={vmInstanceUuid}"
        if primaryStorageUuid:
            command = f"{command} primaryStorageUuid={primaryStorageUuid}"
        if diskOfferingName:
            command = f"{command} diskOfferingName={diskOfferingName}"
        if snapshotUuid:
            command = f"{command} snapshotUuid={snapshotUuid}"
        if imageUuid:
            command = f"{command} imageUuid={imageUuid}"

        response = self.client.run_command(command)
        return response['stdout']

    def get_volume_format(self) -> Union[Dict, str]:
        """
        获取云盘格式
        """
        command = f"{self.zstack_cli} {commands.ZStack_Get_Volume_Format}"
        response = self.client.run_command(command)
        return response['stdout']

    def get_volume_capabilities(self, uuid: str) -> Union[Dict, str]:
        """
        获取云盘支持的类型的能力
        :param uuid: 云盘uuid
        """
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)
        command = f"{self.zstack_cli} {commands.ZStack_Get_Volume_Capabilities.format(uuid=uuid)}"
        response = self.client.run_command(command)

        return response['stdout']

    def sync_volume_size(self, uuid: str) -> Union[Dict, str]:
        """
        同步云盘大小
        :param uuid: 云盘uuid
        """
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)
        command = f"{self.zstack_cli} {commands.ZStack_Sync_Volume_Size.format(uuid=uuid)}"
        response = self.client.run_command(command)

        return response['stdout']

    def resize_rootvolume(self, uuid: str, size: int) -> Union[Dict, str]:
        """
        扩展根云盘
        :param uuid: 云盘uuid
        :param size: 扩展后大小
        """
        if not uuid or not size:
            raise ParameterIsNoneError(uuid=uuid, size=size)

        command = f"{self.zstack_cli} {commands.ZStack_Resize_RootVolume.format(uuid=uuid, size=size)}"
        response = self.client.run_command(command)

        return response['stdout']

    def resize_datavolume(self, uuid: str, size: int) -> Union[Dict, str]:
        """
        扩展数据云盘
        :param uuid: 云盘uuid
        :param size: 扩展后大小
        """
        if not uuid or not size:
            raise ParameterIsNoneError(uuid=uuid, size=size)

        command = f"{self.zstack_cli} {commands.ZStack_Resize_DataVolume.format(uuid=uuid, size=size)}"
        response = self.client.run_command(command)

        return response['stdout']

    def update_volume(self, uuid: str, name: str = None, description: str = None) -> Union[Dict, str]:
        """
        修改云盘属性
        :param uuid: 云盘uuid
        :param name: 云盘名称
        :param description: 云盘的详细描述
        """
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)

        command = f"{self.zstack_cli} {commands.ZStack_Update_Volume.format(uuid=uuid)}"
        if name:
            command = f"{command} name={name}"
        if description:
            command = f"{command} description={description}"
        response = self.client.run_command(command)

        return response['stdout']

    def set_volume_qos(self, uuid: str, volumeBandwidth: int, mode: str = None) -> Union[Dict, str]:
        """
        设置云盘限速
        :param uuid: 云盘uuid
        :param volumeBandwidth: 云盘限速带宽
        :param mode: 限速模式 ["total", "read", "write"]
        """
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)

        command = f"{self.zstack_cli} {commands.ZStack_Set_Volume_QoS.format(uuid=uuid, volwid=volumeBandwidth)}"
        if mode:
            command = f"{command} mode={mode}"
        response = self.client.run_command(command)

        return response['stdout']

    def get_volume_qos(self, uuid: str, forceSync: str = None) -> Union[Dict, str]:
        """
        获取云盘限速
        :param uuid: 云盘uuid
        :param forceSync: 是否到物理机上去同步数据
        """
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)
        command = f"{self.zstack_cli} {commands.ZStack_Get_Volume_QoS.format(uuid=uuid)}"

        if forceSync:
            command = f"{command} forceSync={forceSync}"
        response = self.client.run_command(command)

        return response['stdout']

    def delete_volume_qos(self, uuid: str, mode: str = None) -> Union[Dict, str]:
        """
        取消云盘网卡限速
        :param uuid: 云盘uuid
        :param mode: 删除模式 ["total", "read", "write", "all"]
        """
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)
        command = f"{self.zstack_cli} {commands.ZStack_Delete_Volume_QoS.format(uuid=uuid)}"
        response = self.client.run_command(command)

        return response['sdtout']

    def get_datavolume_attachable_vm(self, volumeUuid: str) -> Union[Dict, str]:
        """
        获取云盘可被加载的云主机列表
        :param volumeUuid: 云盘uuid
        """
        if not volumeUuid:
            raise ParameterIsNoneError(volumeUuid=volumeUuid)

        command = f"{self.zstack_cli} {commands.ZStack_Get_DataVolume_Attachable_Vm.format(voluuid=volumeUuid)}"
        response = self.client.run_command(command)

        return response['stdout']

    def attach_datavolume_to_vm(self, vmInstanceUuid: str, volumeUuid: str) -> Union[Dict, str]:
        """
        挂载云盘到云主机上
        :param vmInstanceUuid: 云主机uuid
        :param volumeUuid: 云盘uuid
        """
        if not vmInstanceUuid or not volumeUuid:
            raise ParameterIsNoneError(vmInstanceUuid=vmInstanceUuid, volumeUuid=volumeUuid)

        command = f"{self.zstack_cli} {commands.ZStack_Attach_DataVolume_to_Vm.format(voluuid=volumeUuid, vuuid=vmInstanceUuid)}"
        response = self.client.run_command(command)

        return response['stdout']

    def detach_datavolume_from_vm(self, uuid: str, vmUuid: str) -> Union[Dict, str]:
        """
        从云主机上卸载云盘
        :param uuid: 云盘uuid
        :param vmUuid: 云主机uuid
        """
        if not uuid or not vmUuid:
            raise ParameterIsNoneError(uuid=uuid, vmUuid=vmUuid)

        command = f"{self.zstack_cli} {commands.ZSTack_Detach_DataVolume_From_Vm.format(uuid=uuid, vuuid=vmUuid)}"
        response = self.client.run_command(command)

        return response['stdout']

    def create_volume_snapshot(self, volumeUuid: str, name: str, description: str = None, resourceUuid: str = None) -> Union[Dict, str]:
        """
        从云盘创建快照
        :param volumeUuid: 云盘uuid
        :param name: 快照名称
        :param description: 快照的详细描述
        :param resourceUuid: 资源uuid
        """
        if not volumeUuid or not name:
            raise ParameterIsNoneError(volumeUuid=volumeUuid, name=name)

        command = f"{self.zstack_cli} {commands.ZStack_Create_Volume_Snapshot.format(voluuid=volumeUuid, name=name)}"
        if description:
            command = f"{command} description={description}"
        if resourceUuid:
            command = f"{command} resourceUuid={resourceUuid}"

        response = self.client.run_command(command)
        return response['stdout']

    def query_volume_snapshot(self, **kwargs) -> Union[Dict, str]:
        """
        查询云盘快照
        """
        command = f"{self.zstack_cli} {commands.ZStack_Query_Volume_Snapshot}"
        if kwargs:
            for key, value in kwargs.items():
                command += f"{key}={value}"
        response = self.client.run_command(command)
        return response['stdout']

    def query_volume_snapshot_tree(self, **kwargs) -> Union[Dict, str]:
        """
        查询快照树
        """
        command = f"{self.zstack_cli} {commands.ZStack_Query_Volume_Snapshot_Tree}"
        if kwargs:
            for key, value in kwargs.items():
                command += f"{key}={value}"
        response = self.client.run_command(command)
        return response['stdout']

    def update_volume_snapshot(self, uuid: str, name: str = None, description: str = None) -> Union[Dict, str]:
        """
        更新云盘快照信息
        :param uuid: 快照uuid
        :param name: 快照的新名称
        :param description: 快照的新详细描述
        """
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)
        command = f"{self.zstack_cli} {commands.ZStack_Update_Volume_Snapshot.format(uuid=uuid)}"
        if name:
            command = f"{command} name={name}"
        if description:
            command = f"{command} description={description}"
        response = self.client.run_command(command)
        return response['stdout']

    def delete_volume_snapshot(self, uuid: str, deleteMode: str) -> Union[Dict, str]:
        """
        删除云盘快照
        :param uuid: 快照uuid
        :param deleteMode: 删除模式 ["Permissive", "Enforcing"]
        """
        if not uuid or not deleteMode:
            raise ParameterIsNoneError(uuid=uuid, deleteMode=deleteMode)
        command = f"{self.zstack_cli} {commands.ZStack_Delete_Volume_Snapshot.format(uuid=uuid, deletemode=deleteMode)}"
        response = self.client.run_command(command)
        return response['stdout']

    def restore_volume_from_snapshot(self, uuid: str) -> Union[Dict, str]:
        """
        将云盘回滚至指定快照
        :param uuid: 快照uuid
        """
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)
        command = f"{self.zstack_cli} {commands.ZStack_Revert_Volume_From_Snapshot.format(uuid=uuid)}"
        response = self.client.run_command(command)

        return response['stdout']

    def get_volume_snapshot_size(self, uuid: str) -> Union[Dict, str]:
        """
        获取快照容量
        :param uuid: 快照UUID
        """
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)
        command = f"{self.zstack_cli} {commands.ZStack_Get_Volume_Snapshot_Size.format(uuid=uuid)}"
        response = self.client.run_command(command)

        return response['stdout']

    def shrink_volume_snapshot(self, uuid: str) -> Union[Dict, str]:
        """
        快照瘦身
        :param uuid: 资源的UUID，唯一标示该资源
        """
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)
        command = f"{self.zstack_cli} {commands.ZStack_Shrink_Volume_Snaspshot.format(uuid=uuid)}"
        response = self.client.run_command(command)

        return response['stdout']
