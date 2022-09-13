#!/usr/bin/env python3
# -*- coding:utf-8 -*- 

from logging import Logger
from typing import Union, Any, Dict, List
from src.api.client import ZStackClient
from src.config.command import *
from src.utils.errors import ParameterIsNoneError, RemoteCommandError

"""云主机资源类"""


class Instances(ZStackClient):

    def __init__(self, logger: Logger = None):
        super(Instances, self).__init__(logger=logger)
        self.create_vm_timeout = 10 * 60
        # self.logger = logger

    def create_vm_instance(self, vmName: str, imageUuid: str, l3NetworkUuids: str, instanceOfferingUuid: str,
                           defaultL3NetworkUuid: str = None, systemTags: str = None) -> Union[Dict, str]:
        """
        Create VM Instance
        :param vmName: 资源的名字
        :param imageUuid: 镜像uuid。云主机的根云盘会从该字段指定的镜像创建
        :param l3NetworkUuids: 三层网络uuid列表。可以指定一个或多个三层网络，云主机会在每个网络上创建一个网卡
        :param instanceOfferingUuid: 计算规格uuid 。指定云主机的CPU、内存等参数
        :param defaultL3NetworkUuid: 如果l3NetworkUuids包含了多个L3网络的UUID，这个参数指定哪个L3网络是默认的L3网络。如果l3NetworkUuids只有一个L3网络UUID ，可不设置这个参数。
        :param systemTags: "consolePassword::123456", "ha::NeverStop", "vmConsoleMode::vnc", "staticIp ::ac5c7e736f1b499bbd0c12763b30051d::172.24.0.5"
        :return:
        """
        self.logger.info("创建云主机...")
        if not vmName or not imageUuid or not l3NetworkUuids or not instanceOfferingUuid:
            raise ParameterIsNoneError(vmName=vmName, imageUuid=imageUuid, l3NetworkUuids=l3NetworkUuids)

        if len(l3NetworkUuids.split(',')) > 1 and not defaultL3NetworkUuid:
            defaultL3NetworkUuid = l3NetworkUuids.split(',')[0]
        elif len(l3NetworkUuids.split(',') > 1 and defaultL3NetworkUuid):
            defaultL3NetworkUuid = defaultL3NetworkUuid
        else:
            defaultL3NetworkUuid = None

        command = f"{self.zstack_cli} {ZStack_Create_Vm_Instance.format(name=vmName, uuid=imageUuid, ouuid=instanceOfferingUuid, l3uuid=l3NetworkUuids)}"

        if defaultL3NetworkUuid:
            command = f"{command} defaultL3NetworkUuid={defaultL3NetworkUuid}"

        if systemTags:
            command = f"{command} systemTags={systemTags}"

        response = self.client.run_command(command, timeout=self.create_vm_timeout)
        return response['stdout']

    def create_vm_instance_from_volume(self, vmName: str, l3NetworkUuids: str, volumeUuid: str,
                                       instanceOfferingUuid: str = None,
                                       defaultL3NetworkUuid: str = None, systemTags: str = None
                                       ) -> Union[Dict, str]:
        """
        Create Vm Instance From Volume
        :param vmName: 资源名称
        :param l3NetworkUuids: 三层网络UUID
        :param volumeUuid: 云盘UUID
        :param instanceOfferingUuid: 计算规格UUID 。指定云主机的CPU、内存等参数
        :param defaultL3NetworkUuid: 如果l3NetworkUuids包含了多个L3网络的UUID，这个参数指定哪个L3网络是默认的L3网络。如果l3NetworkUuids只有一个L3网络UUID ，可不设置这个参数。
        :param systemTags: 系统标签
        """
        self.logger.info("从云盘创建云主机...")
        if not vmName or not l3NetworkUuids or not volumeUuid:
            raise ParameterIsNoneError(vmName=vmName, l3NetworkUuids=l3NetworkUuids, volumeUuid=volumeUuid)
        command = f"{self.zstack_cli} {ZStack_Create_Vm_Instance_From_Volume.format(name=vmName, l3uuid=l3NetworkUuids, vuuid=volumeUuid)}"

        if instanceOfferingUuid:
            command = f"{command} instanceOfferingUuid={instanceOfferingUuid}"

        if defaultL3NetworkUuid:
            command = f"{command} defaultL3NetworkUuid={defaultL3NetworkUuid}"

        if systemTags:
            command = f"{command} systemTags={systemTags}"

        response = self.client.run_command(command, timeout=self.create_vm_timeout)
        return response['stdout']

    def create_vm_instance_from_volume_Snapshot(self, vmName: str, l3NetworkUuids: str, volumeSnapshotUuid: str,
                                               instanceOfferingUuid: str = None, type: str = None, primaryStorageVolume: str = None,
                                               defaultL3NetworkUuid: str = None, strategy: str = None) -> Union[Dict, str]:
        """
        Create Vm Instnace From Volume Snapshot
        :param vmName: 资源名称
        :param l3NetworkUuids: 三层网络UUID
        :param volumeSnapshotUuid: 云盘快照UUID
        :param instanceOfferingUuid: 计算规格UUID
        :param type: 云主机类型 ["UserVm", "ApplianceVm"]
        :param primaryStorageVolume: 主存储UUID
        :param defaultL3NetworkUuid: 默认三层网络UUID
        :param strategy: 创建策略 ["InstantStart", "CreateStopped"]
        """
        self.logger.info("从快照创建云主机...")
        if not vmName or not l3NetworkUuids or not volumeSnapshotUuid:
            raise ParameterIsNoneError(vmName=vmName, l3NetworkUuids=l3NetworkUuids, volumeSnapshotUuid=volumeSnapshotUuid)

        command = f"{self.zstack_cli} {ZStack_Create_Vm_Instance_From_VolumeSnapshot.format(name=vmName, l3uuid=l3NetworkUuids, suuid=volumeSnapshotUuid)}"

        if instanceOfferingUuid:
            command = f"{command} instanceOfferingUuid={instanceOfferingUuid}"
        if type:
            command = f"{command} type={type}"
        if primaryStorageVolume:
            command = f"{command} primaryStorageVolume={primaryStorageVolume}"
        if defaultL3NetworkUuid:
            command = f"{command} defaultL3NetworkUuid={defaultL3NetworkUuid}"
        if strategy:
            command = f"{command} strategy={strategy}"

        response = self.client.run_command(command, timeout=self.create_vm_timeout)
        return response['stdout']

    def create_vm_instance_from_volume_SnapshotGroup(self, vmName: str, l3NetworkUuids: str, volumeSnapshotGroupUuid: str,
                                                     instanceOfferingUuid: str = None, type: str = None,
                                                     primaryStorageUuidForRootVolume: str = None, defaultL3NetworkUuid: str = None,
                                                     strategy: str = None, systemTags: str = None
                                                    ) -> Union[Dict, str]:
        """
        Create Vm Instance From Volume SnapshotGroup
        :param vmName: 资源名称
        :param l3NetworkUuids: 三层网络UUID
        :param volumeSnapshotGroupUuid: 快照组UUID
        :param instanceOfferingUuid: 计算规格UUID。指定云主机的CPU、内存等参数
        :param type: 云主机类型。保留字段，无需指定 ["UserVm", "ApplianceVm"]
        :param primaryStorageUuidForRootVolume: 根盘的主存储UUID
        :param defaultL3NetworkUuid: 默认三层网络UUID
        :param strategy: 云主机创建策略，创建后立刻启动或创建后不启动。 ["InstantStart", "CreateStopped"]
        :param systemTags: 系统标签
        """
        self.logger.info("从快照组创建云主机...")
        if not vmName or not l3NetworkUuids or not volumeSnapshotGroupUuid:
            raise ParameterIsNoneError(vmName=vmName, l3NetworkUuids=l3NetworkUuids, volumeSnapshotGroupUuid=volumeSnapshotGroupUuid)

        command = f"{self.zstack_cli} {ZStack_Create_Vm_Instance_From_VolumeSnapshotGroup.format(name=vmName, l3uuid=l3NetworkUuids, sGuuid=volumeSnapshotGroupUuid)}"

        if instanceOfferingUuid:
            command = f"{command} instanceOfferingUuid={instanceOfferingUuid}"
        if type:
            command = f"{command} type={type}"
        if primaryStorageUuidForRootVolume:
            command = f"{command} primaryStorageUuidForRootVolume={primaryStorageUuidForRootVolume}"
        if defaultL3NetworkUuid:
            command = f"{command} defaultL3NetworkUuid={defaultL3NetworkUuid}"
        if strategy:
            command = f"{command} strategy={strategy}"
        if systemTags:
            command = f"{command} systemTags={systemTags}"

        response = self.client.run_command(command, timeout=self.create_vm_timeout)

    def destory_vm_instance(self, uuid: str, deleteMode: str = None)  -> Union[Dict, str]:
        """
        Remove Vm Instance From Pool
        :param uuid: 云主机的uuid
        :param deleteMod: 删除模式 ["Permissive", "Enforcing"]
        """
        self.logger.info("删除云主机...")
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)

        command = f"{self.zstack_cli} {ZStack_Destory_Vm_Instance.format(uuid=uuid)}"

        if deleteMode:
            command = f"{command} deleteMode={deleteMode}"

        response = self.client.run_command(command)


    def recover_vm_instance(self, uuid: str) -> Union[Dict, str]:
        """
        Recovery Vm Instance From Destory Pool
        :param uuid: 云主机的uuid
        """
        self.logger.info("正在恢复已删除的云主机...")
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)

        command = f"{self.zstack_cli} {ZStack_Recover_Vm_Instance.format(uuid=uuid)}"

        response = self.client.run_command(command)

    def expunge_Vm_Instance(self, uuid: str) -> Union[Dict, str]:
        """
        Expunge Vm Instance From Destoryed Vm Pool
        :param uuid: 云主机的uuid
        """
        self.logger.info("彻底删除云主机...")
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)

        command = f"{self.zstack_cli} {ZStack_Expunge_Vm_Instance.format(uuid=uuid)}"

        response = self.client.run_command(command)

    def query_vm_instance(self, uuid: str = None, state: str = None, vmName: str = None, vmNicIp: str = None) -> Union[Dict, str]:
        """
        Query Vm Instance
        :param uuid: 虚拟机的uuid
        :param state: 虚拟机运行状态
        :param vmName: 虚拟机名称
        :param vmNicIp: 虚拟机使用的l3层网络ip
        """
        self.logger.info("正在查询云主机...")
        command = f"{self.zstack_cli} {ZStack_Query_Vm_Instance}"

        if uuid:
            command = f"{command} uuid={uuid}"
        if state:
            command = f"{command} state={state}"
        if vmName:
            command = f"{command} name={vmName}"
        if vmNicIp:
            command = f"{command} vmNics.ip={vmNicIp}"

        response = self.client.run_command(command)
        # if response['returncode'] != 0:
        #     raise RemoteCommandError(command, response['stdout'])
        return response['stdout']

    def start_instance(self, uuid: str, clusterUuid: str = None, hostUuid: str = None) -> Union[Dict, str]:
        """
        Start Vm Instance
        :param uuid: 云主机的uuid
        :param clusterUuid: 集群UUID。若指定，云主机将在该集群启动。
        :param hostUuid: 物理主机UUID。 若指定，云主机将在该物理主机启动。
        """
        self.logger.info("正在启动云主机...")
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)

        command = f"{self.zstack_cli} {ZStack_Start_Vm_Instance.format(uuid=uuid)}"

        if clusterUuid:
            command = f"{command} clusterUuid={clusterUuid}"
        if hostUuid:
            command = f"{command} hostUuid={hostUuid}"

        response = self.client.run_command(command)

        # if response['returncode'] != 0:
        #     raise RemoteCommandError(command, response['stdout'])
        return response['stdout']

    def stop_instance(self, uuid: str, _type: str = None, stopHA: bool = False)  -> Union[Dict, str]:
        """
        Stoppped Vm Instance
        :param uuid: 云主机的uuid
        :param type: 停止云主机的方式。grace:优雅关机,需要云主机里安装了相关ACPI驱动; cold:冷关机,相当于直接断电。
        :param stopHA: 彻底关闭HA云主机
        """
        self.logger.info("正在关闭云主机...")
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)

        command = f"{self.zstack_cli} {ZStack_Stop_Vm_Instance.format(uuid=uuid)}"

        if _type not in ['grace', 'cold']:
            raise ValueError(f"参数<type: {_type}>传入的值不合法!")
        else:
            command = f"{command} type={_type}"

        if stopHA:
            command = f"{command} stopHA={stopHA}"

        response = self.client.run_command(command)
        return response['stdout']

    def reboot_instance(self, uuid: str) -> Union[Dict, str]:
        """
        Reboot Instance
        :param uuid:
        """
        self.logger.info("正在重启云主机...")
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)

        command = f"{self.zstack_cli} {ZStack_Reboot_Vm_Instance.format(uuid=uuid)}"

        response = self.client.run_command(command)
        return response['stdout']

    def pause_instance(self, uuid: str) -> Union[Dict, str]:
        """
        Pause Vm Instance From Memory
        :param uuid: 云主机的uuid
        """
        self.logger.info("正在将云主机状态挂起...")
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)

        command = f"{self.zstack_cli} {ZStack_Pause_Vm_Instance.format(uuid=uuid)}"
        response = self.client.run_command(command)

        return response['stdout']

    def resume_instance(self, uuid: str) -> Union[Dict, str]:
        """
        Resume Vm Instance From Memory
        :param uuid: 云主机的uuid
        """
        self.logger.info("正在恢复挂起的云主机...")
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)

        command = f"{self.zstack_cli} {ZStack_Resume_Vm_Instance.format(uuid=uuid)}"
        response = self.client.run_command(command)

        return response['stdout']

    def reimage_instance(self, vmInstanceUuid: str)  -> Union[Dict, str]:
        """
        Initialize Root Vm Instance Image. Only valid for Created by ISO Image
        :param vmInstanceUuid: 云主机的uuid
        """
        self.logger.info("正在重置云主机...")
        if not vmInstanceUuid:
            raise ParameterIsNoneError(vmInstanceUuid=vmInstanceUuid)

        command = f"{self.zstack_cli} {ZStack_Reimage_Vm_Instance.format(vuuid=vmInstanceUuid)}"
        response = self.client.run_command(command)

        return response['stdout']

    def megiate_instance(self)  -> Union[Dict, str]:
        """Migrate Vm Instance From Another Host Machine"""
        self.logger.info("正在迁移云主机中...")
        pass

    def get_megiate_hosts(self)  -> Union[Dict, str]:
        """Getting Host List From could Megiate Candidate"""
        self.logger.info("获取可迁移的云主机的主机列表...")
        pass

    def get_primary_storage_for_create_vm(self, imageUuid: str, l3NetworkUuids: str, dataDiskOfferingUuids: str = None,
                                          defaultL3NetworkUuid: str = None, rootDiskOfferingUuid: str = None,
                                          zoneUuid: str = None, clusterUuid: str = None)  -> Union[Dict, str]:
        """
        Get Candidate Primary Storages For Creating Vm
        :param imageUuid: 镜像UUID
        :param l3NetworkUuids: 三层网络UUID
        :param dataDiskOfferingUuids: 数据云盘使用的云盘规格UUID
        :param defaultL3NetworkUuid: 默认三层网络UUID
        :param rootDiskOfferingUuid: 根云盘使用的云盘规格UUID，镜像类型为ISO时可选且必选
        :param zoneUuid: 区域UUID
        :param clusterUuid: 集群UUID
        """
        self.logger.info("正在获取创建云主机时的主存储...")
        if not imageUuid or not l3NetworkUuids:
            raise ParameterIsNoneError(imageUuid=imageUuid, l3NetworkUuids=l3NetworkUuids)

        command = f"{self.zstack_cli} {ZStack_Get_Primary_Storage_For_Create_Vm.format(l3uuid=l3NetworkUuids, iuuid=imageUuid)}"
        if dataDiskOfferingUuids:
            command = f"{command} dataDiskOfferingUuids={dataDiskOfferingUuids}"
        if defaultL3NetworkUuid:
            command = f"{command} defaultL3NetworkUuid={defaultL3NetworkUuid}"
        if rootDiskOfferingUuid:
            command = f"{command} rootDiskOfferingUuid={rootDiskOfferingUuid}"
        if zoneUuid:
            command = f"{command} zoneUuid={zoneUuid}"
        if clusterUuid:
            command = f"{command} clusterUuid={clusterUuid}"

        response = self.client.run_command(command)
        return response['stdout']

    def get_candidate_iso_for_attach_vm(self, vmInstanceUuid: str)  -> Union[Dict, str]:
        """
        Get ISO List For Attaching Vm
        :param vmInstanceUuid: 云主机的uuid
        """
        self.logger.info("正在获取云主机可加载的ISO列表...")
        if not vmInstanceUuid:
            raise ParameterIsNoneError(vmInstanceUuid=vmInstanceUuid)

        command = f"{self.zstack_cli} {ZStack_Get_Candidate_Iso_For_Attach_Vm.format(vuuid=vmInstanceUuid)}"
        response = self.client.run_command(command)

        return response['stdout']

    def get_candidate_vm_for_attach_iso(self, isoUuid: str)  -> Union[Dict, str]:
        """
        Get Candidate Vm For Attaching Iso
        :param isoUuid:
        """
        self.logger.info("正在获取云主机可以加载的ISO列表...")
        if not isoUuid:
            raise ParameterIsNoneError(isoUuid=isoUuid)

        command = f"{self.zstack_cli} {ZStack_Get_Candidate_Vm_For_Attach_Iso.format(isouid=isoUuid)}"
        response = self.client.run_command(command)

        return response['stdout']

    def attach_iso_to_instance(self, vmInstanceUuid: str, isoUuid: str)  -> Union[Dict, str]:
        """
        Attached Iso Image To VmInstance which Status in Running or Stopped
        :param vmInstanceUuid:
        :param isoUuid:
        """
        self.logger.info("正在加载ISO镜像到云主机...")
        if not vmInstanceUuid or not isoUuid:
            raise ParameterIsNoneError(vmInstanceUuid=vmInstanceUuid, isoUuid=isoUuid)

        command = f"{self.zstack_cli} {ZSatck_Attach_Iso_To_Instance.format(vuuid=vmInstanceUuid, isouid=isoUuid)}"
        response = self.client.run_command(command)

        return response['stdout']

    def detach_iso_from_instance(self, vmInstanceUuid: str)  -> Union[Dict, str]:
        """
        Detach ISO From Instance
        :param vmInstanceUuid: 云主机的uuid
        """
        self.logger.info("正在卸载云主机上的ISO镜像...")
        if not vmInstanceUuid:
            raise ParameterIsNoneError(vmInstanceUuid=vmInstanceUuid)

        command = f"{self.zstack_cli} {ZStack_Detach_Iso_From_Instance.format(vuuid=vmInstanceUuid)}"

        response = self.client.run_command(command)
        return response['stdout']

    def get_attached_datavolume(self, vmInstanceUuid: str)  -> Union[Dict, str]:
        """
        Get Vm Instance Attachable DataVolume
        :param vmInstanceUuid: 云主机的uuid
        """
        self.logger.info("正在获取云主机可以加载的云盘列表...")
        if not vmInstanceUuid:
            raise ParameterIsNoneError(vmInstanceUuid=vmInstanceUuid)

        command = f"{self.zstack_cli} {ZStack_Get_Attached_DataVolume.format(vuuid=vmInstanceUuid)}"
        response = self.client.run_command(command)

        return response['stdout']

    def get_attached_l3_network(self, vmInstanceUuid: str)  -> Union[Dict, str]:
        """
        Get Vm Instance Attachable L3 Network
        :param vmInstanceUuid:  云主机的uuid
        """
        self.logger.info("正在获取云主机可以加载的L3网络列表...")
        if not vmInstanceUuid:
            raise ParameterIsNoneError(vmInstanceUuid=vmInstanceUuid)

        command = f"{self.zstack_cli} {ZStack_Get_Attached_L3_Network.format(vuuid=vmInstanceUuid)}"
        response = self.client.run_command(command)

        return response['stdout']

    def attach_l3_to_instance(self, vmInstanceUuid: str, l3NetworkUuid: str, driverType: str = None, staticIp: str = None)  -> Union[Dict, str]:
        """
        Attach L3 Network To Vm Instance which state in Running or Stopped
        :param vmInstanceUuid: 云主机的uuid
        :param l3NetworkUuid: 三层网络的uuid
        :param driverType: 网卡驱动类型 ["E1000E", "E1000", "Vmxnet3", "Sriov"]  version >= 4.0.0
        :param staticIp: 指定分配给云主机的IP地址
        """
        self.logger.info("添加L3网络到Running/Stopped状态的云主机上...")
        if not vmInstanceUuid or not l3NetworkUuid:
            raise ParameterIsNoneError(vmInstanceUuid=vmInstanceUuid, l3NetworkUuid=l3NetworkUuid)

        command = f"{self.zstack_cli} {ZStack_Attach_L3_Network.format(vuuid=vmInstanceUuid, l3uuid=l3NetworkUuid)}"
        if driverType:
            command = f"{command} driverType={driverType}"
        if staticIp:
            command = f"{command} staticIp={staticIp}"

        response = self.client.run_command(command)

        return response['stdout']

    def detach_l3_from_instance(self, vmNicUuid: str)  -> Union[Dict, str]:
        """
        Detach L3 Network From Vm Instance
        :param vmNicUuid: 云主机网卡uuid ，该网卡所在网络会从云主机卸载掉
        """
        self.logger.info("正在卸载云主机上的L3层网络设备...")
        if not vmNicUuid:
            raise ParameterIsNoneError(vmNicUuid=vmNicUuid)

        command = f"{self.zstack_cli} {ZStack_Detach_L3_Network.format(vmNicuuid=vmNicUuid)}"
        response = self.client.run_command(command)

        return response['stdout']

    def create_nic(self, l3NetworkUuid: str, resourceUuid: str = None, ip: str = None)  -> Union[Dict, str]:
        """
        Create Vm Nic
        :param l3NetworkUuid: 三层网络UUID
        :param resourceUuid:
        :param ip:
        """
        self.logger.info("正在创建云主机虚拟网卡...")
        if not l3NetworkUuid:
            raise ParameterIsNoneError(l3NetworkUuid=l3NetworkUuid)

        command = f"{self.zstack_cli} {ZStack_Create_Vm_Nic.format(l3uuid=l3NetworkUuid)}"
        if resourceUuid:
            command = f"{command} resourceUuid={resourceUuid}"
        if ip:
            command = f"{command} ip={ip}"

        response = self.client.run_command(command)

        return response['stdout']

    def attach_nic_to_instance(self, vmNicUuid: str, vmInstanceUuid: str)  -> Union[Dict, str]:
        """
        Attach Vm Nic To Vm @todo 4.0.0-version
        :param vmNicUuid: 云主机网卡UUID
        :param vmInstanceUuid: 云主机UUID
        """
        self.logger.info("加载网卡到云主机...")
        if not vmInstanceUuid or not vmNicUuid:
            raise ParameterIsNoneError(vmInstanceUuid=vmInstanceUuid, vmNicUuid=vmNicUuid)

        command = f"{self.zstack_cli} {ZStack_Attach_Nic_To_Vm.format(vNicuuid=vmNicUuid, vuuid=vmInstanceUuid)}"
        response = self.client.run_command(command)

        return response['stdout']

    def delete_nic(self, l3NetworkUuid: str)  -> Union[Dict, str]:
        """
        Delete Vm Nic @todo 4.0.0-version
        :param l3NetworkUuid: 资源的UUID，唯一标示该资源
        """
        self.logger.info("正在删除云主机上的网卡...")
        if not l3NetworkUuid:
            raise ParameterIsNoneError(l3NetworkUuid=l3NetworkUuid)

        command = f"{self.zstack_cli} {ZStack_Delete_Vm_Nic.format(l3uuid=l3NetworkUuid)}"
        response = self.client.run_command(command)

        return response['stdout']

    def query_nic(self, gateway: str = None, guestIp: str = None)  -> Union[Dict, str]:
        """
        QueryVmNic
        :param gateway: 云主机网卡对应的网关
        :param guestIp: 云主机客户端的IP
        """
        self.logger.info("查询云主机的网卡...")
        command = f"{self.zstack_cli} {ZStack_Query_Vm_Nic}"

        if gateway:
            command = f"{command} gateway={gateway}"
        if guestIp:
            command = f"{command} eip.guestIp={guestIp}"

        response = self.client.run_command(command)
        return response['stdout']

    def get_nic_attached_network_service(self, vmNicUuid: str)  -> Union[Dict, str]:
        """
        GetVmNicAttachedNetworkService @todo 4.1.0-version
        :param vmNicUuid:
        """
        self.logger.info("获取网卡加载的网络服务名称...")
        if not vmNicUuid:
            raise ParameterIsNoneError(vmNicUuid=vmNicUuid)

        command = f"{self.zstack_cli} {ZStack_Get_Vm_Nic_Attached_Network_Service.format(vNicuuid=vmNicUuid)}"
        response = self.client.run_command(command)

        return response['stdout']

    def change_nic_network(self, vmNicUuid: str, destL3NetworkUuid: str) -> Union[Dict, str]:
        """
        ChangeVmNicNetwork @todo 4.1.0-version
        :param vmNicUuid: 云主机网卡UUID
        :param destL3NetworkUuid: 3层网络网卡对应的UUID
        """
        self.logger.info("修改已停止状态云主机的网卡三层网络...")
        if not vmNicUuid or not destL3NetworkUuid:
            raise ParameterIsNoneError(vmNicUuid=vmNicUuid, destL3NetworkUuid=destL3NetworkUuid)

        command = f"{self.zstack_cli} {ZStack_Change_Vm_Nic_Network.format(vNicuuid=vmNicUuid, l3uuid=destL3NetworkUuid)}"
        response = self.client.run_command(command)

        return response['stdout']

    def get_candidate_l3_network_for_change_instance_nic_network(self, vmNicUuid: str) -> Union[Dict, str]:
        """
        GetCandidateL3NetworksForChangeVmNicNetwork @todo 4.1.0-version
        :param vmNicUuid: 云主机网卡UUID
        """
        self.logger.info("获取云主机网卡可挂载的三层网络...")
        if not vmNicUuid:
            raise ParameterIsNoneError(vmNicUuid=vmNicUuid)

        command = f"{self.zstack_cli} {ZStack_Get_Candidate_L3Network_For_Change_Vm_Nic_Network.format(vNicuuid=vmNicUuid)}"
        response = self.client.run_command(command)

        return response['stdout']

    def set_nic_qos(self, uuid: str, outboundBandwidth: int = None, inboundBandwidth: int = None) -> Union[Dict, str]:
        """
        SetNicQoS
        :param uuid: 云主机网卡的uuid
        :param outboundBandwidth: 出流量带宽限制
        :param inboundBandwidth: 入流量宽带限制
        """
        self.logger.info("设置云主机网卡限速...")
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)

        command = f"{self.zstack_cli} {ZStack_Set_Nic_QoS.format(uuid=uuid)}"
        if outboundBandwidth:
            command = f"{command} outboundBandwidth={outboundBandwidth}"
        if inboundBandwidth:
            command = f"{command} inboundBandwidth={inboundBandwidth}"

        response = self.client.run_command(command)

        return response['stdout']

    def get_nic_qos(self, uuid: str) -> Union[Dict, str]:
        """
        GetNicQoS
        :param uuid: 云主机网卡的uuid
        """
        self.logger.info("获取云主机网卡限速...")
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)

        command = f"{self.zstack_cli} {ZStack_Get_Nic_QoS.format(uuid=uuid)}"
        response = self.client.run_command(command)

        return response['stdout']

    def delete_nic_qos(self, uuid: str, direction: str) -> Union[Dict, str]:
        """
        DeleteNicQoS
        :param uuid: 云主机网卡的uuid
        :param direction: 入方向还是出方向 ["in", "out"]
        """
        self.logger.info("正在删除云主机网卡限速设置...")
        if not uuid or not direction:
            raise ParameterIsNoneError(uuid=uuid, direction=direction)

        command = f"{self.zstack_cli} {ZStack_Delete_Nic_QoS.format(uuid=uuid, dire=direction)}"
        response = self.client.run_command(command)

        return response['stdout']

    def get_interdependent_l3_network_images(self, zoneUuid: str, l3NetworkUuids: str = None, imageUuid: str = None) -> Union[Dict, str]:
        """
        Get Interdependent L3 Networks Images
        :param zoneUuid: 区域uuid。必须指定，以确定三层网络和镜像依赖关系。
        :param l3NetworkUuids: 三层网络的uuid列表
        :param imageUuid: 镜像uuid
        """
        self.logger.info("获取镜像和三层网络的相互依赖...")
        if not zoneUuid:
            raise ParameterIsNoneError(zoneUuid=zoneUuid)

        command = f"{self.zstack_cli} {ZStack_Get_Interdependent_L3Network_Images.format(zoneUuid=zoneUuid)}"

        if l3NetworkUuids:
            command = f"{command} l3NetworkUuids={l3NetworkUuids}"
        if imageUuid:
            command = f"{command} imageUuid={imageUuid}"

        response = self.client.run_command(command)

        return response['stdout']

    def set_vm_sshkey(self, uuid: str, SshKey: str) -> Union[Dict, str]:
        """
        Set Vm SshKey
        :param uuid: 云主机的uuid
        :param SshKey:
        """
        self.logger.info("设置云主机SSH Key...")
        if not uuid or not SshKey:
            raise ParameterIsNoneError(uuid=uuid, SshKey=SshKey)

        command = f"{self.zstack_cli} {ZStack_Set_Vm_SshKey.format(sshKey=SshKey, uuid=uuid)}"
        response = self.client.run_command(command)

        return response['stdout']

    def get_vm_sshkey(self, uuid: str) -> Union[Dict, str]:
        """
        Get Vm SshKey
        :param uuid: 云主机的uuid
        """
        self.logger.info("获取云主机SSH Key...")
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)

        command = f"{self.zstack_cli} {ZStack_Get_Vm_SshKey.format(uuid=uuid)}"
        response = self.client.run_command(command)

        return response['stdout']

    def delete_vm_sshkey(self, uuid: str) -> Union[Dict, str]:
        """
        Delete Vm SshKey
        :param uuid: 云主机的uuid
        """
        self.logger.info("删除云主机SSH Key...")
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)

        command = f"{self.zstack_cli} {ZStack_Delete_Vm_SshKey.format(uuid=uuid)}"
        response = self.client.run_command(command)

        return response['stdout']

    def change_vm_password(self, uuid: str, password: str, account: str = 'root') -> Union[Dict, str]:
        """
        变更云主机密码
        :param uuid: 云主机的uuid
        :param password:
        :param account:
        """
        self.logger.info("更新云主机密码...")
        if not uuid or not password:
            raise ParameterIsNoneError(uuid=uuid, password=password)

        command = f"{self.zstack_cli} {ZStack_Change_Vm_Password.format(uuid=uuid, account=account, password=password)}"
        response = self.client.run_command(command)

        return response['stdout']

    def set_vm_console_password(self) -> Union[Dict, str]:
        pass

    def get_vm_console_password(self) -> Union[Dict, str]:
        pass

    def delete_vm_console_password(self) -> Union[Dict, str]:
        pass

    def get_vm_console_address(self) -> Union[Dict, str]:
        pass

    def set_vm_hostname(self, uuid: str, hostname: str) -> Union[Dict, str]:
        """
        设置云主机hostname
        :param uuid: 云主机的uuid
        :param hostname: hostname，必须 符合RFC1123标准
        """
        self.logger.info("设置云主机Hostname...")
        if not uuid or not hostname:
            raise ParameterIsNoneError(uuid=uuid, hostname=hostname)

        command = f"{self.zstack_cli} {ZStack_Set_Vm_Hostname.format(uuid=uuid, hostname=hostname)}"
        response = self.client.run_command(command)

        return response['stdout']

    def get_vm_hostname(self, uuid: str) -> Union[Dict, str]:
        """
        获取云主机hostname
        :param uuid: 云主机的uuid
        """
        self.logger.info("获取云主机hostname...")

        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)

        command = f"{self.zstack_cli} {ZStack_Get_Vm_Hostname.format(uuid=uuid)}"
        response = self.client.run_command(command)

        return response['stdout']

    def delete_vm_hostname(self, uuid: str) -> Union[Dict, str]:
        """
        删除云主机hostname
        :param uuid: 云主机的uuid
        """
        self.logger.info("删除云主机hostname...")

        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)

        command = f"{self.zstack_cli} {ZStack_Delete_Vm_Hostname.format(uuid=uuid)}"
        response = self.client.run_command(command)

        return response['stdout']

    def get_vm_boot_order(self, uuid: str) -> Union[Dict, str]:
        """
        获取一个云主机的启动设备列表
        :param uuid: 云主机的uuid
        """
        self.logger.info("获取一个云主机的启动设备列表...")
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)

        command = f"{self.zstack_cli} {ZStack_Get_Vm_Boot_Order.format(uuid=uuid)}"
        response = self.client.run_command(command)

        return response['stdout']

    def set_vm_boot_order(self, uuid: str, bootOrder: str = 'HardDisk') -> Union[Dict, str]:
        """
        指定云主机的启动设备
        :param uuid: 云主机的uuid
        :param bootOrder: 启动设备。CdRom:光驱，HardDisk:云盘，Network:网络。若该字段不指定，则表示使用系统默认启动设备顺序(HardDisk, CdRom, Network)
        """
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)

        command = f"{self.zstack_cli} {ZStack_Set_Vm_Boot_Order.format(uuid=uuid, order=bootOrder)}"
        response = self.client.run_command(command)

        return response['stdout']

    def get_candidate_zones_clusters_hosts_for_creating_vm(self, imageUuid: str, l3NetworkUuids: str, instanceOfferingUuid: str = None,
                                                           dataDiskOfferingUuids: str = None, zoneUuid: str = None, clusterUuid: str = None,
                                                           defaultL3NetworkUuid: str = None, cpuNum: str = None, memorySize: str = None,
                                                           rootDiskOfferingUuid: str = None) -> Union[Dict, str]:
        """
        获取可以创建云主机参数的目的区域、集群、物理主机。可以通过指定云主机参数获得可以创建满足参数云主机的目的地
        :param imageUuid: 镜像uuid
        :param l3NetworkUuids: 三层网络列表
        :param instanceOfferingUuid: 计算规格uuid
        :param dataDiskOfferingUuids: 云盘规格列表
        :param rootDiskOfferingUuid: 根云盘规格。仅在imageUuid指定的镜像是ISO时需要指定
        :param zoneUuid: 区域uuid
        :param clusterUuid: 集群uuid
        :param defaultL3NetworkUuid: 默认三层网络uuid
        :param cpuNum: CPU数目
        :param memorySize: 内存大小, 单位Byte
        """
        self.logger.info("获取可以创建云主机参数的目的区域...")
        if not imageUuid or not l3NetworkUuids:
            raise ParameterIsNoneError(imageUuid=imageUuid, l3NetworkUuids=l3NetworkUuids)

        command = f"{self.zstack_cli} {ZStack_Get_Candidate_Zones_Clusters_Hosts_For_Creating_Vm.format(iuuid=imageUuid, l3uuid=l3NetworkUuids)}"

        if instanceOfferingUuid:
            command = f"{command} instanceOfferingUuid={instanceOfferingUuid}"
        if dataDiskOfferingUuids:
            command = f"{command} dataDiskOfferingUuids={dataDiskOfferingUuids}"
        if rootDiskOfferingUuid:
            command = f"{command} rootDiskOfferingUuid={rootDiskOfferingUuid}"
        if zoneUuid:
            command = f"{command} zoneUuid={zoneUuid}"
        if clusterUuid:
            command = f"{command} clusterUuid={clusterUuid}"
        if defaultL3NetworkUuid:
            command = f"{command} defaultL3NetworkUuid={defaultL3NetworkUuid}"
        if cpuNum:
            command = f"{command} cpuNum={cpuNum}"
        if memorySize:
            command = f"{command} memorySize={memorySize}"

        response = self.client.run_command(command)
        return response['stdout']




# if __name__ == '__main__':
#     cli = Instances()
#     res = cli.query_vm_instance(uuid='f73ee1c3ad4f4a3dac96a66608332867')
#     print(type(res))

