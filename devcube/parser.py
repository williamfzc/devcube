from pydantic import BaseModel


class GlobalConfig(BaseModel):
    pass


class EnvConfig(BaseModel):
    name: str
    image: str
    work_dir: str = "/devcube"
    entry_point: str = "/bin/bash"


available_config = {
    "global_config": GlobalConfig,
    "env": EnvConfig,
}


class ParsedConfig(BaseModel):
    global_config: GlobalConfig = None
    env: EnvConfig


class Parser(object):
    def parse(self, data: dict) -> ParsedConfig:
        # all the values will be filled
        result = dict()
        # check key
        for k, v in data.items():
            if k not in available_config:
                raise KeyError(f"invalid key: {k}")
            result[k] = available_config[k](**v)
        return ParsedConfig(**result)
