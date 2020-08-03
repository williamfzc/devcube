import typing


class Parser(object):
    class _Global(object):
        def __init__(
            self, name: str, image: str, work_dir: str = None, entry_point: str = None
        ):
            self.name = name
            self.image = image
            self.work_dir = work_dir or "/devcube"
            self.entry_point = entry_point or "/bin/bash"

    class _Before(object):
        def __init__(self, command_list: typing.List[str] = None):
            self.command_list = command_list or []

    KEY_GLOBAL = r"global"
    KEY_BEFORE = r"before"
    KLS_DICT = {
        KEY_GLOBAL: _Global,
        KEY_BEFORE: _Before,
    }

    @classmethod
    def parse(cls, data) -> dict:
        # all the values will be filled
        result = dict()
        # check key
        for k, v in data.items():
            if k not in Parser.KLS_DICT:
                raise KeyError(f"invalid key: {k}")
            inst = Parser.KLS_DICT[k](**v)
            result[k] = inst
        return result
