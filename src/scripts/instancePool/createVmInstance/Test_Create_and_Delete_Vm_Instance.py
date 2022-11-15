#!/usr/bin/env python3
# -*- coding:utf-8 -*- 

from typing import List
from src.scripts.base import BaseCases


class TestCreateVMInstance(BaseCases):

    @classmethod
    def setUpClass(cls) -> None:
        super(TestCreateVMInstance, cls).setUpClass()

        # Define test data
        cls.l3Uuid: str = ''
        cls.imageUuid: List[str] = []
        cls.instanceOffering: List[str] = []
        cls.name: str = 'testCreate'

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def test_create_vm_instance(self):
        self.logger.info("查询已存在的虚拟机...")
        result = self.vmController.query_vm_instance()
        self.logger.info(result)

        self.logger.info("查询网络资源-三层网卡资源实例...")
        l3NetworkInfo = self.l3Controller.query_l3Network()
        self.logger.info(l3NetworkInfo)

        for l3Inventory in l3NetworkInfo['inventories']:
            if l3Inventory['uuid']:
                self.l3Uuid = l3Inventory['uuid']

        self.logger.info("查询镜像资源实例...")
        imagesInfo = self.imgController.query_image()
        self.logger.info(imagesInfo)

        for imgInventory in imagesInfo['inventories']:
            if imgInventory['uuid']:
                self.imageUuid.append(imgInventory['uuid'])


        self.logger.info("查询创建的计算规格uuid...")
        instanceOfferingInfo = self.instanceOfferingController.query_instance_offering()
        self.logger.info(instanceOfferingInfo)

        for offInventory in instanceOfferingInfo['inventories']:
            if offInventory['uuid']:
                self.instanceOffering.append(offInventory['uuid'])

        self.logger.info(f"云主机名称: {self.name}\n云主机所使用的镜像Uuid: {self.imageUuid[0]}\n云主机所使用的计算规格Uuid: {self.instanceOffering[0]}\n云主机所使用的三层网络Uuid: {self.l3Uuid}")
        self.logger.info("创建虚拟云主机...")
        response = self.vmController.create_vm_instance(vmName=self.name, imageUuid=self.imageUuid[0],
                                                        l3NetworkUuids=self.l3Uuid, instanceOfferingUuid=self.instanceOffering[0])
        self.assertTrue(response['success'])

    def test_delete_vm_instance(self):
        uuid: str = None
        self.logger.info("获取创建虚拟的uuid...")
        queryResponse = self.vmController.query_vm_instance(vmName=self.name)
        for vmInventory in queryResponse['inventories']:
            uuid = vmInventory['uuid']
        response = self.vmController.destory_vm_instance(uuid=uuid)
        self.assertTrue(response['success'])



