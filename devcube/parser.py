from pydantic import BaseModel


class GlobalConfig(BaseModel):
    working_dir: str = "."


class EnvConfig(BaseModel):
    name: str
    image: str
    container_working_dir: str = "/devcube"
    entry_point: str = "/bin/bash"


available_config = {
    "global_config": GlobalConfig,
    "env": EnvConfig,
}


class ParsedConfig(BaseModel):
    global_config: GlobalConfig = GlobalConfig()
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
