import subprocess
import pathlib

from devcube.container import Container
from devcube.utils import logout


class Executor(object):
    def __init__(self, container: Container):
        self.docker_bin = "docker"
        self.user_workspace = pathlib.Path(".").absolute().as_posix()
        self.container = container
        # check docker runtime
        self.check_env()

    def check_env(self):
        subprocess.check_call(
            [self.docker_bin, "version",]
        )
        logout("docker runtime ready.")

    def execute(self):
        # todo: use official python-sdk instead?
        command = [
            self.docker_bin,
            "run",
            "-i",
            # workspace
            "-v",
            f"{self.user_workspace}:{self.container.work_dir}",
            "-w",
            self.container.work_dir,
            # image
            self.container.image,
            # interface
            self.container.entry_point,
        ]
        logout(f"ready to start env: {command}")
        process = subprocess.Popen(command, stdin=subprocess.PIPE)
        stop_word = "devcube::exit"
        logout(f"Container up. Type `{stop_word}` to exit. Enjoy it :)")

        # todo
        while True:
            user_input = input()
            if stop_word in user_input:
                break
            user_input += "\n"
            process.stdin.write(user_input.encode())
            process.stdin.flush()
        logout(f"normally stop.")
        process.kill()
