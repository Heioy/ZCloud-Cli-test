#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from typing import List
from src.scripts.base import BaseCases


class TestExpungeImage(BaseCases):

    @classmethod
    def setUpClass(cls) -> None:
        super(TestExpungeImage, cls).setUpClass()

        cls.imageNameList: List[str] = []
        cls.imageUuidList: List[str] = []
        cls.backupStorageUuidList: List[str] = []

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def test_expunge_image(self):
        """彻底删除镜像"""
        self.logger.info("查询已存在的镜像名称...")
        images = self.imgController.query_image()
        for inventory in images['inventories']:
            if inventory['name'] not in self.imageNameList:
                self.imageNameList.append(inventory['name'])
            if inventory['uuid'] not in self.imageUuidList:
                self.imageUuidList.append(inventory['uuid'])
            if inventory['backupStorageRefs']:
                for backupStorageRef in inventory['backupStorageRefs']:
                    self.backupStorageUuidList.append(backupStorageRef['backupStorageUuid'])

        self.logger.info("删除镜像...")
        expungeImage = self.imgController.expunge_image(imageUuid=self.imageUuidList.pop(), backupStorageUuids=self.backupStorageUuidList.pop())
        self.assertTrue(expungeImage['success'], msg="彻底删除镜像")