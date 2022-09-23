#!/usr/bin/env python3
# -*- coding:utf-8 -*- 

import json
import time
import subprocess
import socket
import paramiko
from paramiko.client import SSHClient

from logging import Logger
from configparser import ConfigParser
from typing import Optional, List, Type, Dict
from types import TracebackType

from src.utils.errors import (
    ParameterError,
    RunCommandTimeoutError,
    SSHConnectingError,
    ChannelError,
    RemoteCommandError
)


class Client(object):

    def __init__(self,
                 host: str,
                 username: str,
                 password: str = None,
                 key: str = None,
                 private_host: str = None,
                 config: ConfigParser = None,
                 debug: bool = False,
                 use_public: bool = True,
                 logger: Logger = None
                 ) -> None:
        self.host = host
        self.private_host = private_host
        self.username = username
        self.password = password
        self.key = key
        self.debug = debug
        self.use_public = use_public
        self.logger = logger

        self.config = config
        self.cli: SSHClient = None

    def __enter__(self):
        return self

    def __exit__(self,
                 exc_type: Optional[Type[BaseException]],
                 exc_val: Optional[BaseException],
                 exc_tb: Optional[TracebackType]
                 ):
        if exc_val is not None:
            print(f"{exc_val}")
        return False

    def wait_until_accessible(self,
                              retry_times: int = 5,
                              retry_delay: int = 30
                              ) -> None:
        retry_count = 0

        while retry_count < retry_times:
            if self.is_up():
                pass
                return
            time.sleep(retry_delay)
            retry_count += 1
            pass

    def is_up(self, timeout: int = 30):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((self.host if self.use_public else self.private_host, 22))
        return result == 0

    def run_loacl_cmd(self,
                      command: List[str],
                      bufsize: int = -1,
                      shell: bool = False,
                      timeout: int = 30,
                      retry_count: int = 1
                      ) -> Dict[str, str]:
        stdout, stderr = None, None
        if not isinstance(command, list):
            raise ParameterError(exc_val=command, act_type=list)

        try:
            retry: int = 0
            while retry <= retry_count:
                self.logger.info(f"[Local CMD Execute]: {' '.join(command)}")
                response = subprocess.run(command,
                                          bufsize=bufsize,
                                          stdin=subprocess.PIPE,
                                          stdout=subprocess.PIPE,
                                          stderr=subprocess.PIPE,
                                          shell=shell)
                stdout = response.stdout.decode().strip('\n')
                stderr = response.stderr.decode().strip('\n')
                self.logger.info(f"[Local CMD Response - stdout] {stdout}")
                self.logger.info(f"[Local CMD Response - stderr] {stderr}")

                if stderr:
                    # logger
                    pass
                return {
                    'stdout': stdout,
                    'stderr': stderr,
                    'returncode': response.returncode
                }

        except TimeoutError as rcte:
            raise RunCommandTimeoutError(command=command, local=True, timeout=timeout, error=repr(rcte))

    def _get_cli(self) -> paramiko.SSHClient:
        timeout: float = 20
        try:
            # 当cli对象不存在时建立
            if self.cli is None or self.cli.get_transport() is None or not self.cli.get_transport().is_active():
                cli = paramiko.SSHClient()
                cli.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                hostname = self.host if self.use_public else self.private_host
                cli.connect(hostname=hostname, username=self.username, password=self.password, key_filename=self.key,
                            allow_agent=False, look_for_keys=False, timeout=timeout)
                self._cli = cli

            return self._cli
        except paramiko.ssh_exception.SSHException:
            raise SSHConnectingError(f"与远程服务器 {hostname} 建立SSH会话失败. ")

    def run_command(self, command: str, timeout: int = 30, retry_count: int = 1):
        if not command:
            raise ValueError(f"执行命令的参数传递错误. {command}")
        retry_times: int = 1

        while retry_times <= retry_count:
            try:
                client = self._get_cli()
                # print(client)
                object_at = client.__repr__().split()[-1].strip('>')
                self.logger.info(f"[Remote CMD Execute - (Object at {object_at})]: {command}")
                _, stdout, stderr = client.exec_command(command=command, timeout=timeout)
                stdout.flush()
                stderr.flush()

                # Blocks until done
                while not stdout.channel.exit_status_ready():
                    status = stdout.channel.recv_exit_status()

                out = stdout.read().decode()
                err = stderr.read().decode()

                self.logger.info(f"[Remote CMD Response - (Object at {object_at}) - retcod] {status}")
                self.logger.info(f"[Remote CMD Response - (Object at {object_at}) - stdout] {out}")
                self.logger.info(f"[Remote CMD Response - (Object at {object_at}) - stderr] {err}")

                if status != 0:
                    raise RemoteCommandError(command, out)

                try:
                    return {'stdout': json.loads(out), 'stderr': err, 'returncode': status}
                except json.decoder.JSONDecodeError:
                    print(f"解析<{command}>命令执行结果异常")
                    return {'stdout': out, 'stderr': err, 'returncode': status}

            except paramiko.ssh_exception.ChannelException:
                raise ChannelError(command, self.host)

# if __name__ == '__main__':
#     client = Client(host='10.10.100.22', username='root', password='Cljslrl0620!')
#     res = client.run_command('ls -lh')
#     print(res)
