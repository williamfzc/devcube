import fire
import json
import pathlib

from devcube.executor import Executor
from devcube.parser import Parser


DEFAULT_CFG_NAME = ".devcube.json"


class Cli(object):
    def start(self, file_path: str = None):
        if not file_path:
            file_path = DEFAULT_CFG_NAME
        cfg_file = pathlib.Path(file_path)
        assert cfg_file.is_file(), f"file {file_path} not existed"
        with open(cfg_file, encoding="utf-8") as f:
            cfg = json.load(f)
        parsed = Parser().parse(cfg)
        Executor(parsed).execute()


def main():
    fire.Fire(Cli)
