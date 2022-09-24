#!/usr/bin/env python3
# -*- coding:utf-8 -*- 

from logging import Logger
from typing import Dict, Union
from src.api.client import ZStackClient
from src.config import commands
from src.utils.errors import ParameterIsNoneError

"""镜像资源类"""


class Images(ZStackClient):

    def __init__(self, logger: Logger = None):
        super(Images, self).__init__(logger=logger)

    def add_image(self, name: str, url: str, form: str, backupStorageUuids: str, description: str = None,
                  mediaType: str = None, guestOsType: str = None, system: bool = False, platform: str = None
                  ) -> Union[Dict, str]:
        """
        添加镜像
        :param name: 镜像名称
        :param url: 被添加镜像的URL地址
        :param form: 镜像的格式 ["raw", "qcow2", "iso"]
        :param backupStorageUuids: 指定添加镜像的镜像服务器uuid列表
        :param description: 镜像的详细描述
        :param mediaType: 镜像的类型 ["RootVolumeTemplate", "ISO", "DataVolumeTemplate"]
        :param guestOsType: 镜像对应客户机操作系统的类型
        :param system: 是否系统镜像
        :param platform: 镜像的系统平台 ["Linux", "Windows", "Windows Virtio", "Other", "Paravirtualization"]
        """
        if not name or not url or not form or not backupStorageUuids:
            raise ParameterIsNoneError(name=name, url=url, form=form, backupStorageUuids=backupStorageUuids)

        command = f"{self.zstack_cli} {commands.ZStack_Add_Image.format(name=name, url=url, form=form, stouuid=backupStorageUuids)}"
        if description:
            command = f"{command} description={description}"
        if mediaType:
            command = f"{command} mediaType={mediaType}"
        if guestOsType:
            command = f"{command} guestOsType={guestOsType}"
        if system:
            command = f"{command} system={system}"
        if platform:
            command = f"{command} platform={platform}"
        response = self.client.run_command(command)
        return response['stdout']

    def delete_image(self, uuid: str, backupStorageUuids: str = None, deleteMode: str = None) -> Union[Dict, str]:
        """
        删除镜像
        :param uuid: 镜像uuid
        :param backupStorageUuids: 镜像服务器uuid列表
        :param deleteMode: 删除模式 ["Permissive", "Enforcing"]
        """
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)
        command = f"{self.zstack_cli} {commands.ZStack_Delete_Image.format(uuid=uuid)}"
        if backupStorageUuids:
            command = f"{command} backupStorageUuids={backupStorageUuids}"
        if deleteMode:
            command = f"{command} deleteMode={deleteMode}"
        response = self.client.run_command(command)
        return response['stdout']

    def expunge_image(self, imageUuid: str, backupStorageUuids: str = None) -> Union[Dict, str]:
        """
        彻底删除镜像
        :param imageUuid: 镜像uuid
        :param backupStorageUuids: 镜像服务器uuid列表
        """
        if not imageUuid:
            raise ParameterIsNoneError(imageUuid=imageUuid)

        command = f"{self.zstack_cli} {commands.ZStack_Expunge_Image.format(iuuid=imageUuid)}"
        if backupStorageUuids:
            command = f"{command} backupStorageUuids={backupStorageUuids}"
        response = self.client.run_command(command)
        return response['stdout']

    def query_image(self, status: str = None, system: str = None, vmInstanceUuid: str = None, **kwargs) -> Union[Dict, str]:
        """
        查询镜像
        :param status: 镜像状态
        :param system: 是否是系统镜像 [true, false]
        :param vmInstanceUuid: 云主机uuid
        """
        command = f"{self.zstack_cli} {commands.ZStack_Query_Image}"
        if status:
            command = f"{command} status={status}"
        if system:
            command = f"{command} system={system}"
        if vmInstanceUuid:
            command = f"{command} volume.vmInstanceUuid={vmInstanceUuid}"
        if kwargs:
            for key, value in kwargs.items():
                command += f"{key}={value}"
        response = self.client.run_command(command)
        return response['stdout']

    def recover_image(self, imageUuid: str, backupStorageUuids: str = None) -> Union[Dict, str]:
        """
        恢复删除(但未彻底删除)的镜像
        :param imageUuid: 镜像uuid
        :param backupStorageUuids: 镜像服务器uuid列表
        """
        if not imageUuid:
            raise ParameterIsNoneError(imageUuid=imageUuid)
        command = f"{self.zstack_cli} {commands.ZStack_Recover_Image.format(iuuid=imageUuid)}"
        if backupStorageUuids:
            command = f"{command} backupStorageUuids={backupStorageUuids}"
        response = self.client.run_command(command)
        return response['stdout']

    def change_image_state(self, uuid: str, stateEvent: str) -> Union[Dict, str]:
        """
        修改镜像状态
        :param uuid: 镜像uuid
        :param stateEvent: 镜像的状态 ["enable", "disable"]
        """
        if not uuid or not stateEvent:
            raise ParameterIsNoneError(uuid=uuid, stateEvent=stateEvent)
        command = f"{self.zstack_cli} {commands.ZStack_Chaneg_Image_State.format(uuid=uuid, state=stateEvent)}"
        response = self.client.run_command(command)
        return response['stdout']

    def update_image(self, uuid: str, name: str = None, description: str = None, mediaType: str = None,
                     guestOsType: str = None, system: str = None, form: str = None, platform: str = None,
                     architecture: str = None) -> Union[Dict, str]:
        """
        更新镜像信息
        :param uuid: 镜像uuid
        :param name: 镜像名称
        :param description: 镜像的详细描述
        :param mediaType: 镜像的类型 ["RootVolumeTemplate", "ISO", "DataVolumeTemplate"]
        :param guestOsType: 镜像对应客户机操作系统的类型
        :param system: 是否系统镜像
        :param form: 镜像的格式 ["raw", "qcow2", "iso"]
        :param platform: 镜像的系统平台 ["Linux", "Windows", "Windows Virtio", "Other", "Paravirtualization"]
        :param architecture: 支持的架构 ["x86_64",  "aarch64", "mips64el"]
        """
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)
        command = f"{self.zstack_cli} {commands.ZStack_Update_Image.format(uuid=uuid)}"
        if name:
            command = f"{command} name={name}"
        if description:
            command = f"{command} description={description}"
        if mediaType:
            command = f"{command} mediaType={mediaType}"
        if guestOsType:
            command = f"{command} guestOsType={guestOsType}"
        if system:
            command = f"{command} system={system}"
        if form:
            command = f"{command} format={form}"
        if platform:
            command = f"{command} platform={platform}"
        if architecture:
            command = f"{command} architecture={architecture}"
        response = self.client.run_command(command)
        return response['stdout']

    def sync_image_size(self, uuid: str) -> Union[Dict, str]:
        """
        刷新镜像大小信息
        :param uuid: 镜像uuid
        """
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)
        command = f"{self.zstack_cli} {commands.ZStack_Sync_Image_Size.format(uuid=uuid)}"
        response = self.client.run_command(command)
        return response['stdout']

    def get_candidate_backupstorage_for_creating_image(self, volumeUuid: str, volumeSnapshotUuid: str) -> Union[Dict, str]:
        """
        获取创建镜像的镜像服务器候选
        :param volumeUuid: 云盘uuid，注意: volumeUuid和volumeSnapshotUuid二选一
        :param volumeSnapshotUuid: 云盘快照uuid，注意:volumeUuid和volumeSnapshotUuid二选一
        """
        if volumeUuid and volumeSnapshotUuid:
            raise ParameterIsNoneError(volumeUuid=volumeUuid, volumeSnapshotUuid=volumeSnapshotUuid)
        command = f"{self.zstack_cli} {commands.ZStack_Get_Candidate_BackupStorage_For_Creating_Image}"
        if volumeUuid:
            command = f"{command} volumeUuid={volumeUuid}"
        if volumeSnapshotUuid:
            command = f"{command} volumeSnapshotUuid={volumeSnapshotUuid}"
        response = self.client.run_command(command)
        return response['stdout']

    def create_rootvolume_template_from_rootvolume(self, name: str, backupStorageUuids: str, rootVolumeUuid: str,
                                                   description: str = None, guestOsType: str = None,
                                                   platform: str = None, system: str = None, resourceUuid: str = None,
                                                   architecture: str = None, tagUuids: str = None) -> Union[Dict, str]:
        """
        从根云盘创建根云盘镜像
        :param name: 根云盘镜像名称
        :param description: 根云盘镜像的详细描述
        :param guestOsType: 根云盘镜像对应客户机操作系统类型
        :param backupStorageUuids: 镜像服务器uuid列表
        :param rootVolumeUuid: 根云盘uuid
        :param platform: 根云盘镜像对应的系统平台 ["Linux", "Windows", "Windows Virtio", "Other", "Paravirtualization"]
        :param system: 是否系统根云盘镜像
        :param resourceUuid: 资源uuid。若指定，根云盘镜像会使用该字段值作为uuid
        :param architecture: 镜像所使用的系统架构
        :param tagUuids: 标签UUID列表
        """
        if not name or not backupStorageUuids or not rootVolumeUuid:
            raise ParameterIsNoneError(name=name, backupStorageUuids=backupStorageUuids, rootVolumeUuid=rootVolumeUuid)
        command = f"{self.zstack_cli} {commands.ZStack_Create_RootVolume_Template_From_RootVolume.format(name=name, voluuid=rootVolumeUuid, stouuid=backupStorageUuids)}"
        if description:
            command = f"{command} description={description}"
        if guestOsType:
            command = f"{command} guestOsType={guestOsType}"
        # if backupStorageUuids:
        #     command = f"{command} backupStorageUuids={backupStorageUuids}"
        # if rootVolumeUuid:
        #     command = f"{command} rootVolumeUuid={rootVolumeUuid}"
        if platform:
            command = f"{command} platform={platform}"
        if system:
            command = f"{command} system={system}"
        if resourceUuid:
            command = f"{command} resourceUuid={resourceUuid}"
        if architecture:
            command = f"{command} architecture={architecture}"
        if tagUuids:
            command = f"{command} tagUuids={tagUuids}"

        response = self.client.run_command(command)
        return response['stdout']

    def create_rootvolume_template_from_volumesnapshot(self, name: str, backupStorageUuids: str, snapshotUuid: str,
                                                       description: str = None, guestOsType: str = None,
                                                       platform: str = None, system: str = None, resourceUuid: str = None,
                                                       architecture: str = None, tagUuids: str = None) -> Union[Dict, str]:
        """
        从云盘快照创建根云盘镜像
        :param name: 根云盘镜像名称
        :param description: 根云盘镜像的详细描述
        :param guestOsType: 根云盘镜像对应客户机操作系统类型
        :param backupStorageUuids: 镜像服务器uuid列表
        :param snapshotUuid: 快照uuid
        :param platform: 根云盘镜像对应的系统平台 ["Linux", "Windows", "Windows Virtio", "Other", "Paravirtualization"]
        :param system: 是否系统根云盘镜像
        :param resourceUuid: 资源uuid。若指定，根云盘镜像会使用该字段值作为uuid
        :param architecture: 镜像所使用的系统架构
        :param tagUuids: 标签UUID列表
        """
        if not name or not backupStorageUuids or not snapshotUuid:
            raise ParameterIsNoneError(name=name, backupStorageUuids=backupStorageUuids, snapshotUuid=snapshotUuid)
        command = f"{self.zstack_cli} {commands.ZStack_Create_RootVolume_Template_From_VolumeSnapshot.format(name=name, snapUuid=snapshotUuid, stouuid=backupStorageUuids)}"
        if description:
            command = f"{command} description={description}"
        if guestOsType:
            command = f"{command} guestOsType={guestOsType}"
        # if backupStorageUuids:
        #     command = f"{command} backupStorageUuids={backupStorageUuids}"
        # if snapshotUuid:
        #     command = f"{command} snapshotUuid={snapshotUuid}"
        if platform:
            command = f"{command} platform={platform}"
        if system:
            command = f"{command} system={system}"
        if resourceUuid:
            command = f"{command} resourceUuid={resourceUuid}"
        if architecture:
            command = f"{command} architecture={architecture}"
        if tagUuids:
            command = f"{command} tagUuids={tagUuids}"

        response = self.client.run_command(command)
        return response['stdout']

    def create_datavolume_template_from_volume(self, volumeUuid: str, name: str, description: str = None,
                                               backupStorageUuids: str = None, resourceUuid: str = None) -> Union[Dict, str]:
        """
        从云盘创建数据云盘镜像
        :param volumeUuid: 起始云盘uuid
        :param name: 数据云盘镜像名称
        :param description: 数据云盘镜像的详细描述
        :param backupStorageUuids: 镜像服务器uuid列表
        :param resourceUuid: 数据云盘镜像uuid。若指定，数据云盘镜像会使用该字段值作为uuid
        """
        if not volumeUuid or not name:
            raise ParameterIsNoneError(volumeUuid=volumeUuid, name=name)
        command = f"{self.zstack_cli} {commands.ZStack_Create_DataVolume_Template_From_Volume.format(name=name, voluuid=volumeUuid)}"
        if description:
            command = f"{command} description={description}"
        if backupStorageUuids:
            command = f"{command} backupStorageUuids={backupStorageUuids}"
        if resourceUuid:
            command = f"{command} resourceUuid={resourceUuid}"
        response = self.client.run_command(command)
        return response['stdout']

    def create_datavolume_template_from_volumesnapshot(self, name: str, backupStorageUuids: str, snapshotUuid: str,
                                                       description: str = None, guestOsType: str = None, platform: str = None,
                                                       system: str = None, resourceUuid: str = None) -> Union[Dict, str]:
        """
        从云盘快照创建数据云盘镜像
        :param name: 数据云盘镜像名称
        :param backupStorageUuids: 镜像服务器uuid列表
        :param snapshotUuid: 快照uuid
        :param description: 数据云盘镜像的详细描述
        :param guestOsType: 数据云盘镜像对应客户机操作系统类型
        :param platform: 数据云盘镜像对应的系统平台 ["Linux", "Windows", "Windows Virtio", "Other", "Paravirtualization"]
        :param system: 是否系统数据云盘镜像
        :param resourceUuid: 资源uuid。若指定，数据云盘镜像会使用该字段值作为uuid
        """
        if not name or not backupStorageUuids or not snapshotUuid:
            raise ParameterIsNoneError(name=name, backupStorageUuids=backupStorageUuids, snapshotUuid=snapshotUuid)
        command = f"{self.zstack_cli} {commands.ZStack_Create_DataVolume_Template_From_VolumeSnapshot.format(name=name, stouuid=backupStorageUuids, snapUuid=snapshotUuid)}"

        if description:
            command = f"{command} description={description}"
        if guestOsType:
            command = f"{command} guestOsType={guestOsType}"
        if platform:
            command = f"{command} platform={platform}"
        if system:
            command = f"{command} system={system}"
        if resourceUuid:
            command = f"{command} resourceUuid={resourceUuid}"

        response = self.client.run_command(command)
        return response['stdout']

    def get_image_qga(self, uuid: str) -> Union[Dict, str]:
        """
        获取镜像Qga
        :param uuid: 镜像uuid
        """
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)

        command = f"{self.zstack_cli} {commands.ZStack_Get_Image_Qga.format(uuid=uuid)}"
        response = self.client.run_command(command)
        return response['stdout']

    def set_image_qga(self, uuid: str, enable: str = None) -> Union[Dict, str]:
        """
        设置镜像Qga
        :param uuid: 镜像uuid
        :param enable: [true, false]
        """
        if not uuid or not enable:
            raise ParameterIsNoneError(uuid=uuid, enable=enable)
        command = f"{self.zstack_cli} {commands.ZStack_Set_Image_Qga.format(enable=enable, uuid=uuid)}"
        response = self.client.run_command(command)
        return response['stdout']

    def set_image_boot_mode(self, uuid: str, bootMode: str) -> Union[Dict, str]:
        """
        设置镜像启动模式
        :param uuid: 资源的UUID，唯一标示该资源
        :param bootMode: 镜像启动模式 ["Legacy", "UEFI", "UEFI_WITH_CSM"]
        """
        if not uuid or not bootMode:
            raise ParameterIsNoneError(uuid=uuid, bootMode=bootMode)
        command = f"{self.zstack_cli} {commands.ZStack_Set_Image_Boot_Mode.format(uuid=uuid, mode=bootMode)}"
        response = self.client.run_command(command)
        return response['stdout']

    def get_upload_image_job_details(self, imageId: str) -> Union[Dict, str]:
        """
        获取上传镜像任务详情
        :param imageId: 上传镜像的唯一标识，由用户自定义，推荐使用md5
        """
        if not imageId:
            raise ParameterIsNoneError(imageId=imageId)
        command = f"{self.zstack_cli} {commands.ZStack_Get_Upload_Image_Job_Details}"
        response = self.client.run_command(command)
        return response['stdout']
