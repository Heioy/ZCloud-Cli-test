#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from typing import List
from src.scripts.base import BaseCases


class TestCreateDataVolume(BaseCases):

    @classmethod
    def setUpClass(cls) -> None:
        super(TestCreateDataVolume, cls).setUpClass()

        cls.dataVolumeList: List[str] = []
        cls.diskOfferingList: List[str] = []
        cls.dataVolumeName: str = "dv01"

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def test_create_dataVolume(self):
        """创建数据云盘"""
        self.logger.info("查询已存在的数据云盘...")
        existedDataVolume = self.volumeController.query_volume()
        for inventory in existedDataVolume['inventories']:
            if inventory['uuid'] not in self.dataVolumeList:
                self.dataVolumeList.append(inventory['uuid'])

        self.logger.info("查询云盘规格...")
        diskOffering = self.OfferingController.query_diskoffering()
        for inventory in diskOffering['inventories']:
            if inventory['uuid'] not in self.diskOfferingList:
                self.diskOfferingList.append(inventory['uuid'])

        self.logger.info("创建数据云盘...")
        createDataVolume = self.volumeController.create_datavolume(name=self.dataVolumeName, diskOffering=self.dataVolumeList.pop())
        self.assertTrue(createDataVolume['success'])

    def test_delete_dataVolume(self):
        """删除云盘"""
        existedDataVolume = self.volumeController.query_volume()
        for inventory in existedDataVolume['inventories']:
            if inventory['uuid'] not in self.dataVolumeList:
                self.dataVolumeList.append(inventory['uuid'])
        self.logger.info(f"可删除的云盘列表为: {' '.join(self.dataVolumeList)}")

        self.logger.info("删除云盘...")
        deleteDataVolume = self.volumeController.delete_datavolume(uuid=self.dataVolumeList.pop())
        self.assertTrue(deleteDataVolume['success'])
