#!/usr/bin/env python3
# -*- coding:utf-8 -*- 

from typing import Union, Dict
from logging import Logger
from src.api.client import ZStackClient
from src.config import commands
from src.utils.errors import ParameterIsNoneError


class PrimaryStorage(ZStackClient):

    def __init__(self, logger: Logger = None):
        super(PrimaryStorage, self).__init__(logger=logger)

    def delete_primaryStorage(self, uuid: str, deleteMode: str = None) -> Union[Dict, str]:
        """
        删除主存储
        :param uuid: 主存储的uuid
        :param deleteMode: 删除模式
        """
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)
        command = f"{self.zstack_cli} {commands.ZStack_Delete_PrimaryStorage.format(uuid=uuid)}"
        if deleteMode:
            command = f"{command} deleteMode={deleteMode}"
        response = self.client.run_command(command)
        return response['stdout']

    def query_primaryStorage(self, uuid: str = None, cluster_uuid: str = None) -> Union[Dict, str]:
        """
        查询主存储
        :param uuid: 主存储资源UUID
        :param cluster_uuid: 区域内集群资源的UUID
        """
        command = f"{self.zstack_cli} {commands.ZStack_Query_PrimaryStorage}"
        if uuid:
            command = f"{command} uuid={uuid}"
        if cluster_uuid:
            command = f"{command} zone.cluster.uuid={cluster_uuid}"
        response = self.client.run_command(command)
        return response['stdout']

    def attach_primaryStorage_to_cluster(self, primaryStorageUuid: str, clusterUuid: str) -> Union[Dict, str]:
        """
        向集群加载主存储
        :param primaryStorageUuid: 主存储uuid
        :param clusterUuid: 集群uuid
        """
        if not primaryStorageUuid or not clusterUuid:
            raise ParameterIsNoneError(primaryStorageUuid=primaryStorageUuid, clusterUuid=clusterUuid)
        command = f"{self.zstack_cli} {commands.ZStack_Attach_PrimaryStorage_to_Cluster.format(clusterUuid=clusterUuid, stoUuid=primaryStorageUuid)}"
        response = self.client.run_command(command)
        return response['stdout']

    def detach_primaryStorage_to_cluster(self, primaryStorageUuid: str, clusterUuid: str) -> Union[Dict, str]:
        """
        从集群卸载主存储
        :param primaryStorageUuid: 主存储uuid
        :param clusterUuid: 集群uuid
        """
        if not primaryStorageUuid or not clusterUuid:
            raise ParameterIsNoneError(primaryStorageUuid=primaryStorageUuid, clusterUuid=clusterUuid)
        command = f"{self.zstack_cli} {commands.ZStack_Detach_PrimaryStorage_to_Cluster.format(clusterUuid=clusterUuid, stoUuid=primaryStorageUuid)}"
        response = self.client.run_command(command)
        return response['stdout']

    def reconnect_primaryStorage(self, uuid: str) -> Union[Dict, str]:
        """
        重连主存储
        :param uuid: 主存储uuid
        """
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)
        command = f"{self.zstack_cli} {commands.ZStack_Reconnect_PrimaryStorage.format(uuid=uuid)}"
        response = self.client.run_command(command)
        return response['stdout']

    def get_primaryStorage_capacity(self, zoneUuids: str = None, clusterUuids: str = None, primaryStorageUuids: str = None,
                                    _all: bool = False) -> Union[Dict, str]:
        """
        区域uuid列表
        :param zoneUuids: 区域uuid列表
        :param clusterUuids: 集群uuid列表
        :param primaryStorageUuids: 主存储uuid列表;区域、集群、主存储的Uuids中必须至少有一个不为空列表，或者all设置为true
        :param _all: 当主存储uuid列表为空时，该项为真，表示查询系统中所有的主存储
        """
        if not primaryStorageUuids or not _all:
            raise ParameterIsNoneError(primaryStorageUuids=primaryStorageUuids, _all=_all)
        command = f"{self.zstack_cli} {commands.ZStack_Get_PrimaryStorage_Capacity}"
        if zoneUuids:
            command = f"{command} zoneUuids={zoneUuids}"
        if clusterUuids:
            command = f"{command} clusterUuids={clusterUuids}"
        if primaryStorageUuids:
            command = f"{command} primaryStorageUuids={primaryStorageUuids}"
        if _all:
            command = f"{command} all={_all}"
        response = self.client.run_command(command)
        return response['stdout']

    def sync_primaryStorage_capacity(self, primaryStorageUuid: str) -> Union[Dict, str]:
        """
        刷新主存储容量
        :param primaryStorageUuid: 主存储uuid
        """
        if not primaryStorageUuid:
            raise ParameterIsNoneError(primaryStorageUuid=primaryStorageUuid)
        command = f"{self.zstack_cli} {commands.ZStack_Sync_PrimaryStorage_Capacity.format(stoUuid=primaryStorageUuid)}"
        response = self.client.run_command(command)
        return response['stdout']

    def change_primaryStorage_state(self, uuid: str, stateEvent: str) -> Union[Dict, str]:
        """
        更改主存储状态
        :param uuid: 主存储uuid
        :param stateEvent: 主存储的目标状态 ["enable", "disable", "maintain", "deleting"]
        """
        if not uuid or not stateEvent:
            raise ParameterIsNoneError(uuid=uuid, stateEvent=stateEvent)
        command = f"{self.zstack_cli} {commands.ZStack_Change_PrimaryStorage_State.format(uuid=uuid, state=stateEvent)}"
        response = self.client.run_command(command)
        return response['stdout']

    def update_primaryStorage(self, uuid: str, name: str, description: str = None, url: str = None) -> Union[Dict, str]:
        """
        更新主存储信息
        :param uuid: 主存储uuid
        :param name: 主存储的新名称
        :param description: 主存储的新详细描述
        :param url: 主存储的新地址
        """
        if not uuid or not name:
            raise ParameterIsNoneError(uuid=uuid, name=name)
        command = f"{self.zstack_cli} {commands.ZStack_Update_PrimaryStorage.format(uuid=uuid, name=name)}"
        if description:
            command = f"{command} description={description}"
        if url:
            command = f"{command} url={url}"
        response = self.client.run_command(command)
        return response['stdout']

    def cleanup_image_cahche_on_primaryStorage(self, uuid: str, mode: str = None) -> Union[Dict, str]:
        """
        清除主存储镜像缓存
        :param uuid: 主存储uuid
        :param mode: 模式 ["soft", "hard"]
        """
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)
        command = f"{self.zstack_cli} {commands.ZStack_CleanUp_Image_Cache_on_PrimaryStorage.format(uuid=uuid)}"
        if mode:
            command = f"{command} mode={mode}"
        response = self.client.run_command(command)
        return response['stdout']

    def get_primaryStorage_allocator_strategies(self) -> Union[Dict, str]:
        """
        获取主存储分配策略清单
        """
        command = f"{self.zstack_cli} {commands.ZStack_Get_PrimaryStorage_Allocator_Strategies}"
        response = self.client.run_command(command)
        return response['stdout']

    def get_primaryStorage_types(self) -> Union[Dict, str]:
        """
        获取主存储类型列表
        """
        command = f"{self.zstack_cli} {commands.ZStack_Get_PrimaryStorage_Types}"
        response = self.client.run_command(command)
        return response['stdout']

    def get_primaryStorage_candidates_for_volume_migration(self, volumeUuid: str) -> Union[Dict, str]:
        """
        获取候选列表
        :param volumeUuid: 云盘uuid
        """
        if not volumeUuid:
            raise ParameterIsNoneError(volumeUuid=volumeUuid)
        command = f"{self.zstack_cli} {commands.ZStack_Get_PrimaryStorage_Candidates_For_Volume_Migration.format(voluuid=volumeUuid)}"
        response = self.client.run_command(command)
        return response['stdout']

    def get_host_candidates_for_vm_migration(self, vmInstanceUuid: str, dstPrimaryStorageUuid: str, limit: str = None) -> Union[Dict, str]:
        """
        获取跨存储迁移可选物理机列表
        :param vmInstanceUuid: 云主机UUID
        :param dstPrimaryStorageUuid: 目的主存储UUID
        :param limit: 获取物理机列表数量
        """
        if not vmInstanceUuid or not dstPrimaryStorageUuid:
            raise ParameterIsNoneError(vmInstanceUuid=vmInstanceUuid, dstPrimaryStorageUuid=dstPrimaryStorageUuid)
        command = f"{self.zstack_cli} {commands.ZStack_Get_Host_Candidates_for_Vm_Migration.format(vuuid=vmInstanceUuid, dstuuid=dstPrimaryStorageUuid)}"
        if limit:
            command = f"{command} limit={limit}"
        response = self.client.run_command(command)
        return response['stdout']

    def primaryStorage_migrate_volume(self, volumeUuid: str, dstPrimaryStorageUuid: str) -> Union[Dict, str]:
        """
        跨主存储迁移云盘
        :param volumeUuid: 云盘uuid
        :param dstPrimaryStorageUuid: 目标主存储uuid
        """
        if not volumeUuid or not dstPrimaryStorageUuid:
            raise ParameterIsNoneError(volumeUuid=volumeUuid, dstPrimaryStorageUuid=dstPrimaryStorageUuid)
        command = f"{self.zstack_cli} {commands.ZStack_PrimaryStorage_Migrate_Volume.format(voluuid=volumeUuid, dstuuid=dstPrimaryStorageUuid)}"
        response = self.client.run_command(command)
        return response['stdout']

    def primaryStorage_migrate_vm(self, vmInstanceUuid: str, dstPrimaryStorageUuid: str, withDataVolumes: str = None,
                                  withSnapshots: str = None, dstHostUuid: str = None) -> Union[Dict, str]:
        """
        跨主存储迁移云主机
        :param vmInstanceUuid: 云主机uuid
        :param dstPrimaryStorageUuid: 目标主存储uuid
        :param withDataVolumes: 迁移包含云盘
        :param withSnapshots: 迁移包含快照
        :param dstHostUuid:
        """
        if not vmInstanceUuid or not dstPrimaryStorageUuid:
            raise ParameterIsNoneError(vmInstanceUuid=vmInstanceUuid, dstPrimaryStorageUuid=dstPrimaryStorageUuid)
        command = f"{self.zstack_cli} {commands.ZStack_PrimaryStorage_Migrate_Vm.format(vuuid=vmInstanceUuid, dstuuid=dstPrimaryStorageUuid)}"
        if withDataVolumes:
            command = f"{command} withDataVolumes={withDataVolumes}"
        if withSnapshots:
            command = f"{command} withSnapshots={withSnapshots}"
        if dstHostUuid:
            command = f"{command} dstHostUuid={dstHostUuid}"
        response = self.client.run_command(command)
        return response['stdout']

    def get_primaryStorage_candidates_for_vm_migration(self, vmInstanceUuid: str, withDataVolumes: str = None) -> Union[Dict, str]:
        """
        获取跨主存储迁移云主机候选主存储列表
        :param vmInstanceUuid: 云主机UUID
        :param withDataVolumes:
        """
        if not vmInstanceUuid:
            raise ParameterIsNoneError(vmInstanceUuid=vmInstanceUuid)
        command = f"{self.zstack_cli} {commands.ZStack_Get_PrimaryStorage_Candidates_For_Vm_Migration.format(vuuid=vmInstanceUuid)}"
        if withDataVolumes:
            command = f"{command} withDataVolumes={withDataVolumes}"
        response = self.client.run_command(command)
        return response['stdout']

    def get_primaryStorage_license_info(self, uuid: str) -> Union[Dict, str]:
        """
        获取主存储的License信息
        :param uuid: 主存储UUID
        """
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)
        command = f"{self.zstack_cli} {commands.ZStack_Get_PrimaryStorage_License_Info.format(uuid=uuid)}"
        response = self.client.run_command(command)
        return response['stdout']

    def add_local_primaryStorage(self, url: str, name: str, zoneUuid: str, description: str = None, stotype: str = None,
                                 resourceUuid: str = None) -> Union[Dict, str]:
        """
        添加本地存储为主存储
        :param url: 本地存储的路径
        :param name: 本地存储主存储名称
        :param zoneUuid: 区域uuid
        :param description: 本地存储主存储详细描述
        :param stotype: 类型为LocalStorage
        :param resourceUuid: 资源uuid
        """
        if not url or not name or not zoneUuid:
            raise ParameterIsNoneError(url=url, name=name, zoneUuid=zoneUuid)
        command = f"{self.zstack_cli} {commands.ZStack_Add_Local_PrimaryStorage.format(url=url, name=name, zoneUuid=zoneUuid)}"
        if description:
            command = f"{command} description={description}"
        if stotype:
            command = f"{command} type={stotype}"
        if resourceUuid:
            command = f"{command} resourceUuid={resourceUuid}"
        response = self.client.run_command(command)
        return response['stdout']

    def query_local_Storage_resource_ref(self, primaryStorageUuid: str = None, imageUuid: str = None) -> Union[Dict, str]:
        """
        查询本地存储资源引用
        :param primaryStorageUuid:
        :param imageUuid:
        """
        command = f"{self.zstack_cli} {commands.ZStack_Query_Local_Storage_Resource_Ref}"
        if primaryStorageUuid:
            command = f"{command} primaryStorageUuid={primaryStorageUuid}"
        if imageUuid:
            command = f"{command} image.uuid={imageUuid}"
        response = self.client.run_command(command)
        return response['stdout']

    def local_storage_migrate_volume(self, volumeUuid: str, destHostUuid: str) -> Union[Dict, str]:
        """
        迁移本地存储上存放的云盘
        :param volumeUuid: 云盘uuid
        :param destHostUuid: 目标主机uuid
        """
        if not volumeUuid or not destHostUuid:
            raise ParameterIsNoneError(volumeUuid=volumeUuid, destHostUuid=destHostUuid)
        command = f"{self.zstack_cli} {commands.ZStack_Local_Storage_Migrate_Volume.format(voluuid=volumeUuid, dstuuid=destHostUuid)}"
        response = self.client.run_command(command)
        return response['stdout']

    def get_local_storage_host_disk_capacity(self, hostUuid: str, primaryStorageUuid: str) -> Union[Dict, str]:
        """
        获取主机本地存储容量
        :param hostUuid: 物理主机uuid
        :param primaryStorageUuid: 主存储uuid
        """
        if not hostUuid or not primaryStorageUuid:
            raise ParameterIsNoneError(hostUuid=hostUuid, primaryStorageUuid=primaryStorageUuid)
        command = f"{self.zstack_cli} {commands.ZStack_Get_Local_Storage_Host_Disk_Capacity.format(hostUuid=hostUuid, stoUuid=primaryStorageUuid)}"
        response = self.client.run_command(command)
        return response['stdout']

    def local_storage_get_volume_migratable_hosts(self, volumeUuid: str) -> Union[Dict, str]:
        """
        检查哪些物理主机可以迁移本地存储上存放的云盘
        :param volumeUuid: 云盘uuid
        """
        if not volumeUuid:
            raise ParameterIsNoneError(volumeUuid=volumeUuid)
        command = f"{self.zstack_cli} {commands.ZStack_Local_Storage_Get_Volume_Migratable_Hosts.format(voluuid=volumeUuid)}"
        response = self.client.run_command(command)
        return response['stdout']
