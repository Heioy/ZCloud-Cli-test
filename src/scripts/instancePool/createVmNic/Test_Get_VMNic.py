#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List
from src.scripts.base import BaseCases


class TestGetVMNic(BaseCases):

    @classmethod
    def setUpClass(cls) -> None:
        super(TestGetVMNic, cls).setUpClass()

        cls.vmNicUuidList: List[str] = []
        cls.vmNicUuid: str = ''

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def test_get_attached_network_service(self):
        self.logger.info("查询云主机网卡信息...")
        nicInfo = self.vmController.query_nic()
        self.logger.info(nicInfo)

        for inventory in nicInfo['inventories']:
            self.vmNicUuidList.append(inventory['uuid'])

        self.vmNicUuid = self.vmNicUuidList[0]

        self.logger.info("获取网卡加载的网络服务名称...")
        nicAttachedNetworkService = self.vmController.get_nic_attached_network_service(vmNicUuid=self.vmNicUuid)
        self.assertTrue(nicAttachedNetworkService['success'], msg="获取网卡加载的网络服务名称成功")

    def test_candidates_l3Networks(self):
        self.logger.info("获取云主机网卡可挂载的三层网络")
        l3NetworkInfo = self.vmController.get_candidate_l3_network_for_change_instance_nic_network(vmNicUuid=self.vmNicUuid)
        self.assertTrue(l3NetworkInfo['success'], msg="获取云主机网卡可挂载的三层网络成功")
