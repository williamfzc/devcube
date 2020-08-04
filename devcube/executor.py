import subprocess
import pathlib

from devcube.utils import logout
from devcube.parser import Parser


class Executor(object):
    def __init__(self, cfg_data: dict):
        self.docker_bin = "docker"
        self.user_workspace = pathlib.Path(".").absolute().as_posix()
        # check docker runtime
        self.check_env()
        # parse
        self.cfg = Parser.parse(cfg_data)

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
            # remove after usage
            "--rm",
            # workspace
            "-v",
            f"{self.user_workspace}:{self.cfg[Parser.KEY_GLOBAL].work_dir}",
            "-w",
            self.cfg[Parser.KEY_GLOBAL].work_dir,
            # image
            self.cfg[Parser.KEY_GLOBAL].image,
            # interface
            self.cfg[Parser.KEY_GLOBAL].entry_point,
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
