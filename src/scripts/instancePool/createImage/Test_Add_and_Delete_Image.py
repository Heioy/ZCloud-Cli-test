#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from typing import List
from src.scripts.base import BaseCases


class TestAddAndDeleteImage(BaseCases):

    @classmethod
    def setUpClass(cls) -> None:
        super(TestAddAndDeleteImage, cls).setUpClass()

        cls.imageNameList: List[str] = []
        cls.imageUuidList: List[str] = []
        cls.backupStorageUuidList: List[str] = []
        cls.name: str = 'img-01'
        cls.url: str = "xxx"
        cls.form: str = "qcow2"

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def test_add_image(self):
        """添加镜像"""
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

        self.logger.info("添加镜像到镜像服务器...")
        addImage = self.imgController.add_image(name=self.name, form=self.form, url=self.url, backupStorageUuids=self.backupStorageUuidList.pop())
        self.assertTrue(addImage['success'], msg="添加镜像")

    def test_delete_image(self):
        """删除镜像"""
        self.logger.info("已存在的镜像名称为: \n%s" % ('\n'.join(self.imageNameList)))
        self.logger.info("删除镜像...")
        deleteImage = self.imgController.delete_image(uuid=self.imageUuidList.pop(), backupStorageUuids=self.backupStorageUuidList.pop())
        self.assertTrue(deleteImage['success'], msg="删除镜像")


