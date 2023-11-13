import logging

import paramiko
from pydantic import ValidationError

from host import Host

logger = logging.getLogger(__name__)


class SSHClient(paramiko.SSHClient):
    def __init__(self) -> None:
        super().__init__()
        self.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def exec_commands(self, host: Host, commands: dict[str, str]) -> None:
        self.connect(
            hostname=host.ip,
            port=host.port,
            username=host.username,
            password=host.password
        )

        for param, cmd in commands.items():
            _, stdout, stderr = self.exec_command(cmd)
            if stdout.channel.recv_exit_status() == 0:
                try:
                    setattr(host, param, stdout.read().decode("utf8").strip())
                except ValidationError as err:
                    stdout.close()
                    stderr.close()
                    self.close()

                    logger.error(err)
                    raise RuntimeError(err)
            else:
                message = f'command: "{cmd}", description: {stderr.read().decode("utf8").strip()}'

                stdout.close()
                stderr.close()
                self.close()

                logger.error(message)
                raise RuntimeError(message)

            stdout.close()
            stderr.close()

        self.close()
