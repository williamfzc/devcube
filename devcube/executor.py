import pathlib
import docker
import dockerpty

from devcube.utils import logout
from devcube.parser import ParsedConfig


class Executor(object):
    def __init__(self, cfg: ParsedConfig):
        self.cfg = cfg
        self.docker_cli = docker.from_env()
        # check docker runtime
        self.check_env()

    def check_env(self):
        info = self.docker_cli.info()
        logout(f"docker runtime ready: {info}")

    def execute(self):
        # prepare
        container_working_dir = (
            pathlib.Path(self.cfg.env.container_working_dir).absolute().as_posix()
        )
        working_dir = (
            pathlib.Path(self.cfg.global_config.working_dir).absolute().as_posix()
        )

        container = self.docker_cli.containers.create(
            image=self.cfg.env.image,
            command=self.cfg.env.entry_point,
            working_dir=container_working_dir,
            volumes={working_dir: {"bind": container_working_dir, "mode": "rw"}},
            auto_remove=True,
            # required
            tty=True,
            stdin_open=True,
        )

        dockerpty.start(self.docker_cli.api, container.id)
        # end, stop it
        self.docker_cli.api.stop(container.name)
        logout("devcube end.")
