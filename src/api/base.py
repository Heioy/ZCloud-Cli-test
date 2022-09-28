#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
from logging import Logger
from typing import Any
from src.utils.ssh import Client
from src.utils.readFile import read_toml
from src.utils import errors


class Base(object):

    def __init__(self, host: Any = None, username: str = None, password: str = None, key: str = None,
                 private_host: str = None, debug: bool = False, use_public: bool = True, port: Any = None,
                 admin_password: str = None, zstack_config_dump_file: str = None,
                 deploy_config_template_file: str = None, deploy_config_file: str = None,
                 logger: Logger = None
                 ):
        """
        ZStack Client Tools
        :param zstack_config_dump_file: [Optional] dump a cloud to a XML file
        :param deploy_config_template_file: [Optional] variable template file for XML file. specified in option '-d'
        :param deploy_config_file: [Optional] deploy a cloud from a XML file.
        """
        # if not host or not username or not password:
        #     raise errors.ParameterIsNoneError(host=host, username=username, password=password)

        self.config = self.set_config()
        self.host = host if host else self.config['develop']['server']
        self.username = username if username else self.config['develop']['username']
        self.password = password if password else self.config['develop']['password']
        self.key = key
        self.private_host = private_host
        self.debug = debug
        self.use_public = use_public
        self.port = port if port else self.config['develop']['port']
        self.admin_password = admin_password
        self.zstack_config_dump_file = zstack_config_dump_file
        self.deploy_config_template_file = deploy_config_template_file
        self.deploy_config_file = deploy_config_file

        # logger record
        self.logger = logger

        self.client = Client(host=self.host, username=self.username, password=self.password, key=self.key,
                             private_host=self.private_host, debug=self.debug, use_public=self.use_public,
                             logger=logger)

    def set_config(self):
        """Read Toml config"""
        current_dir = os.path.dirname(os.getcwd())
        config_file = os.path.join(current_dir, 'config/config.toml')
        return read_toml(config_file, mode='r')
