#!/usr/bin/env python3
# -*- coding:utf-8 -*- 

from typing import Union, Dict
from logging import Logger
from src.api.client import ZStackClient
from src.config import commands
from src.utils.errors import ParameterIsNoneError


class Host(ZStackClient):

    def __init__(self, logger: Logger = None):
        super(Host, self).__init__(logger=logger)

    def query_host(self, managementIp: str = None, vmNicIp: str = None, **kwargs) -> Union[Dict, str]:
        """
        查询主机
        :param managementIp: 管理IP
        :param vmNicIp: 云主机实例所使用的IP
        """
        command = f"{self.zstack_cli} {commands.ZStack_Query_Host}"
        if managementIp:
            command = f"{command} managementIp={managementIp}"
        if vmNicIp:
            command = f"{command} vmInstance.vmNics.ip={vmNicIp}"
        if kwargs:
            for key, value in kwargs.items():
                command += f" {key}={value}"
        response = self.client.run_command(command)
        return response['stdout']

    def update_host(self, uuid: str, name: str, description: str = None, managementIp: str = None) -> Union[Dict, str]:
        """
        更新物理主机的名称、描述和标签等参数
        :param uuid: 物理主机的uuid
        :param name: 资源名字
        :param description: 资源描述
        :param managementIp:
        """
        if not uuid or not name:
            raise ParameterIsNoneError(uuid=uuid, name=name)
        command = f"{self.zstack_cli} {commands.ZStack_Update_Host.format(uuid=uuid, name=name)}"
        if description:
            command = f"{command} description={description}"
        if managementIp:
            command = f"{command} managementIp={managementIp}"
        response = self.client.run_command(command)
        return response['stdout']

    def change_host_state(self, uuid: str, stateEvent: str) -> Union[Dict, str]:
        """
        改变物理主机的可用状态
        :param uuid: 物理主机的uuid
        :param stateEvent: 可用状态触发事件 ["enable", "disable", "maintain"]
        """
        if not uuid or not stateEvent:
            raise ParameterIsNoneError(uuid=uuid, stateEvent=stateEvent)
        command = f"{self.zstack_cli} {commands.ZStack_Change_Host_State.format(uuid=uuid, state=stateEvent)}"
        response = self.client.run_command(command)
        return response['stdout']

    def reconnect_host(self, uuid: str) -> Union[Dict, str]:
        """
        重新建立云平台管理节点和主机间的命令通道
        :param uuid: 物理主机的uuid
        """
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)
        command = f"{self.zstack_cli} {commands.ZStack_Reconnect_Host.format(uuid=uuid)}"
        response = self.client.run_command(command)
        return response['stdout']

    def delete_host(self, uuid: str, deleteMode: str = None) -> Union[Dict, str]:
        """
        删除物理主机
        :param uuid: 物理主机的uuid
        :param deleteMode: 资源删除模式 ["Permissive", "Enforcing"]
        """
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)
        command = f"{self.zstack_cli} {commands.ZStack_Delete_Host.format(uuid=uuid)}"
        if deleteMode:
            command = f"{command} deleteMode={deleteMode}"
        response = self.client.run_command(command)
        return response['stdout']

    def get_host_alloator_strategies(self) -> Union[Dict, str]:
        """
        获取物理主机分配策略
        """
        command = f"{self.zstack_cli} {commands.ZStack_Get_Host_Allocator_Strategies}"
        response = self.client.run_command(command)
        return response['stdout']

    def get_hypervisor_type(self) -> Union[Dict, str]:
        """
        获取云主机虚拟化技术类型
        """
        command = f"{self.zstack_cli} {commands.ZStack_Get_Hypervisor_Types}"
        response = self.client.run_command(command)
        return response['stdout']

    def update_kvm_host(self, uuid: str, name: str, username: str = None, password: str = None, sshPort: str = None,
                        description: str = None, managementIp: str = None) -> Union[Dict, str]:
        """
        更新KVM主机信息
        :param uuid: 物理主机uuid
        :param name: 资源名称
        :param username: 用户名
        :param password: 密码
        :param sshPort: ssh端口号
        :param description: 资源的详细描述
        :param managementIp: 管理节点IP
        """
        if not uuid or not name:
            raise ParameterIsNoneError(uuid=uuid, name=name)
        command = f"{self.zstack_cli} {commands.ZStack_Update_KVM_Host.format(uuid=uuid, anme=name)}"
        if username:
            command = f"{command} username={username}"
        if password:
            command = f"{command} password={password}"
        if sshPort:
            command = f"{command} sshPort={sshPort}"
        if description:
            command = f"{command} description={description}"
        if managementIp:
            command = f"{command} managementIp={managementIp}"
        response = self.client.run_command(command)
        return response['stdout']

    def add_kvm_host(self, username: str, password: str, name: str, managementIp: str, clusterUuid: str,
                     sshPort: int = 22, description: str = None, resourceUuid: str = None) -> Union[Dict, str]:
        """
        添加KVM主机
        :param username: ssh用户名
        :param password: ssh密码
        :param name: 资源名称
        :param managementIp: 管理节点IP
        :param clusterUuid: 集群uuid
        :param sshPort: ssh端口号
        :param description: 资源的详细描述
        :param resourceUuid: 资源的uuid
        """
        if not username or not password or not name or not managementIp or not clusterUuid:
            raise ParameterIsNoneError(username=username, password=password, name=name, managementIp=managementIp,
                                       clusterUuid=clusterUuid)
        command = f"{self.zstack_cli} {commands.ZStack_Add_KVM_Host.format(username=username, name=name, clusterUuid=clusterUuid, password=password, ip=managementIp)}"
        command = f"{command} sshPort={sshPort}"
        if description:
            command = f"{command} description={description}"
        if resourceUuid:
            command = f"{command} resourceUuid={resourceUuid}"
        response = self.client.run_command(command)
        return response['stdout']

    def kvm_run_shell(self, hostUuids: str, script: str) -> Union[Dict, str]:
        """
        在KVM中运行命令
        :param hostUuids: 目标机器uuid
        :param script: 执行的命令
        """
        if not hostUuids or not script:
            raise ParameterIsNoneError(hostUuids=hostUuids, script=script)
        command = f"{self.zstack_cli} {commands.ZStack_KVM_Run_Shell(hostUuids=hostUuids, script=script)}"
        response = self.client.run_command(command)
        return response['stdout']

    def add_kvm_from_configFile(self, hostInfo: str, resourceUuid: str = None) -> Union[Dict, str]:
        """
        通过文件导入方式添加物理机
        :param hostInfo: 经过base64编码的物理机信息 #todo utils 增加操作base64方法
        :param resourceUuid: 资源的uuid
        """
        if not hostInfo:
            raise ParameterIsNoneError(hostInfo=hostInfo)
        command = f"{self.zstack_cli} {commands.ZStack_Add_KVM_from_ConfigFile.format(hostInfo=hostInfo)}"
        if resourceUuid:
            command = f"{command} resourceUuid={resourceUuid}"
        response = self.client.run_command(command)
        return response['stdout']

    def check_kvm_host_configFile(self, hostInfo: str) -> Union[Dict, str]:
        """
        添加物理机文件语法检查
        :param hostInfo: 经过base64编码的物理机信息
        """
        if not hostInfo:
            raise ParameterIsNoneError(hostInfo=hostInfo)
        command = f"{self.zstack_cli} {commands.ZStack_Check_KVM_Host_ConfigFile.format(hostInfo=hostInfo)}"
        response = self.client.run_command(command)
        return response['stdout']

    def get_host_network_facts(self, hostUuid: str) -> Union[Dict, str]:
        """
        获取物理机物理网络信息
        :param hostUuid: 物理机UUID
        """
        if not hostUuid:
            raise ParameterIsNoneError(hostUuid=hostUuid)
        command = f"{self.zstack_cli} {commands.ZStack_Get_Host_Network_Facts.format(hostUuid=hostUuid)}"
        response = self.client.run_command(command)
        return response['stdout']

    def query_host_network_bonding(self, hostUuid: str = None, **kwargs) -> Union[Dict, str]:
        """
        查询物理机Bond信息
        :param hostUuid: 物理机uuid
        :param kwargs:
        """
        command = f"{self.zstack_cli} {commands.ZStack_Query_Host_Network_Bonding}"
        if hostUuid:
            command = f"{command} hostUuid={hostUuid}"
        if kwargs:
            for key, value in kwargs.items():
                command += f" {key}={value}"
        response = self.client.run_command(command)
        return response['stdout']

    def query_host_network_interface(self, hostUuid: str = None, **kwargs) -> Union[Dict, str]:
        """
        查询物理机网卡信息
        :param hostUuid: 物理机uuid
        :param kwargs:
        """
        command = f"{self.zstack_cli} {commands.ZStack_Query_Host_Network_Interface}"
        if hostUuid:
            command = f"{command} hostUuid={hostUuid}"
        if kwargs:
            for key, value in kwargs.items():
                command += f" {key}={value}"
        response = self.client.run_command(command)
        return response['stdout']


class PCIDevice(ZStackClient):

    def __init__(self, logger: Logger = None):
        super(PCIDevice, self).__init__(logger=logger)

    def query_pci_device(self, **kwargs) -> Union[Dict, str]:
        """
        查询PCI设备
        :param kwargs:
        """
        command = f"{self.zstack_cli} {commands.ZStack_Query_Pci_Device}"
        if kwargs:
            for key, value in kwargs.items():
                command += f" {key}={value}"
        response = self.client.run_command(command)
        return response['stdout']

    def update_pci_device(self, uuid: str, state: str, description: str = None, metaData: str = None) -> Union[
        Dict, str]:
        """
        更新PCI设备
        :param uuid: 资源的UUID，唯一标示该资源
        :param state: 资源状态 ["Enabled", "Disabled"]
        :param description: 资源的详细描述
        :param metaData:
        """
        if not uuid or not state:
            raise ParameterIsNoneError(uuid=uuid, state=state)
        command = f"{self.zstack_cli} {commands.ZStack_Update_Pci_Device.format(uuid=uuid, state=state)}"
        if description:
            command = f"{command} description={description}"
        if metaData:
            command = f"{command} metaData={metaData}"
        response = self.client.run_command(command)
        return response['stdout']

    def delete_pci_device(self, uuid: str, deleteMode: str = None) -> Union[Dict, str]:
        """
        删除PCI设备
        :param uuid: 资源的UUID，唯一标示该资源
        :param deleteMode: 删除模式
        """
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)
        command = f"{self.zstack_cli} {commands.ZStack_Delete_Pci_Device.format(uuid=uuid)}"
        if deleteMode:
            command = f"{command} deleteMode={deleteMode}"
        response = self.client.run_command(command)
        return response['stdout']

    def get_pci_device_candidates_for_attaching_vm(self, vmInstanceUuid: str, device_types: str = None) -> Union[
        Dict, str]:
        """
        获取PCI设备列表
        :param vmInstanceUuid: 云主机UUID
        :param device_types: PCI Device 设备类型
        """
        if not vmInstanceUuid:
            raise ParameterIsNoneError(vmInstanceUuid=vmInstanceUuid)
        command = f"{self.zstack_cli} {commands.ZStack_Get_Pci_Device_Candidates_for_Attaching_Vm.format(vuuid=vmInstanceUuid)}"
        if device_types:
            command = f"{command} types={device_types}"
        response = self.client.run_command(command)
        return response['stdout']

    def get_pci_device_candidates_for_newcreate_vm(self, hostUuid: str = None, clusterUuids: str = None,
                                                   types: str = None) -> Union[Dict, str]:
        """
        获取可加载PCI设备
        :param hostUuid: 物理机UUID
        :param clusterUuids: 集群UUID
        :param types: PCI Device设备类型
        """
        command = f"{self.zstack_cli} {commands.ZStack_Get_Pci_Device_Candidates_for_NewCreate_Vm}"
        if hostUuid:
            command = f"{command} hostUuid={hostUuid}"
        if clusterUuids:
            command = f"{command} clusterUuids={clusterUuids}"
        if types:
            command = f"{command} types={types}"
        response = self.client.run_command(command)
        return response['stdout']

    def attach_pci_device_to_vm(self, pciDeviceUuid: str, vmInstanceUuid: str) -> Union[Dict, str]:
        """
        绑定PCI设备到云主机
        :param pciDeviceUuid: PCI设备UUID
        :param vmInstanceUuid: 云主机UUID
        """
        if not pciDeviceUuid or not vmInstanceUuid:
            raise ParameterIsNoneError(pciDeviceUuid=pciDeviceUuid, vmInstanceUuid=vmInstanceUuid)
        command = f"{self.zstack_cli} {commands.ZStack_Attach_Pci_Device_to_Vm.format(pciUuid=pciDeviceUuid, vuuid=vmInstanceUuid)}"
        response = self.client.run_command(command)
        return response['stdout']

    def detach_pci_device_from_vm(self, pciDeviceUuid: str, vmInstanceUuid: str) -> Union[Dict, str]:
        """
        卸载PCI设备
        :param pciDeviceUuid: PCI设备UUID
        :param vmInstanceUuid: 云主机UUID
        """
        if not pciDeviceUuid or not vmInstanceUuid:
            raise ParameterIsNoneError(pciDeviceUuid=pciDeviceUuid, vmInstanceUuid=vmInstanceUuid)
        command = f"{self.zstack_cli} {commands.ZStack_Detach_Pci_Device_from_Vm.format(pciUuid=pciDeviceUuid, vuuid=vmInstanceUuid)}"
        response = self.client.run_command(command)
        return response['stdout']

    def create_pci_device_offering(self, vendorId: str, deviceId: str, name: str = None, description: str = None,
                                   device_type: str = None, subvendorId: str = None, subdeviceId: str = None,
                                   resourceUuid: str = None) -> Union[Dict, str]:
        """
        创建PCI设备规格
        :param vendorId: 供应商ID
        :param deviceId: 产品ID
        :param name: 资源名称
        :param description: 资源的详细描述
        :param device_type: 设备类型
        :param subvendorId: 子供应商ID
        :param subdeviceId: 子设备ID
        :param resourceUuid: 资源UUID
        """
        if not vendorId or not deviceId:
            raise ParameterIsNoneError(vendorId=vendorId, deviceId=deviceId)
        command = f"{self.zstack_cli} {commands.ZStack_Create_Pci_Device_Offering.format(vendorId=vendorId, deviceId=deviceId)}"
        if name:
            command = f"{command} name={name}"
        if description:
            command = f"{command} description={description}"
        if device_type:
            command = f"{command} type={device_type}"
        if subdeviceId:
            command = f"{command} subdeviceId={subdeviceId}"
        if subvendorId:
            command = f"{command} subvendorId={subvendorId}"
        if resourceUuid:
            command = f"{command} resourceUuid={resourceUuid}"
        response = self.client.run_command(command)
        return response['stdout']

    def delete_pci_device_offering(self, uuid: str, deleteMode: str = None) -> Union[Dict, str]:
        """
        删除PCI设备规格
        :param uuid: 资源的UUID，唯一标示该资源
        :param deleteMode: 删除模式
        """
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)
        command = f"{self.zstack_cli} {commands.ZStack_Delete_Pci_Device_Offering.format(uuid=uuid)}"
        if deleteMode:
            command = f"{command} deleteMode={deleteMode}"
        response = self.client.run_command(command)
        return response['stdout']

    def query_pci_device_offering(self, **kwargs) -> Union[Dict, str]:
        """
        查询PCI设备规格信息
        :param kwargs:
        """
        command = f"{self.zstack_cli} {commands.ZStack_Query_Pci_Device_Offering}"
        if kwargs:
            for key, value in kwargs.items():
                command += f" {key}={value}"
        response = self.client.run_command(command)
        return response['stdout']


class VmUSB(ZStackClient):

    def __init__(self, logger: Logger = None):
        super(VmUSB, self).__init__(logger=logger)


class SRIOV(ZStackClient):

    def __init__(self, logger: Logger = None):
        super(SRIOV, self).__init__(logger=logger)

    def is_vf_nic_available_in_l3network(self, l3NetworkUuid: str, hostUuid: str) -> Union[Dict, str]:
        """
        查询L3网络中是否存在可用VF网卡
        :param l3NetworkUuid: 三层网络UUID
        :param hostUuid: 物理机UUID
        """
        if not l3NetworkUuid or not hostUuid:
            raise ParameterIsNoneError(l3NetworkUuid=l3NetworkUuid, hostUuid=hostUuid)
        command = f"{self.zstack_cli} {commands.ZStack_Is_VfNic_Available_In_L3Network.format(l3uuid=l3NetworkUuid, hostUuid=hostUuid)}"
        response = self.client.run_command(command)
        return response['stdout']

    def change_vm_nic_type(self, vmNicUuid: str, vmNicType: str) -> Union[Dict, str]:
        """
        修改云主机网卡类型
        :param vmNicUuid: 云主机网卡UUID
        :param vmNicType: 云主机网卡类型  "VNIC"
        """
        if not vmNicUuid or not vmNicType:
            raise ParameterIsNoneError(vmNicType=vmNicType, vmNicUuid=vmNicUuid)
        command = f"{self.zstack_cli} {commands.ZStack_Change_Vm_Nic_Type.format(vNicuuid=vmNicUuid, vNictype=vmNicType)}"
        response = self.client.run_command(command)
        return response['stdout']
