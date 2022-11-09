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
ZStack_Query_Network_Service = "QueryNetworkServiceProvider"
ZStack_Query_L3_Network_Ref = "QueryNetworkServiceL3NetworkRef"

# VM Pool
ZStack_Create_Vm_Instance = "CreateVmInstance name={name} imageUuid={uuid} instanceOfferingUuid={ouuid} \
                             l3NetworkUuids={l3uuid}"
ZStack_Create_Vm_Instance_From_Volume = "CreateVmInstanceFromVolume name={name} l3NetworkUuids={l3uuid} \
                                         volumeUuid={vuuid}"
ZStack_Create_Vm_Instance_From_VolumeSnapshot = "CreateVmInstanceFromVolumeSnapshot name={name} \
                                                 l3NetworkUuids={l3uuid} volumeSnapshotUuid={suuid}"
ZStack_Create_Vm_Instance_From_VolumeSnapshotGroup = "CreateVmInstanceFromVolumeSnapshotGroup name={name} \
                                                      l3NetworkUuids={l3uuid} volumeSnapshotGroupUuid={sGuuid}"
ZStack_Destory_Vm_Instance = "DestroyVmInstance uuid={uuid}"
ZStack_Expunge_Vm_Instance = "ExpungeVmInstance uuid={uuid}"
ZStack_Recover_Vm_Instance = "RecoverVmInstance uuid={uuid}"
ZStack_Query_Vm_Instance = "QueryVmInstance"
ZStack_Start_Vm_Instance = "StartVmInstance uuid={uuid}"
ZStack_Stop_Vm_Instance = "StopVmInstance uuid={uuid}"
ZStack_Reboot_Vm_Instance = "RebootVmInstance uuid={uuid}"
ZStack_Pause_Vm_Instance = "PauseVmInstance uuid={uuid}"
ZStack_Resume_Vm_Instance = "ResumeVmInstance uuid={uuid}"
ZStack_Reimage_Vm_Instance = "ReimageVmInstance vmInstanceUuid={vuuid}"
ZStack_Migate_Vm_Instance = "MigrateVm vmInstanceUuid={vuuid}"
ZStack_Get_Migate_Vm_Instance = "GetVmMigrationCandidateHosts vmInstanceUuid={vuuid}"
ZStack_Get_Primary_Storage_For_Create_Vm = "GetCandidatePrimaryStoragesForCreatingVm l3NetworkUuids={l3uuid} \
                                            imageUuid={iuuid}"
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
ZStack_Get_Candidate_L3Network_For_Change_Vm_Nic_Network = "GetCandidateL3NetworksForChangeVmNicNetwork \
                                                            vmNicUuid={vNicuuid}"
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
ZStack_Get_Candidate_Zones_Clusters_Hosts_For_Creating_Vm = "GetCandidateZonesClustersHostsForCreatingVm \
                                                             imageUuid={iuuid} l3NetworkUuids={l3uuid}"
ZStack_Get_Vm_Starting_Candidate_Clusters_Hosts = "GetVmStartingCandidateClustersHosts uuid={uuid}"
ZStack_Set_Vm_Static_IP = " SetVmStaticIp vmInstanceUuid={vuuid} l3NetworkUuid={l3uuid} ip={ip}"
ZStack_Delete_Static_IP = " DeleteVmStaticIp vmInstanceUuid={vuuid} l3NetworkUuid={l3uuid} deleteMode={deletemode}"
ZSatck_Update_Vm_Instance = "UpdateVmInstance uuid={uuid}"
ZStack_Change_Vm_Image = "ChangeVmImage vmInstanceUuid={vuuid} imageUuid={iuuid}"
ZStack_Get_Image_Candidates_For_Vm_To_Change = " GetImageCandidatesForVmToChange vmInstanceUuid={vuuid}"
ZStack_Get_Vm_Device_Address = "GetVmDeviceAddress uuid={uuid} resourceTypes={restype}"
ZStack_Get_Vms_Capabilities = "GetVmsCapabilities vmUuids={vuuid}"
ZStack_Create_User_Tags = "CreateUserTag tag={tag} resourceType={restype} resourceUuid={resuuid}"

# DataVolume
ZStack_Create_DataVolume = "CreateDataVolume name={volname}"
ZStack_Delete_DataVolume = "DeleteDataVolume uuid={uuid}"
ZStack_Expunge_DataVolume = "ExpungeDataVolume uuid={uuid}"
ZStack_Recover_DataVolume = "RecoverDataVolume uuid={uuid}"
ZStack_Change_Volume_State = "ChangeVolumeState uuid={uuid} stateEvent={state}"
ZStack_Create_DataVolume_From_Volume_Templat = "CreateDataVolumeFromVolumeTemplate name={name} \
                                                imageUuid={iuuid} primaryStorageUuid={stoUuid}"
ZStack_Create_DataVolume_From_Volume_Snapshot = "CreateDataVolumeFromVolumeSnapshot volumeSnapshotUuid={snapUuid} \
                                                 name={name} primaryStorageUuid={stoUuid}"
ZStack_Query_Volume = "QueryVolume"
ZStack_Get_Volume_Format = "GetVolumeFormat"
ZStack_Get_Volume_Capabilities = "GetVolumeCapabilities uuid={uuid}"
ZStack_Sync_Volume_Size = "SyncVolumeSize uuid={uuid}"
ZStack_Resize_RootVolume = "ResizeRootVolume uuid={uuid} size={size}"
ZStack_Resize_DataVolume = "ResizeDataVolume uuid={uuid} size={size}"
ZStack_Update_Volume = "UpdateVolume uuid={uuid}"
ZStack_Set_Volume_QoS = "SetVolumeQos uuid={uuid} volumeBandwidth={volwid}"
ZStack_Get_Volume_QoS = "GetVolumeQos uuid={uuid}"
ZStack_Delete_Volume_QoS = "DeleteVolumeQos uuid={uuid}"
ZStack_Get_DataVolume_Attachable_Vm = "GetDataVolumeAttachableVm volumeUuid={voluuid}"
ZStack_Attach_DataVolume_to_Vm = " AttachDataVolumeToVm volumeUuid={voluuid} vmInstanceUuid={vuuid}"
ZSTack_Detach_DataVolume_From_Vm = "DetachDataVolumeFromVm uuid={uuid} vmUuid={vuuid}"
ZStack_Create_Volume_Snapshot = " CreateVolumeSnapshot volumeUuid={voluuid} name={name}"
ZStack_Query_Volume_Snapshot = "QueryVolumeSnapshot"
ZStack_Query_Volume_Snapshot_Tree = "QueryVolumeSnapshotTree"
ZStack_Update_Volume_Snapshot = "UpdateVolumeSnapshot uuid={uuid}"
ZStack_Delete_Volume_Snapshot = "DeleteVolumeSnapshot uuid={uuid} deleteMode={deletemode}"
ZStack_Revert_Volume_From_Snapshot = "RevertVolumeFromSnapshot uuid={uuid}"
ZStack_Get_Volume_Snapshot_Size = "GetVolumeSnapshotSize uuid={uuid}"
ZStack_Shrink_Volume_Snaspshot = "ShrinkVolumeSnapshot uuid={uuid}"

# Image
ZStack_Add_Image = "AddImage name={name} url={url} backupStorageUuids={stouuid} format={form}"
ZStack_Delete_Image = "DeleteImage uuid={uuid}"
ZStack_Expunge_Image = " ExpungeImage imageUuid={iuuid}"
ZStack_Query_Image = "QueryImage"
ZStack_Recover_Image = "RecoverImage imageUuid={iuuid}"
ZStack_Chaneg_Image_State = "ChangeImageState uuid={uuid} stateEvent={state}"
ZStack_Update_Image = "UpdateImage uuid={uuid}"
ZStack_Sync_Image_Size = "SyncImageSize uuid={uuid}"
ZStack_Get_Candidate_BackupStorage_For_Creating_Image = "GetCandidateBackupStorageForCreatingImage"
ZStack_Create_RootVolume_Template_From_RootVolume = "CreateRootVolumeTemplateFromRootVolume name={name} \
                                                     rootVolumeUuid={voluuid} backupStorageUuids={stouuid}"
ZStack_Create_RootVolume_Template_From_VolumeSnapshot = "CreateRootVolumeTemplateFromVolumeSnapshot name={name} \
                                                         snapshotUuid={snapUuid} backupStorageUuids={stouuid}"
ZStack_Create_DataVolume_Template_From_Volume = "CreateDataVolumeTemplateFromVolume name={name} volumeUuid={voluuid}"
ZStack_Create_DataVolume_Template_From_VolumeSnapshot = "CreateDataVolumeTemplateFromVolumeSnapshot name={name} \
                                                         snapshotUuid={snapUuid} backupStorageUuids={stouuid}"
ZStack_Get_Image_Qga = "GetImageQga uuid={uuid}"
ZStack_Set_Image_Qga = "SetImageQga enable={enable} uuid={uuid}"
ZStack_Set_Image_Boot_Mode = "SetImageBootMode uuid={uuid} bootMode={mode}"
ZStack_Get_Upload_Image_Job_Details = "GetUploadImageJobDetails"

# AffinityGroup
ZStack_Create_AffinityGroup = "CreateAffinityGroup name={name} policy={policy}"
ZStack_Delete_AffinityGroup = "DeleteAffinityGroup uuid={uuid}"
ZStack_Query_AffinityGroup = "QueryAffinityGroup"
ZStack_Update_AffinityGroup = "UpdateAffinityGroup uuid={uuid}"
ZStack_Add_Vm_to_AffinityGroup = " AddVmToAffinityGroup affinityGroupUuid={affUuid} uuid={uuid}"
ZStack_Remove_Vm_from_AffinityGroup = "RemoveVmFromAffinityGroup affinityGroupUuid={affUuid} uuid={uuid}"
ZStack_Change_AffinityGroup_State = "ChangeAffinityGroupState uuid={uuid} stateEvent={state}"
ZStack_Get_Candidate_AffinityGroup_for_Attaching_Vm = "GetCandidateAffinityGroupForAttachingVm vmUuid={vuuid}"
ZStack_Get_Candidate_VM_for_Attaching_AffinityGroup = "GetCandidateVMForAttachingAffinityGroup affinityGroupUuid={affUuid}"
ZStack_Get_Candidate_AffinityGroup_for_Creating_Vm = "GetCandidateAffinityGroupForCreatingVm zoneUuid={zoneUuid}"

# InstanceOffering
ZStack_Create_InstanceOffering = "CreateInstanceOffering name={name} cpuNum={num} memorySize={memSize}"
ZStack_Delete_InstanceOffering = "DeleteInstanceOffering uuid={uuid}"
ZStack_Query_InstanceOffering = "QueryInstanceOffering"
ZStack_Change_InstanceOffering = " ChangeInstanceOffering vmInstanceUuid={vuuid} instanceOfferingUuid={offUuid}"
ZStack_Update_InstanceOffering = "UpdateInstanceOffering uuid={uuid}"
ZStack_Change_InstanceOffering_State = "ChangeInstanceOfferingState stateEvent={state} uuid={uuid}"

# DiskOffering
ZStack_Create_DiskOffering = "CreateDiskOffering name={name} diskSize={size}"
ZStack_Delete_DiskOffering = "DeleteDiskOffering uuid={uuid}"
ZStack_Query_DiskOffering = "QueryDiskOffering"
ZStack_Change_DiskOffering_State = "ChangeDiskOfferingState uuid={uuid} stateEvent={state}"
ZStack_Update_DiskOffering = "UpdateDiskOffering uuid={uuid} name={name}"

# SnapshotGroup
ZStack_Create_SnapshotGroup = "CreateVolumeSnapshotGroup rootVolumeUuid={voluuid} name={name}"
ZStack_Delete_SnapshotGroup = "DeleteVolumeSnapshotGroup uuid={uuid}"
ZStack_Update_SnapshotGroup = "UpdateVolumeSnapshotGroup uuid={uuid} name={name}"
ZStack_Query_SnapshotGroup = "QueryVolumeSnapshotGroup"
ZStack_Check_SnapshotGroup_Availability = "CheckVolumeSnapshotGroupAvailability uuids={uuids}"
ZStack_Revert_Vm_from_SnapshotGroup = "RevertVmFromSnapshotGroup uuid={uuid}"
ZStack_Ungroup_Volume_SnapshotGroup = "UngroupVolumeSnapshotGroup uuid={uuid}"

# Zone
ZStack_Create_Zone = "CreateZone name={name}"
ZStack_Delete_Zone = "DeleteZone uuid={uuid}"
ZStack_Query_Zone = "QueryZone"
ZStack_Update_Zone = "UpdateZone uuid={uuid} name={name}"
ZStack_Change_Zone_State = "ChangeZoneState stateEvent={state} uuid={uuid}"

# Cluster
ZStack_Create_Cluster = "CreateCluster name={name} hypervisorType={hyoerType} zoneUuid={zoneUuid}"
ZStack_Delete_Cluster = "DeleteCluster uuid={uuid}"
ZStack_Query_Cluster = "QueryCluster"
ZStack_Update_Cluster = "UpdateCluster uuid={uuid} name={test}"
ZStack_Change_Cluster_State = "ChangeClusterState uuid={uuid} stateEvent={state}"

# Host
ZStack_Query_Host = "QueryHost"
ZStack_Update_Host = "UpdateHost name={name} uuid={uuid}"
ZStack_Change_Host_State = "ChangeHostState stateEvent={state} uuid={uuid}"
ZStack_Reconnect_Host = "ReconnectHost uuid={uuid}"
ZStack_Delete_Host = "DeleteHost uuid={uuid}"
ZStack_Get_Host_Allocator_Strategies = "GetHostAllocatorStrategie"
ZStack_Get_Hypervisor_Types = "GetHypervisorTypes"
ZStack_Update_KVM_Host = "UpdateKVMHost name={name} uuid={uuid}"
ZStack_Add_KVM_Host = "AddKVMHost username={username} clusterUuid={clusterUuid} name={name} \
                       managementIp={ip} password={password}"
ZStack_KVM_Run_Shell = "KvmRunShell hostUuids={hostUuids} script={script}"
ZStack_Add_KVM_from_ConfigFile = "AddKVMHostFromConfigFile hostInfo={hostInfo}"
ZStack_Check_KVM_Host_ConfigFile = "CheckKVMHostConfigFile hostInfo={hostInfo}"
ZStack_Get_Host_Network_Facts = "GetHostNetworkFacts hostUuid={hostUuid}"
ZStack_Query_Host_Network_Bonding = "QueryHostNetworkBonding"
ZStack_Query_Host_Network_Interface = "QueryHostNetworkInterface"

# Host - PCI Device
ZStack_Query_Pci_Device = "QueryPciDevice"
ZStack_Update_Pci_Device = "UpdatePciDevice uuid={uuid} state={state}"
ZStack_Delete_Pci_Device = "DeletePciDevice uuid={uuid}"
ZStack_Get_Pci_Device_Candidates_for_Attaching_Vm = "GetPciDeviceCandidatesForAttachingVm vmInstanceUuid={vuuid}"
ZStack_Get_Pci_Device_Candidates_for_NewCreate_Vm = "GetPciDeviceCandidatesForNewCreateVm"
ZStack_Attach_Pci_Device_to_Vm = "AttachPciDeviceToVm pciDeviceUuid={pciUuid} vmInstanceUuid={vuuid}"
ZStack_Detach_Pci_Device_from_Vm = " DetachPciDeviceFromVm pciDeviceUuid={pciUuid} vmInstanceUuid={vuuid}"
ZStack_Create_Pci_Device_Offering = "CreatePciDeviceOffering vendorId={vendorId} deviceId={deviceId}"
ZStack_Delete_Pci_Device_Offering = "DeletePciDeviceOffering uuid={uuid}"
ZStack_Query_Pci_Device_Offering = "QueryPciDeviceOffering"

# Host - SR-IOV
ZStack_Is_VfNic_Available_In_L3Network = "IsVfNicAvailableInL3Network l3NetworkUuid={l3uuid} hostUuid={hostUuid}"
ZStack_Change_Vm_Nic_Type = "ChangeVmNicType vmNicUuid={vNicuuid} vmNicType={vNictype}"

# Primary Storage
ZStack_Delete_PrimaryStorage = "DeletePrimaryStorage uuid={uuid}"
ZStack_Query_PrimaryStorage = "QueryPrimaryStorage"
ZStack_Attach_PrimaryStorage_to_Cluster = "AttachPrimaryStorageToCluster clusterUuid={clusterUuid} \
                                           primaryStorageUuid={stoUuid}"
ZStack_Detach_PrimaryStorage_to_Cluster = "AttachPrimaryStorageToCluster clusterUuid={clusterUuid} \
                                           primaryStorageUuid={stoUuid}"
ZStack_Reconnect_PrimaryStorage = "ReconnectPrimaryStorage uuid={uuid}"
ZStack_Get_PrimaryStorage_Capacity = "GetPrimaryStorageCapacity"
ZStack_Sync_PrimaryStorage_Capacity = "SyncPrimaryStorageCapacity primaryStorageUuid={stoUuid}"
ZStack_Change_PrimaryStorage_State = "ChangePrimaryStorageState uuid={uuid} stateEvent={state}"
ZStack_Update_PrimaryStorage = "UpdatePrimaryStorage uuid={uuid} name={name}"
ZStack_CleanUp_Image_Cache_on_PrimaryStorage = "CleanUpImageCacheOnPrimaryStorage uuid={uuid}"
ZStack_Get_PrimaryStorage_Allocator_Strategies = "GetPrimaryStorageAllocatorStrategies"
ZStack_Get_PrimaryStorage_Types = "GetPrimaryStorageTypes"
ZStack_Get_PrimaryStorage_Candidates_For_Volume_Migration = "GetPrimaryStorageCandidatesForVolumeMigration \
                                                             volumeUuid={voluuid}"
ZStack_Get_Host_Candidates_for_Vm_Migration = "GetHostCandidatesForVmMigration vmInstanceUuid={vuuid} \
                                               dstPrimaryStorageUuid={dstuuid}"
ZStack_PrimaryStorage_Migrate_Volume = "PrimaryStorageMigrateVolume volumeUuid={voluuid} \
                                        dstPrimaryStorageUuid={dstuuid}"
ZStack_PrimaryStorage_Migrate_Vm = "PrimaryStorageMigrateVm vmInstanceUuid={vuuid} dstPrimaryStorageUuid={dstuuid}"
ZStack_Get_PrimaryStorage_Candidates_For_Vm_Migration = "GetPrimaryStorageCandidatesForVmMigration vmInstanceUuid={vuuid}"
ZStack_Get_PrimaryStorage_License_Info = "GetPrimaryStorageLicenseInfo uuid={uuid}"

# Local Primary Storage
ZStack_Add_Local_PrimaryStorage = "AddLocalPrimaryStorage url='{url}' name={name} zoneUuid={zoneUuid}"
ZStack_Query_Local_Storage_Resource_Ref = "QueryLocalStorageResourceRef"
ZStack_Local_Storage_Migrate_Volume = "LocalStorageMigrateVolume volumeUuid={voluuid} destHostUuid={dstuuid}"
ZStack_Get_Local_Storage_Host_Disk_Capacity = "GetLocalStorageHostDiskCapacity hostUuid={hostUuid} \
                                               primaryStorageUuid={stoUuid}"
ZStack_Local_Storage_Get_Volume_Migratable_Hosts = "LocalStorageGetVolumeMigratableHosts volumeUuid={voluuid}"

# NFS Primary Storage
ZStack_Add_NFS_PrimaryStorage = "AddNfsPrimaryStorage name={name} zoneUuid={zoneUuid} url={url}"

# Shared Mount Point
ZStack_Add_Shared_MountPoint_PrimaryStorage = "AddSharedMountPointPrimaryStorage name={name} url={url} \
                                               zoneUuid={zoneUuid}"

# Ceph Primary Storage
ZStack_Add_Ceph_PrimaryStorage = "AddCephPrimaryStorage name={name} zoneUuid={zoneUuid} monUrls={monUrls}"
ZStack_Query_Ceph_PrimaryStorage = "QueryCephPrimaryStorage"
ZStack_Add_Mon_to_Ceph_PrimaryStorage = "AddMonToCephPrimaryStorage uuid={uuid} monUrls={monUrls}"
ZStack_Remove_Mon_from_Ceph_PrimaryStorage = "RemoveMonFromCephPrimaryStorage uuid={uuid} monHostnames={monHostnames}"
ZStack_Update_Ceph_PrimaryStorage = "UpdateCephPrimaryStorageMon monUuid={monUuid}"
ZStack_Add_Ceph_PrimaryStorage_Pool = "AddCephPrimaryStoragePool poolName={poolName} primaryStorageUuid={stoUuid} \
                                       isCreate={isCreate}"
ZStack_Delete_Ceph_PrimaryStorage_Pool = "DeleteCephPrimaryStoragePool uuid={uuid}"
ZStack_Query_Ceph_PrimaryStorage_Pool = "QueryCephPrimaryStoragePool"
ZStack_Update_Ceph_PrimaryStorage_Pool = "UpdateCephPrimaryStoragePool uuid={uuid}"

# Backup Storage
ZStack_Delete_BackupStorage = "DeleteBackupStorage uuid={uuid}"
ZStack_Query_BackupStorage = "QueryBackupStorage"
ZStack_Reconnect_BackupStorage = "ReconnectBackupStorage uuid={uuid}"
ZStack_Change_BackupStorage_State = "ChangeBackupStorageState uuid={uuid} stateEvent={state}"
ZStack_Get_BackupStorage_Capacity = "GetBackupStorageCapacity backupStorageUuids={stouuid}"
ZStack_Get_BackupStorage_Types = "GetBackupStorageTypes"
ZStack_Update_BackupStorage = "UpdateBackupStorage uuid={uuid} name={name}"
ZStack_Export_Image_from_BackupStorage = "ExportImageFromBackupStorage backupStorageUuid={stouuid} imageUuid={iuuid}"
ZStack_Delete_Exported_Image_from_BackupStorage = "DeleteExportedImageFromBackupStorage backupStorageUuid={stouuid} \
                                                   imageUuid={iuuid}"
ZStack_Attach_BackupStorage_to_Zone = "AttachBackupStorageToZone backupStorageUuid={stouuid} zoneUuid={zoneUuid}"
ZStack_Detach_BackupStorage_from_Zone = "DetachBackupStorageFromZone backupStorageUuid={stouuid} zoneUuid={zoneUuid}"
ZStack_BackupStorage_Migrate_Image = "BackupStorageMigrateImage imageUuid={iuuid} srcBackupStorageUuid={srcUuid} \
                                      dstBackupStorageUuid={dstUuid}"
ZStack_Get_BackupStorage_Candidates_from_Image_Migration = "GetBackupStorageCandidatesForImageMigration \
                                                            srcBackupStorageUuid={srcUuid}"
ZStack_Add_ImageStore_BakcupStorage = "AddImageStoreBackupStorage hostname='{hostname}' username={username} name={name} \
                                       url='{url}' password={password}"
ZStack_Update_ImageStore_BackupStorage = "UpdateImageStoreBackupStorage uuid={uuid} name={name}"
ZStack_Reconnect_ImageStore_BackupStorage = "ReconnectImageStoreBackupStorage uuid={uuid}"
ZStack_Recliam_Space_from_ImageStore = "ReclaimSpaceFromImageStore uuid={uuid}"
ZStack_Add_Ceph_BackupStorage = "AddCephBackupStorage name={name} monUrls={monUrls}"
ZStack_Query_Ceph_BackupStorage = "QueryCephBackupStorage"
ZStack_Update_Ceph_BackupStorage = "UpdateCephBackupStorageMon monUuid={monUuid}"
ZStack_Add_Mon_to_Ceph_BackupStorage = "AddMonToCephBackupStorage uuid={uuid} monUrls='{monUrls}'"
ZStack_Remove_Mon_from_Ceph_BackupStorage = "RemoveMonFromCephBackupStorage uuid={uuid} monHostnames={monHostnames}"

# Scsi Lun
ZStack_Query_ScsiLun = "QueryScsiLun"
ZStack_Detach_ScsiLun_from_Host = "DetachScsiLunFromHost uuid={uuid}"

# L2 Network
ZStack_Create_L2_Vxlan_Network_Pool = "CreateL2VxlanNetworkPool name={name} zoneUuid={zoneUuid} physicalInterface={interface}"
ZStack_Query_L2_Vxlan_Network_Pool = "QueryL2VxlanNetworkPool"
ZStack_Create_L2_Vxlan_Network = "CreateL2VxlanNetwork name={name} zoneUuid={zoneUuid} physicalInterface={interface} poolUuid={poolUuid}"
ZStack_Query_L2_Vxlan_Network = "QueryL2VxlanNetwork"
ZStack_Create_L2_NoVlan_Network = "CreateL2NoVlanNetwork name={name} physicalInterface={interface} zoneUuid={zoneUuid}"
ZStack_Create_L2_Vlan_Network = "CreateL2VlanNetwork name={name} zoneUuid={zoneUuid} physicalInterface={interface} vlan={vlan}"
ZStack_Query_L2_Vlan_Network = "QueryL2VlanNetwork"
ZStack_Delete_L2_Network = "DeleteL2Network uuid={uuid}"
ZStack_Query_L2_Network = "QueryL2Network"
ZStack_Update_L2_Network = "UpdateL2Network uuid={uuid}"
ZStack_Get_L2_Network_Types = "GetL2NetworkTypes"
ZStack_Attach_L2_Network_2_Cluster = "AttachL2NetworkToCluster clusterUuid={clusterUuid} l2NetworkUuid={l2uuid}"
ZStack_Detach_L2_Network_From_Cluster = "DetachL2NetworkFromCluster clusterUuid={clusterUuid} l2NetworkUuid={l2uuid}"
ZStack_Create_Vni_Range = "CreateVniRange name={name} startVni={startVni} endVni={endVni} l2NetworkUuid={l2uuid}"
ZStack_Query_Vni_Range = "QueryVniRange"
ZStack_Delete_Vni_Range = "DeleteVniRange uuid={uuid}"
ZStack_Update_Vni_Range = "UpdateVniRange uuid={uuid}"

# L3 Network
ZStack_Create_L3_Network = "CreateL3Network name={name} l2NetworkUuid={l2uuid}"
ZStack_Delete_L3_Network = "DeleteL3Network uuid={uuid}"
ZStack_Query_L3_Network = "QueryL3Network"
ZStack_Update_L3_Network = "UpdateL3Network uuid={uuid} name={name}"
ZStack_Get_L3_Network_Types = "GetL3NetworkTypes"
ZStack_Change_L3_Network_State = "ChangeL3NetworkState uuid={uuid} stateEvent={state}"      # state [enable, disable]
ZStack_Get_L3_Network_DHCP = "GetL3NetworkDhcpIpAddress l3NetworkUuid={l3uuid}"
ZStack_Remove_Dns_To_L3_Network = "RemoveDnsFromL3Network dns={dns} l3NetworkUuid={l3uuid}"
ZStack_Add_Dns_To_L3_Network = "AddDnsToL3Network dns={dns} l3NetworkUuid={l3uuid}"
ZSatck_Add_HostRouter_to_L3_Network = "AddHostRouteToL3Network l3NetworkUuid={l3uuid} nexthop={ip} prefix={prefix}"
ZStack_Remove_HostRouter_From_L3_Network = "RemoveHostRouteFromL3Network l3NetworkUuid={l3uuid} prefix={prefix}"
ZStack_Get_Free_IP = "GetFreeIp"
ZStack_Check_IP_Availability = "CheckIpAvailability ip={ip} l3NetworkUuid={l3uuid}"
ZStack_Get_IPAddress_Capacity = "GetIpAddressCapacity"
ZStack_Add_IPRange = "AddIpRange name={name} l3NetworkUuid={l3uuid} startIp={startIp} endIp={endIp} \
                      netmask={netmask} gateway={gateway}"
ZStack_Delete_IPRange = "DeleteIpRange uuid={uuid}"
ZStack_Query_IPRange = "QueryIpRange"
ZStack_Update_IPRange = "UpdateIpRange uuid={uuid}"
ZStack_Add_IPRange_by_Network_Cidr = "AddIpRangeByNetworkCidr name={name} l3NetworkUuid={l3uuid} networkCidr={cidr}"
ZStack_Get_L3Network_MTU = "GetL3NetworkMtu l3NetworkUuid={l3uuid}"
ZStack_Set_L3_Network_MTU = "SetL3NetworkMtu l3NetworkUuid={l3uuid}  mtu={mtu}"
ZStack_Get_L3_Network_Router = "GetL3NetworkRouterInterfaceIp l3NetworkUuid={l3uuid}"
ZStack_Set_L3_Network_Router = "SetL3NetworkRouterInterfaceIp l3NetworkUuid={l3uuid} routerInterfaceIp={router}"
ZStack_Query_IP_Address = "QueryIpAddress"
ZStack_Get_L3Network_IP_Statistic = "GetL3NetworkIpStatistic l3NetworkUuid={l3uuid}"
ZStack_Query_Address_Pool = "QueryAddressPool"

# Virtual Router
ZStack_Query_VirtualRouter = "QueryVirtualRouterVm"
ZStack_Reconnect_VirtualRouter = "ReconnectVirtualRouter vmInstanceUuid={vuuid}"
ZStack_Create_VirtualRouter_Offering = f"CreateVirtualRouterOffering name={name} zoneUuid={zoneUuid} cpuNum={cpuName} \
                                         memorySize={memorySize} imageUuid={iuuid} managementNetworkUuid={netUuid}"
ZStack_Query_VirtualRouter_Offering = "QueryVirtualRouterOffering"
ZStack_Update_VirtualRouter_Offering = "UpdateVirtualRouterOffering uuid={uuid} name={name}"
ZStack_Query_Applicance_VM = "QueryApplianceVm"
ZStack_Get_Attachable_Public_L3_for_VRouter = "GetAttachablePublicL3ForVRouter vmInstanceUuid={vuuid}"
ZStack_Create_VRouterRoute_Table = "CreateVRouterRouteTable name={name}"
ZStack_Delete_VRouterRoute_Table = "DeleteVRouterRouteTable uuid={uuid}"
ZStack_Query_VRouterRoute_Table = "QueryVRouterRouteTable"
ZStack_Get_VRouterRoute_Table = "GetVRouterRouteTable virtualRouterVmUuid={virtualRouterVmUuid}"
ZStack_Add_VRouterRoute_Entry = "AddVRouterRouteEntry routeTableUuid={routeUuid} destination={destination}"
ZStack_Delete_VRouterRoute_Entry = "DeleteVRouterRouteEntry uuid={uuid} routeTableUuid={routeUuid}"
ZStack_Query_VRouterRoute_Entry = "QueryVRouterRouteEntry"
ZStack_Attach_VRouterRoute_Entry_to_Router = "AttachVRouterRouteTableToVRouter virtualRouterVmUuid={vrouteUuid} \
                                              routeTableUuid={routeUuid}"
ZStack_Detach_VRouterRoute_Entry_from_VRouter = "DetachVRouterRouteTableFromVRouter virtualRouterVmUuid={vrouteeUuid} \
                                                 routeTableUuid={routeUuid}"
ZStack_Query_VirtualRouter_VRouterRoute_Table_Ref = "QueryVirtualRouterVRouterRouteTableRef"

# VPC Router
ZStack_Create_VpcVRouter = "CreateVpcVRouter name={name} virtualRouterOfferingUuid={virtualRouterOfferingUuid}"
ZStack_Query_VpcRouter = "QueryVpcRouter"
ZStack_Get_Attachable_VPC_L3Network = "GetAttachableVpcL3Network uuid={uuid}"
ZStack_Get_VPCVRouter_Distributed_Routing_Connections = "GetVpcVRouterDistributedRoutingConnections uuid={uuid}"
ZStack_Get_VPCVRouter_Distributed_Routing_Enabled = "GetVpcVRouterDistributedRoutingEnabled uuid={uuid}"
ZStack_Set_VPCVRouter_Distributed_Routing_Enabled = "SetVpcVRouterDistributedRoutingEnabled uuid={uuid} stateEvent={state}"
ZStack_Add_DNS_to_VPCRouter = "AddDnsToVpcRouter dns={dns} uuid={uuid}"
ZStack_Remove_DNS_from_VPCRouter = "RemoveDnsFromVpcRouter dns={dns} uuid={uuid}"
ZStack_Get_VPCVRouter_NetworkService_State = "GetVpcVRouterNetworkServiceState uuid={uuid} networkService={service}"
ZStack_Set_VPCVRouter_NetworkService_State = "SetVpcVRouterNetworkServiceState uuid={uuid} networkService={service} state={state}"
ZStack_Change_VPC_HAGroup_Monitorlps = "ChangeVpcHaGroupMonitorIps uuid={uuid}"
ZStack_Create_VPC_HAGroup = "CreateVpcHaGroup name={name}"
ZStack_Delete_VPC_HAGroup = "DeleteVpcHaGroup uuid={uuid}"
ZStack_Update_VPC_HAGroup = "UpdateVpcHaGroup uuid={uuid}"
ZStack_Query_VPC_HAGroup = "QueryVpcHaGroup"
ZStack_Update_Virtual_Router = "UpdateVirtualRouter vmInstanceUuid={vuuid}"

# VRouter OSPF
ZStack_Create_VRouter_OSPF_Area = "CreateVRouterOspfArea areaId={areaId}"
ZStack_Delete_VRouter_OSPF_Area = "DeleteVRouterOspfArea uuid={uuid}"
ZStack_Get_VRouter_OSPF_Neighbor = "GetVRouterOspfNeighbor vRouterUuid={vRouterUuid}"
ZStack_Query_VRouter_OSPF_Area = "QueryVRouterOspfArea"
ZStack_Get_VRouter_RouterID = "GetVRouterRouterId vRouterUuid={vRouterUuid}"
ZStack_Set_VRouter_RouterID = "SetVRouterRouterId vRouterUuid={vRouterUuid} routerId={routerId}"
ZStack_Add_VRouter_Networks_to_OSPF_Area = "AddVRouterNetworksToOspfArea routerAreaUuid={routerAreaUuid} \
                                            vRouterUuid={vRouterUuid} l3NetworkUuids={l3uuid}"
ZStack_Remove_VRouter_Networks_from_OSPF_Area = "RemoveVRouterNetworksFromOspfArea uuids={uuids}"
ZStack_Update_VRouter_OSPF_Area = "UpdateVRouterOspfArea uuid={uuid}"
ZStack_Query_VRouter_OSPF_Network = "QueryVRouterOspfNetwork"

# Host
ZStack_Query_Host = "QueryHost"
ZStack_Reconnect_Host = "ReconnectHost uuid={uuid}"
ZStack_Update_Host = "UpdateHost uuid={uuid}"
ZStack_Delete_Host = "DeleteHost uuid={uuid}"
ZStack_Get_Host_Task = "GetHostTask hostUuids={uuid}"
ZStack_Get_Host_Networks_Facts = "GetHostNetworkFacts hostUuid={uuid}"
