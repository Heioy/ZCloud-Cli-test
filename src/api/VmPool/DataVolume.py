#!/usr/bin/env python3
# -*- coding:utf-8 -*- 

from logging import Logger
from typing import Union, Any, Dict, List
from src.api.client import ZStackClient
from src.config.command import *
from src.utils.errors import ParameterIsNoneError, RemoteCommandError


"""云盘资源类"""


class DataVolume(ZStackClient):

    def __init__(self, logger: Logger = None):
        super(DataVolume, self).__init__(logger=logger)
        self.create_volume_timeout = 10 * 60

    def create_datavolume(self, name: str, description: str = None, diskOfferingUuid: str = None,
                          primaryStorageUuid: str = None, resourceUuid: str = None, tagUuids: str = None
                          ) -> Union[Dict, str]:
        """
        创建云盘
        :param name: 云盘名称
        :param description: 云盘描述
        :param diskOfferingUuid: 云盘规格uuid
        :param primaryStorageUuid: 主存储uuid
        :param resourceUuid: 资源uuid。若指定，镜像会使用该字段值作为uuid
        :param tagUuids: 标签UUID列表
        """
        if not name:
            raise ParameterIsNoneError(name=name)

        command = f"{self.zstack_cli} {ZStack_Create_DataVolume.format(volname=name)}"

        if description:
            command = f"{command} description={description}"
        if diskOfferingUuid:
            command = f"{command} diskOfferingUuid={diskOfferingUuid}"
        if primaryStorageUuid:
            command = f"{command} primaryStorageUuid={primaryStorageUuid}"
        if resourceUuid:
            command = f"{command} resourceUuid={resourceUuid}"
        if tagUuids:
            command = f"{command} tagUuids={tagUuids}"

        response = self.client.run_command(command)
        return response['stdout']


