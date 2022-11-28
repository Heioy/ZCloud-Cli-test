#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import unittest
from src.api.VmPool.VmInstance import Instances
from src.api.VmPool.Image import Images
from src.api.VmPool.DataVolume import DataVolume
from src.api.VmPool.DiskOffering import DiskOffering
from src.api.VmPool.InstanceOffering import InstanceOffering
from src.api.NetworkResource.Network3 import L3Network
from src.scripts import logDirName, date
from src.utils.logger import get_logger


class BaseCases(unittest.TestCase):
    _instance = None

    def __init__(self, methodName):
        super(BaseCases, self).__init__(methodName)
        # 实例化各种类接口
        if not methodName.endswith('.log'):
            methodName = f"{methodName}.log"

        logs_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), logDirName)
        filename_dir = os.path.join(logs_dir, date, f"{self.__module__.split('.', 1)[0]}")

        if not os.path.exists(filename_dir):
            try:
                os.makedirs(filename_dir, exist_ok=True)
            except Exception:
                pass

        filename = os.path.join(filename_dir, methodName)

        self.logger = get_logger(filename=filename)
        # __base = Base(logger=self.logger)
        self.vmController = Instances(logger=self.logger)
        self.imgController = Images(logger=self.logger)
        self.instanceOfferingController = InstanceOffering(logger=self.logger)
        self.l3Controller = L3Network(logger=self.logger)
        self.volumeController = DataVolume(logger=self.logger)
        self.OfferingController = DiskOffering(logger=self.logger)

    @classmethod
    def setUpClass(cls) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass
