#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List
from src.scripts.base import BaseCases


class TestCreateVMNic(BaseCases):

    @classmethod
    def setUpClass(cls) -> None:
        super(TestCreateVMNic, cls).setUpClass()

        cls.nicName: str = 'testNic'
        cls.l3NetworkUuidList: List[str] = []
        cls.l3NetworkUuid: str = ''

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def test_create_vmNic(self):
        self.logger.info("查询云主机虚拟网卡...")
        nicInfo = self.vmController.query_nic()
        self.logger.info(nicInfo)

        self.logger.info("查询网络资源-三层网卡资源实例...")
        l3NetworkInfo = self.l3Controller.query_l3Network()
        self.logger.info(l3NetworkInfo)

        for l3Inventory in l3NetworkInfo['inventories']:
            if l3Inventory['uuid']:
                self.l3NetworkUuidList.append(l3Inventory['uuid'])

        self.l3NetworkUuid = self.l3NetworkUuidList[0]
        self.logger.info("创建云主机网卡...")
        createResponse = self.vmController.create_nic(l3NetworkUuid=self.l3NetworkUuid)
        self.assertTrue(createResponse['success'], msg="创建云主机网卡成功")

    def test_delete_vmNic(self):
        self.logger.info("删除云主机虚拟机网卡...")
        deleteResponse = self.vmController.delete_nic(l3NetworkUuid=self.l3NetworkUuid)
        self.assertTrue(deleteResponse['success'], msg="删除云主机网卡成功")


