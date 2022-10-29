#!/usr/bin/env python3
# -*- coding:utf-8 -*- 

from typing import Union, Dict
from logging import Logger
from src.api.client import ZStackClient
from src.config import commands
from src.utils.errors import ParameterIsNoneError


class ScsiLun(ZStackClient):

    def __init__(self, logger: Logger = None):
        super(ScsiLun, self).__init__(logger=logger)

    def query_scsiLun(self, name: str = None) -> Union[Dict, str]:
        """
        查询Iscsi块设备和FC块设备
        :param name:
        """
        command = f"{self.zstack_cli} {commands.ZStack_Query_ScsiLun}"
        if name:
            command = f"{command} name={name}"
        response = self.client.run_command(command)
        return response['stdout']

    def detach_scciLun_from_host(self, uuid: str, hostUuid: str = None) -> Union[Dict, str]:
        """
        将LUN设备从物理机卸载
        :param uuid: SCSI LUN UUID
        :param hostUuid: 物理机UUID
        """
        if not uuid:
            raise ParameterIsNoneError(uuid=uuid)
        command = f"{self.zstack_cli} {commands.ZStack_Detach_ScsiLun_from_Host.format(uuid=uuid)}"
        if hostUuid:
            command = f"{command} hostUuid={hostUuid}"
        response = self.client.run_command(command)
        return response['stdout']


