#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from typing import List, Tuple
from src.scripts.base import BaseCases


class TestCandidateVMInstance(BaseCases):

    @classmethod
    def setUpClass(cls) -> None:
        super(TestCandidateVMInstance, cls).setUpClass()
        cls.imageUuidList: List[str] = []
        cls.l3NetworkUuidList: List[str] = []
        cls.vmInstanceUuidList: List[str] = []
        cls.imageUuid: str = ""
        cls.l3NetworkUuid: str = ""
        cls.vmInstanceUuid: str = ""

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def test_get_primary_storage(self):
        self.logger.info("查询云主机资源池中可使用的镜像uuid...")
        imageResponse = self.imgController.query_image()
        for inventory in imageResponse['inventories']:
            self.imageUuidList.append(inventory['uuid'])

        self.logger.info("查询三层网络资源的uuid...")
        l3networkResponse = self.l3Controller.query_l3Network()
        for network in l3networkResponse['inventories']:
            self.l3NetworkUuidList.append(network['uuid'])

        self.imageUuid = self.imageUuidList.pop()
        self.l3NetworkUuid = self.l3NetworkUuidList.pop()

        self.logger.info("获取创建云主机时可选择的主存储...")
        psResponse = self.vmController.get_primary_storage_for_create_vm(imageUuid=self.imageUuid,
                                                                         l3NetworkUuids=self.l3NetworkUuid)
        self.assertTrue(psResponse['success'])

    def test_get_data_volume(self):
        self.logger.info("获取云主机实例资源...")
        vmResponse = self.vmController.query_vm_instance()
        for vm in vmResponse['inventories']:
            self.vmInstanceUuidList.append(vm['uuid'])

        self.vmInstanceUuid = self.vmInstanceUuidList.pop()
        self.logger.info("获取云主机可加载云盘列表...")
        dvResponse = self.vmController.get_attached_datavolume(vmInstanceUuid=self.vmInstanceUuid)
        self.assertTrue(dvResponse['success'])