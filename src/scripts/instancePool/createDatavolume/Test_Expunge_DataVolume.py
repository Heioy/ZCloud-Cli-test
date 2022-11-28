#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from typing import List
from src.scripts.base import BaseCases


class TestExpungeDataVolume(BaseCases):

    @classmethod
    def setUpClass(cls) -> None:
        super(TestExpungeDataVolume, cls).setUpClass()

        cls.dataVolumeList: List[str] = []

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def test_expunge_dataVolume(self):
        """彻底删除云盘"""
        self.logger.info("查询已存在的数据云盘...")
        existedDataVolume = self.volumeController.query_volume()
        for inventory in existedDataVolume['inventories']:
            if inventory['uuid'] not in self.dataVolumeList:
                self.dataVolumeList.append(inventory['uuid'])

        self.logger.info("删除数据云盘...")
        expungeDataVolume = self.volumeController.expunge_datavolume(uuid=self.dataVolumeList.pop())
        self.assertTrue(expungeDataVolume['success'])
