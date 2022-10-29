#!/usr/bin/env python3
# -*- coding:utf-8 -*- 

from typing import Union, Dict
from logging import Logger
from src.api.client import ZStackClient
from src.config import commands
from src.utils.errors import ParameterIsNoneError


class BackupStorage(ZStackClient):

    def __init__(self, logger: Logger = None):
        super(BackupStorage, self).__init__(logger=logger)

    def delete_backupStorage(self, uuid: str, deleteMode: str = None) -> Union[Dict, str]:
        """
        删除镜像服务器
        :param uuid: 镜像服务器的uuid
        :param deleteMode: 资源删除模式 ["Permissive", "Enforcing"]
        """
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)
        command = f"{self.zstack_cli} {commands.ZStack_Delete_BackupStorage.format(uuid=uuid)}"
        if deleteMode:
            command = f"{command} deleteMode={deleteMode}"
        response = self.client.run_command(command)
        return response['stdout']

    def query_backupStorage(self, uuid: str = None, stoUuid: str = None) -> Union[Dict, str]:
        """
        查询镜像服务器
        :param uuid:
        :param stoUuid:
        """
        command = f"{self.zstack_cli} {commands.ZStack_Query_BackupStorage}"
        if uuid:
            command = f"{command} uuid={uuid}"
        if stoUuid:
            command = f"{command} zone.primaryStorage.uuid={stoUuid}"
        response = self.client.run_command(command)
        return response['stdout']

    def reconnect_backupStorage(self, uuid: str) -> Union[Dict, str]:
        """
        重连镜像服务器
        :param uuid: 镜像服务器的uuid
        """
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)
        command = f"{self.zstack_cli} {commands.ZStack_Reconnect_BackupStorage.format(uuid=uuid)}"
        response = self.client.run_command(command)
        return response['stdout']

    def change_backupStorage_state(self, uuid: str, stateEvent: str) -> Union[Dict, str]:
        """
        更改镜像服务器可用状态
        :param uuid: 镜像服务器的uuid
        :param stateEvent: 镜像服务器的目标状态 ["enable", "disable"]
        """
        if not uuid or not stateEvent:
            raise ParameterIsNoneError(uuid=uuid, stateEvent=stateEvent)
        command = f"{self.zstack_cli} {commands.ZStack_Change_BackupStorage_State.format(uuid=uuid, state=stateEvent)}"
        response = self.client.run_command(command)
        return response['stdout']

    def get_backupStorage_capacity(self, backupStorageUuids: str, zoneUuids: str = None, get_all: str = None) -> Union[Dict, str]:
        """
        获取镜像服务器存储容量
        :param backupStorageUuids: 镜像服务器uuid列表；zoneUuids,backupStorageUuids 至少有一个不为空，或者all被设置为真
        :param zoneUuids: 区域uuid列表
        :param get_all: 当镜像服务器uuid列表为空时，该项为真表示查询系统中所有的镜像服务器
        """
        if not backupStorageUuids:
            raise ParameterIsNoneError(backupStorageUuids=backupStorageUuids)
        command = f"{self.zstack_cli} {commands.ZStack_Get_BackupStorage_Capacity.format(stouuid=backupStorageUuids)}"
        if zoneUuids:
            command = f"{command} zoneUuids={zoneUuids}"
        if get_all:
            command = f"{command} all={get_all}"
        response = self.client.run_command(command)
        return response['stdout']

    def get_backupStorage_types(self) -> Union[Dict, str]:
        """
        获取镜像服务器类型列表
        """
        command = f"{self.zstack_cli} {commands.ZStack_Get_BackupStorage_Types}"
        response = self.client.run_command(command)
        return response['stdout']

    def update_backupStorage(self, uuid: str, name: str, description: str = None) -> Union[Dict, str]:
        """
        更新镜像服务器信息
        :param uuid: 指定目标镜像服务器的uuid
        :param name: 镜像服务器的新名称
        :param description: 镜像服务器的详细描述
        """
        if not uuid or not name:
            raise ParameterIsNoneError(uuid=uuid, name=name)
        command = f"{self.zstack_cli} {commands.ZStack_Update_BackupStorage.format(uuid=uuid, name=name)}"
        if description:
            command = f"{command} description={description}"
        response = self.client.run_command(command)
        return response['stdout']

    def export_image_from_backupStorage(self, backupStorageUuid: str, imageUuid: str, exportFormat: str = None) -> Union[Dict, str]:
        """
        从镜像服务器导出镜像
        :param backupStorageUuid: 镜像服务器uuid
        :param imageUuid: 镜像uuid
        :param exportFormat: 导出镜像的保存格式
        """
        if not backupStorageUuid or not imageUuid:
            raise ParameterIsNoneError(backupStorageUuid=backupStorageUuid, imageUuid=imageUuid)
        command = f"{self.zstack_cli} {commands.ZStack_Export_Image_from_BackupStorage.format(stouuid=backupStorageUuid, iuuid=imageUuid)}"
        if exportFormat:
            command = f"{command} exportFormat={exportFormat}"
        response = self.client.run_command(command)
        return response['stdout']

    def delete_exported_image_from_backupStorage(self, backupStorageUuid: str, imageUuid: str) -> Union[Dict, str]:
        """
        从镜像服务器删除导出的镜像
        :param backupStorageUuid: 镜像服务器uuid
        :param imageUuid: 镜像uuid
        """
        if not backupStorageUuid or not imageUuid:
            raise ParameterIsNoneError(backupStorageUuid=backupStorageUuid, imageUuid=imageUuid)
        command = f"{self.zstack_cli} {commands.ZStack_Delete_Exported_Image_from_BackupStorage.format(stouuid=backupStorageUuid, iuuid=imageUuid)}"
        response = self.client.run_command(command)
        return response['stdout']

    def attach_backupStorage_to_zone(self, backupStorageUuid: str, zoneUuid: str) -> Union[Dict, str]:
        """
        挂载镜像服务器至区域
        :param backupStorageUuid: 镜像服务器uuid
        :param zoneUuid: 区域uuid
        """
        if not backupStorageUuid or not zoneUuid:
            raise ParameterIsNoneError(backupStorageUuid=backupStorageUuid, zoneUuid=zoneUuid)
        command = f"{self.zstack_cli} {commands.ZStack_Attach_BackupStorage_to_Zone.format(stouuid=backupStorageUuid, zoneUuid=zoneUuid)}"
        response = self.client.run_command(command)
        return response['stdout']

    def detach_backupStorage_from_zone(self, backupStorageUuid: str, zoneUuid: str) -> Union[Dict, str]:
        """
        从区域中卸载已经挂载的镜像服务器
        :param backupStorageUuid: 镜像服务器uuid
        :param zoneUuid: 区域uuid
        """
        if not backupStorageUuid or not zoneUuid:
            raise ParameterIsNoneError(backupStorageUuid=backupStorageUuid, zoneUuid=zoneUuid)
        command = f"{self.zstack_cli} {commands.ZStack_Detach_BackupStorage_from_Zone.format(stouuid=backupStorageUuid, zoneUuid=zoneUuid)}"
        response = self.client.run_command(command)
        return response['stdout']

    def backupStorage_migrate_image(self, imageUuid: str, srcBackupStorageUuid: str, dstBackupStorageUuid: str) -> Union[Dict, str]:
        """
        跨镜像服务器迁移镜像
        :param imageUuid: 镜像uuid
        :param srcBackupStorageUuid: 源镜像服务器uuid
        :param dstBackupStorageUuid: 目标镜像服务器uuid
        """
        if not imageUuid or not srcBackupStorageUuid or not dstBackupStorageUuid:
            raise ParameterIsNoneError(imageUuid=imageUuid,
                                       srcBackupStorageUuid=srcBackupStorageUuid,
                                       dstBackupStorageUuid=dstBackupStorageUuid)
        command = f"{self.zstack_cli} \
                    {commands.ZStack_BackupStorage_Migrate_Image.format(iuuid=imageUuid, srcUuid=srcBackupStorageUuid, dstUuid=dstBackupStorageUuid)}"
        response = self.client.run_command(command)
        return response['stdout']

    def get_backupStorage_candidates_for_image_migration(self, srcBackupStorageUuid: str) -> Union[Dict, str]:
        """
        获取候选列表
        :param srcBackupStorageUuid: 待迁移镜像所在镜像服务器uuid
        """
        if not srcBackupStorageUuid:
            raise ParameterIsNoneError(srcBackupStorageUuid=srcBackupStorageUuid)
        command = f"{self.zstack_cli} {commands.ZStack_Get_BackupStorage_Candidates_from_Image_Migration.format(srcUuid=srcBackupStorageUuid)}"
        response = self.client.run_command(command)
        return response['stdout']

    def add_imageStore_backupStorage(self, hostname: str, username: str, password: str, url: str, name: str,
                                      sshPort: int = 22, description: str = None, store_type: str = 'ImageStoreBackupStorage ',
                                      importImages: str = None, resourceUuid: str = None) -> Union[Dict, str]:
        """
        添加镜像仓库服务器
        :param hostname: 服务器主机地址
        :param username: 服务器SSH用户名
        :param password: 服务器SSH用户密码
        :param url: 镜像仓库本地数据存放路径
        :param name: 镜像仓库名称
        :param sshPort: 服务器SSH端口
        :param description: 镜像仓库详细描述
        :param store_type: 类型为ImageStoreBackupStorage
        :param importImages: 是否导入镜像
        :param resourceUuid: 资源uuid
        """
        if not hostname or not username or not password or not url or not name:
            raise ParameterIsNoneError(hostname=hostname, username=username, password=password, url=url, name=name)
        command = f"{self.zstack_cli} {commands.ZStack_Add_ImageStore_BakcupStorage.format(hostname=hostname, username=username, password=password, url=url, name=name)}"
        if sshPort:
            command = f"{command} sshPort={sshPort}"
        if description:
            command = f"{command} description={description}"
        if store_type:
            command = f"{command} type={store_type}"
        if importImages:
            command = f"{command} importImages={importImages}"
        if resourceUuid:
            command = f"{command} resourceUuid={resourceUuid}"
        response = self.client.run_command(command)
        return response['stdout']

    def update_imageStore_backupStorage(self, uuid: str, name: str, hostname: str = None, username: str = None,
                                        password: str = None, sshPort: int = 22, description: str =  None) -> Union[Dict, str]:
        """
        更新镜像仓库服务器信息
        :param uuid: 镜像服务器uuid
        :param name: 镜像服务器新名称
        :param hostname: 镜像服务器主机地址
        :param username: SSH用户名
        :param password: SSH用户密码
        :param sshPort: 服务器SSH端口
        :param description: 镜像服务器新详细描述
        """
        if not uuid or not name:
            raise ParameterIsNoneError(uuid=uuid, name=name)
        command = f"{self.zstack_cli} {commands.ZStack_Update_ImageStore_BackupStorage.format(uuid=uuid, name=name)}"
        if hostname:
            command = f"{command} hostname={hostname}"
        if username:
            command = f"{command} username={username}"
        if password:
            command = f"{command} password={password}"
        if sshPort:
            command = f"{command} sshPort={sshPort}"
        if description:
            command = f"{command} description={description}"
        response = self.client.run_command(command)
        return response['stdout']

    def reconnect_imageStore_backupStorage(self, uuid: str) -> Union[Dict, str]:
        """
        重连镜像仓库服务器
        :param uuid: 镜像仓库服务器uuid
        """
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)
        command = f"{self.zstack_cli} {commands.ZStack_Reconnect_ImageStore_BackupStorage.format(uuid=uuid)}"
        response = self.client.run_command(command)
        return response['stdout']

    def recliam_space_from_imageStore(self, uuid: str) -> Union[Dict, str]:
        """
        从镜像仓库回收磁盘空间
        :param uuid: 镜像仓库服务器uuid
        """
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)
        command = f"{self.zstack_cli} {commands.ZStack_Recliam_Space_from_ImageStore.format(uuid=uuid)}"
        response = self.client.run_command(command)
        return response['stdout']

    def add_ceph_backupStorage(self, monUrls: str, name: str, poolName: str = None, description: str = None,
                               ceph_type: str = 'Ceph', importImages: str = None, resourceUuid: str = None) -> Union[Dict, str]:
        """
        添加Ceph镜像服务器
        :param monUrls: Ceph mon的地址列表
        :param name: 镜像服务器新名称
        :param poolName: 用于存放镜像的Ceph pool名字
        :param description: 镜像服务器详细描述
        :param ceph_type: 类型为Ceph
        :param importImages: 是否导入镜像
        :param resourceUuid: 资源uuid
        """
        if not monUrls or not name:
            raise ParameterIsNoneError(monUrls=monUrls, name=name)
        command = f"{self.zstack_cli} {commands.ZStack_Add_Ceph_BackupStorage.format(name=name, monUrls=monUrls)}"
        if poolName:
            command = f"{command} poolName={poolName}"
        if description:
            command = f"{command} description={description}"
        if ceph_type:
            command = f"{command} type={ceph_type}"
        if importImages:
            command = f"{command} importImages={importImages}"
        if resourceUuid:
            command = f"{command} resourceUuid={resourceUuid}"
        response = self.client.run_command(command)
        return response['stdout']

    def query_ceph_backupStorage(self, uuid: str = None, hostname: str = None) -> Union[Dict, str]:
        """
        查询Ceph镜像服务器
        :param uuid:
        :param hostname:
        """
        command = f"{self.zstack_cli} {commands.ZStack_Query_Ceph_BackupStorage}"
        if uuid:
            command = f"{command} uuid={uuid}"
        if hostname:
            command = f"{command} mons.hostname={hostname}"
        response = self.client.run_command(command)
        return response['stdout']

    def update_ceph_backupStorage(self, monUuid: str, hostname: str = None, sshUsername: str = None, sshPassword: str = None,
                                  sshPort: int = 22, monPort: int = 22) -> Union[Dict, str]:
        """
        更新Ceph镜像服务器mon节点
        :param monUuid: mon节点uuid
        :param hostname: mon节点新主机地址
        :param sshUsername: mon节点主机ssh用户名
        :param sshPassword: mon节点主机ssh用户密码
        :param sshPort: mon节点主机ssh端口
        :param monPort: mon节点的端口
        """
        if not monUuid:
            raise ParameterIsNoneError(monUuid=monUuid)
        command = f"{self.zstack_cli} {commands.ZStack_Update_Ceph_BackupStorage.format(monUuid=monUuid)}"
        if hostname:
            command = f"{command} hostname={hostname}"
        if sshUsername:
            command = f"{command} sshUsername={sshUsername}"
        if sshPassword:
            command = f"{command} sshPassword={sshPassword}"
        if sshPort:
            command = f"{command} sshPort={sshPort}"
        if monPort:
            command = f"{command} monPort={monPort}"
        response = self.client.run_command(command)
        return response['stdout']

    def add_mon_to_ceph_backupStorage(self, uuid: str, monUrls: str) -> Union[Dict, str]:
        """
        为Ceph镜像服务器添加mon节点
        :param uuid: Ceph镜像服务器uuid
        :param monHostnames: mon节点名字列表
        """
        if not uuid or not monUrls:
            raise ParameterIsNoneError(uuid=uuid, monUrls=monUrls)
        command = f"{self.zstack_cli} {commands.ZStack_Add_Mon_to_Ceph_BackupStorage.format(uuid=uuid, monUrls=monUrls)}"
        response = self.client.run_command(command)
        return response['stdout']

    def remove_mon_from_ceph_backupStorage(self, uuid: str, monHostnames: str) -> Union[Dict, str]:
        """
        Ceph镜像服务器删除mon
        :param uuid: Ceph镜像服务器uuid
        :param monHostnames: mon节点名字列表
        """
        if not uuid or not monHostnames:
            raise ParameterIsNoneError(uuid=uuid, monHostnames=monHostnames)
        command = f"{self.zstack_cli} {commands.ZStack_Remove_Mon_from_Ceph_BackupStorage.format(uuid=uuid, monHostnames=monHostnames)}"
        response = self.client.run_command(command)
        return response['stdout']
