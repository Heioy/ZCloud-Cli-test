#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# Control
ZStack_Show_UI_Config = "show_ui_config"
ZStack_show_Session_list = "show_session_list"
ZStack_Status = "status"
ZStack_Get_Version = "get_version"
ZStack_Drop_Session = "drop_account_session"

# ZStack-Client
ZStack_Login_Account = "LogInByAccount accountName={username} password={password}"
ZStack_LogOut = "LogOut"
ZStack_Query_Zone = "QueryZone name={zone}"
ZStack_Save_History = "save {num}"
ZStack_Query_IPRange = "QueryIpRange"
ZStack_Query_Network_Service = "QueryNetworkServiceProvider"
ZStack_Query_L3_Network_Ref = "QueryNetworkServiceL3NetworkRef"

# VM Pool
## Create Vm
ZStack_Create_Vm_Instance = "CreateVmInstance name={name} imageUuid={uuid} instanceOfferingUuid={ouuid} l3NetworkUuids={l3uuid}"
ZStack_Create_Vm_Instance_From_Volume = "CreateVmInstanceFromVolume name={name} l3NetworkUuids={l3uuid} volumeUuid={vuuid}"
ZStack_Create_Vm_Instance_From_VolumeSnapshot = "CreateVmInstanceFromVolumeSnapshot name={name} l3NetworkUuids={l3uuid} volumeSnapshotUuid={suuid}"
ZStack_Create_Vm_Instance_From_VolumeSnapshotGroup = "CreateVmInstanceFromVolumeSnapshotGroup name={name} l3NetworkUuids={l3uuid} volumeSnapshotGroupUuid={sGuuid}"

## Destory Vm
ZStack_Destory_Vm_Instance = "DestroyVmInstance uuid={uuid}"
ZStack_Expunge_Vm_Instance = "ExpungeVmInstance uuid={uuid}"

## Recovery Vm
ZStack_Recover_Vm_Instance = "RecoverVmInstance uuid={uuid}"

## Query Vm
ZStack_Query_Vm_Instance = "QueryVmInstance"

## Start Vm
ZStack_Start_Vm_Instance = "StartVmInstance uuid={uuid}"

## Stop Vm
ZStack_Stop_Vm_Instance = "StopVmInstance uuid={uuid}"

## Reboot Vm
ZStack_Reboot_Vm_Instance = "RebootVmInstance uuid={uuid}"
ZStack_Pause_Vm_Instance = "PauseVmInstance uuid={uuid}"
ZStack_Resume_Vm_Instance = "ResumeVmInstance uuid={uuid}"
ZStack_Reimage_Vm_Instance = "ReimageVmInstance vmInstanceUuid={vuuid}"
ZStack_Migate_Vm_Instance = "MigrateVm vmInstanceUuid={vuuid}"
ZStack_Get_Migate_Vm_Instance = "GetVmMigrationCandidateHosts vmInstanceUuid={vuuid}"
ZStack_Get_Primary_Storage_For_Create_Vm = "GetCandidatePrimaryStoragesForCreatingVm l3NetworkUuids={l3uuid} imageUuid={iuuid}"
ZStack_Get_Candidate_Iso_For_Attach_Vm = "GetCandidateIsoForAttachingVm vmInstanceUuid={vuuid}"
ZStack_Get_Candidate_Vm_For_Attach_Iso = "GetCandidateVmForAttachingIso isoUuid={isouid}"
ZSatck_Attach_Iso_To_Instance = "AttachIsoToVmInstance vmInstanceUuid={vuuid} isoUuid={isouid}"
ZStack_Detach_Iso_From_Instance = "DetachIsoFromVmInstance vmInstanceUuid={vuuid}"
ZStack_Get_Attached_DataVolume = "GetVmAttachableDataVolume vmInstanceUuid={vuuid}"
ZStack_Get_Attached_L3_Network = "GetVmAttachableL3Network vmInstanceUuid={vuuid}"
ZStack_Attach_L3_Network = " AttachL3NetworkToVm vmInstanceUuid={vuuid} l3NetworkUuid={l3uuid}"
ZStack_Detach_L3_Network = "DetachL3NetworkFromVm vmNicUuid={vNicuuid}"
ZStack_Create_Vm_Nic = "CreateVmNic l3NetworkUuid={l3uuid}"
ZStack_Attach_Nic_To_Vm = " AttachVmNicToVm vmNicUuid={vNicuuid} vmInstanceUuid={vuuid}"
ZStack_Delete_Vm_Nic = "DeleteVmNic l3NetworkUuid={l3uuid}"
ZStack_Query_Vm_Nic = "QueryVmNic"
ZStack_Get_Vm_Nic_Attached_Network_Service = "GetVmNicAttachedNetworkService vmNicUuid={vNicuuid}"
ZStack_Change_Vm_Nic_Network = " ChangeVmNicNetwork vmNicUuid={vNicuuid} destL3NetworkUuid={l3uuid}"
ZStack_Get_Candidate_L3Network_For_Change_Vm_Nic_Network = " GetCandidateL3NetworksForChangeVmNicNetwork vmNicUuid={vNicuuid}"
ZStack_Set_Nic_QoS = "SetNicQos uuid={uuid}"
ZStack_Get_Nic_QoS = "GetNicQos uuid={uuid}"
ZStack_Delete_Nic_QoS = "DeleteNicQos uuid={uuid} direction={dire}"
ZStack_Get_Interdependent_L3Network_Images = " GetInterdependentL3NetworksImages zoneUuid={zoneUuid} "
ZStack_Set_Vm_SshKey = "SetVmSshKey SshKey={sshKey} uuid={uuid}"
ZStack_Get_Vm_SshKey = "GetVmSshKey uuid={uuid}"
ZStack_Delete_Vm_SshKey = "DeleteVmSshKey uuid={uuid}"
ZStack_Change_Vm_Password = "ChangeVmPassword uuid={uuid} account={account} password={password}"
ZStack_Set_Vm_Console_Password = "SetVmConsolePassword uuid={uuid} consolePassword={password}"
ZStack_Get_Vm_Console_Password = "GetVmConsolePassword uuid={uuid}"
ZStack_Delete_Vm_Console_Password = "DeleteVmConsolePassword uuid={uuid}"
ZStack_Get_Vm_Console_Address = "GetVmConsoleAddress uuid={uuid}"
ZStack_Set_Vm_Hostname = "SetVmHostname uuid={uuid} hostname={hostname}"
ZStack_Get_Vm_Hostname = "GetVmHostname uuid={uuid}"
ZStack_Delete_Vm_Hostname = "DeleteVmHostname uuid={uuid}"
ZStack_Get_Vm_Boot_Order = "GetVmBootOrder uuid={uuid}"
ZStack_Set_Vm_Boot_Order = "SetVmBootOrder uuid={uuid} bootOrder={order}"
ZStack_Get_Candidate_Zones_Clusters_Hosts_For_Creating_Vm = "GetCandidateZonesClustersHostsForCreatingVm imageUuid={iuuid} l3NetworkUuids={l3uuid}"




# L2 Network
ZStack_Get_L2_Network_Types = "GetL2NetworkTypes"
ZStack_Query_L2_Network = "QueryL2Network"
ZStack_Query_L2_Vlan_Network = "QueryL2VlanNetwork"
ZStack_Query_L2_Vxlan_Network = "QueryL2VxlanNetwork"
ZStack_Query_L2_Vxlan_Network_Pool = "QueryL2VxlanNetworkPool"
ZStack_Create_L2_NoVlan_Network = "CreateL2NoVlanNetwork"
ZStack_Create_L2_Vlan_Network = "CreateL2VlanNetwork"
ZStack_Create_L2_Vxlan_Network = "CreateL2VxlanNetwork"
ZStack_Create_L2_Vxlan_Network_Pool = "CreateL2VxlanNetworkPool"
ZStack_Attach_L2_Network_2_Cluster = "AttachL2NetworkToCluster"
ZStack_Detach_L2_Network_From_Cluster = "DetachL2NetworkFromCluster"
ZStack_Update_L2_Network = "UpdateL2Network"
ZStack_Delete_L2_Network = "DeleteL2Network"

# L3 Network
ZStack_Query_L3_Network = "QueryL3Network"
ZStack_Get_L3_Network_Types = "GetL3NetworkTypes"
ZStack_Get_L3_Network_UUID = "GetL3NetworkMtu l3NetworkUuid={uuid}"
ZStack_Get_L3_Network_Router = "GetL3NetworkRouterInterfaceIp l3NetworkUuid={l3uuid}"
ZStack_Get_VmAttachable_L3_Network = "GetVmAttachableL3Network vmInstanceUuid={vuuid}"
ZStack_Query_Network_Service_L3_Ref = "QueryNetworkServiceL3NetworkRef"
ZStack_Get_L3_Network_IPStatistic = "GetL3NetworkIpStatistic l3NetworkUuid={l3uuid}"
ZStack_Get_L3_Network_DHCP = "GetL3NetworkDhcpIpAddress l3NetworkUuid={l3uuid}"
ZStack_Update_L3_Network = "UpdateL3Network uuid={uuid}"
ZStack_Set_L3_Network_MTU = "SetL3NetworkMtu l3NetworkUuid={uuid}"
ZStack_Set_L3_Network_Router = "SetL3NetworkRouterInterfaceIp l3NetworkUuid={l3uuid}"
ZStack_Query_Firewall_Rule_Set_L3_Ref = "QueryFirewallRuleSetL3Ref"
ZStack_Create_L3_Network = "CreateL3Network name={name} l2NetworkUuid={l2uuid}"
ZStack_Delete_L3_Network = "DeleteL3Network uuid={uuid}"
ZStack_Attach_L3_Network_To_Vm = "AttachL3NetworkToVm vmInstanceUuid={uuid}"
ZStack_Attach_L3_Network_To_VmNic = "AttachL3NetworkToVmNic vmNicUuid={vNicuuid}"
ZStack_Attach_Network_Service_To_L3_Network = "AttachNetworkServiceToL3Network l3NetworkUuid={uuid}"
ZStack_Add_Dns_To_L3_Network = "AddDnsToL3Network dns={dns} l3NetworkUuid={uuid}"
ZStack_Remove_Dns_To_L3_Network = "RemoveDnsFromL3Network dns={dns} l3NetworkUuid={uuid}"
ZStack_Remove_HostRouter_From_L3_Network = "RemoveHostRouteFromL3Network l3NetworkUuid={uuid}"
ZSatck_Add_HostRouter_From_L3_Network = "AddHostRouteToL3Network l3NetworkUuid={uuid} nexthop={ip} prefix={prefix}"
ZStack_Change_L3_Network_State = "ChangeL3NetworkState uuid={uuid} stateEvent={state}" # state [enable, disable]
ZStack_Detach_L3_Network_From_Vm = "DetachL3NetworkFromVm vmNicUuid={vNicuuid}"

# Host
ZStack_Query_Host = "QueryHost"
ZStack_Reconnect_Host = "ReconnectHost uuid={uuid}"
ZStack_Update_Host = "UpdateHost uuid={uuid}"
ZStack_Delete_Host = "DeleteHost uuid={uuid}"
ZStack_Get_Host_Task = "GetHostTask hostUuids={uuid}"
ZStack_Get_Host_Networks_Facts = "GetHostNetworkFacts hostUuid={uuid}"




# AddHostRouteToL3Network                       AddKVMHost
# AddKVMHostFromConfigFile                      AddSimulatorHost
# AddV2VConversionHost
# AddXDragonHost                                BootstrapMiniHost
# ChangeHostPassword                            ChangeHostState
# ChangeV2VConversionHostState
# CheckKVMHostConfigFile
# DeleteV2VConversionHost                       DeleteVmHostname
# GetCandidateMiniHosts
# GetCandidateZonesClustersHostsForCreatingVm   GetHostAllocatorStrategies
# GetHostIommuState                             GetHostIommuStatus
#
#                                    GetLocalStorageHostDiskCapacity
# GetVmHostname                                 GetVmMigrationCandidateHosts
# GetVmStartingCandidateClustersHosts
# IdentifyHost                                  ListVMsFromKVMHost
# LocalStorageGetVolumeMigratableHosts          PowerOffHost
# QueryMiniStorageHostRef                       QuerySharedBlockGroupPrimaryStorageHostRef
# QueryV2VConversionHost
# RemoveHostRouteFromL3Network
# SetVmHostname
# UpdateHostIommuState                          UpdateKVMHost
# UpdateV2VConversionHost
