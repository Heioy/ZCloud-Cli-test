#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List
from src.scripts.base import BaseCases


class TestCreateInstanceOffering(BaseCases):

    @classmethod
    def setUpClass(cls) -> None:
        super(TestCreateInstanceOffering, cls).setUpClass()

        cls.instanceOfferingUuidList: List[str] = []
        cls.instanceOfferingNameList: List[str] = []
        cls.instanceOfferingName: str = "1G-1CPU"
        cls.cpuNum: int = 1
        cls.memorySize: int = 102400

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def test_create_instanceOffering(self):
        """创建计算规格"""
        self.logger.info("查询已存在的计算规格...")
        offeringInfo = self.OfferingController.query_diskoffering()
        for inventory in offeringInfo['inventories']:
            if inventory['name'] not in self.instanceOfferingNameList:
                self.instanceOfferingNameList.append(inventory['name'])
            if inventory['uuid'] not in self.instanceOfferingUuidList:
                self.instanceOfferingUuidList.append(inventory['uuid'])

        self.logger.info("创建计算规格...")
        response = self.instanceOfferingController.create_instance_offering(name=self.instanceOfferingName,
                                                                            cpuNum=self.cpuNum, memorySize=self.memorySize)
        self.assertTrue(response['true'])
        self.instanceOfferingUuid = response['inventories']['uuid']

    def test_delete_instanceOffering(self):
        """删除创建的计算规格"""
        self.logger.info("删除创建的计算规格...")
        response = self.instanceOfferingController.delete_instance_offering(uuid=self.instanceOfferingUuid)
        self.assertTrue(response['success'])
