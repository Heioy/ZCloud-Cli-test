#!/usr/bin/env python3
# -*- coding:utf-8 -*- 

import unittest
from src.scripts.base import BaseCases


class TestCreateVMInstance(BaseCases):

    @classmethod
    def setUpClass(cls) -> None:
        super(TestCreateVMInstance, cls).setUpClass()

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def test_query_vm_instance(self):
        self.logger.info("查询虚拟机")
        result = self.vmController.query_vm_instance()
        # print(result)
