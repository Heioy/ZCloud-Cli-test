#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from typing import List
from src.scripts.base import BaseCases


class TestUpdateInstanceOffering(BaseCases):

    @classmethod
    def setUpClass(cls) -> None:
        super(TestUpdateInstanceOffering, cls).setUpClass()

        cls.instanceOfferingUuidList: List[str] = []
        cls.instanceOfferingNameList: List[str] = []
        cls.instanceOfferingName: str = "1G-1CPU"
        cls.cpuNum: int = 1
        cls.memorySize: int = 102400

        cls.vmInstanceUuidList: List[str] = []

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def test_update_instanceOffering(self):
        """更新计算规格的配置"""
        self.logger.info("查询已存在的计算规格...")
        offeringInfo = self.OfferingController.query_diskoffering()
        for inventory in offeringInfo['inventories']:
            if inventory['name'] not in self.instanceOfferingNameList:
                self.instanceOfferingNameList.append(inventory['name'])
            if inventory['uuid'] not in self.instanceOfferingUuidList:
                self.instanceOfferingUuidList.append(inventory['uuid'])

        self.logger.info("创建计算规格...")
        response = self.instanceOfferingController.create_instance_offering(name=self.instanceOfferingName,
                                                                            cpuNum=self.cpuNum,
                                                                            memorySize=self.memorySize)
        self.assertTrue(response['true'])
        self.instanceOfferingUuid = response['inventories']['uuid']

        self.logger.info("修改云主机计算规格配置...")
        vmInstanceUuid = self.vmController.query_vm_instance()
        for inventory in vmInstanceUuid['inventories']:
            if inventory['uuid'] not in self.vmInstanceUuidList:
                self.vmInstanceUuidList.append(inventory['uuid'])

        changed = self.instanceOfferingController.change_instance_offering(instanceOfferingUuid=self.instanceOfferingUuid,
                                                                           vmInstanceUuid=self.vmInstanceUuidList.pop())
        self.assertTrue(changed['success'])

        self.logger.info("更新计算的规格...")
        response = self.instanceOfferingController.update_instance_offering(uuid=self.instanceOfferingUuid)
        self.assertTrue(response['success'])
