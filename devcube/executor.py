import pathlib
import docker
import subprocess

from devcube.utils import logout
from devcube.parser import ParsedConfig


class Executor(object):
    def __init__(self, cfg: ParsedConfig):
        self.cfg = cfg
        self.docker_cli = docker.from_env()
        # check docker runtime
        self.check_env()

    def check_env(self):
        status = self.docker_cli.ping()
        logout(f"docker runtime status: {status}")

    def execute(self):
        # prepare
        container_working_dir = self.cfg.env.container_working_dir
        working_dir = (
            pathlib.Path(self.cfg.global_config.working_dir).absolute().as_posix()
        )

        try:
            # linux/mac
            import dockerpty

            container = self.docker_cli.containers.create(
                name=self.cfg.env.name,
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
        except ImportError:
            # windows
            # i have no better idea now
            logout(
                "Your system does not support pty. Trying to use command line instead ..."
            )
            command = [
                "docker",
                "run",
                "-i",
                # remove after usage
                "--rm",
                # workspace
                "-v",
                f"{working_dir}:{container_working_dir}",
                "-w",
                container_working_dir,
                "--name",
                self.cfg.env.name,
                # image
                self.cfg.env.image,
                # interface
                self.cfg.env.entry_point,
            ]
            logout(f"start env: {command}")
            process = subprocess.Popen(command, stdin=subprocess.PIPE)

            try:
                while True:
                    user_input = input()
                    user_input += "\n"
                    process.stdin.write(user_input.encode())
                    process.stdin.flush()
            except KeyboardInterrupt:
                process.kill()
        finally:
            # end, stop it
            self.docker_cli.api.stop(self.cfg.env.name)
            logout("devcube end.")
