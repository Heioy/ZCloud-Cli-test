#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from typing import List
from src.scripts.base import BaseCases


class TestStartVMInstance(BaseCases):

    @classmethod
    def setUpClass(cls) -> None:
        super(TestStartVMInstance, cls).setUpClass()
        cls.vmStatus: str = "Stopped"
        cls.uuidList: List[str] = []
        cls.uuid: str = ""

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def test_start_vm_instance(self):
        self.logger.info("获取关机状态的云主机实例...")
        queryResponse = self.vmController.query_vm_instance(state=self.vmStatus)
        if queryResponse:
            for inventory in queryResponse['inventories']:
                self.uuidList.append(inventory['uuid'])

        else:
            self.logger.warning("未获取到关机状态的云主机实例")

        if self.uuidList:
            self.uuid = self.uuidList[0]

        startResponse = self.vmController.start_instance(uuid=self.uuid)
        self.assertTrue(startResponse['success'])

    def test_stop_vm_instance(self):
        self.logger.info("关闭开启的云主机实例...")
        stopResponse = self.vmController.stop_instance(uuid=self.uuid)
        self.assertTrue(stopResponse['success'])
