from devcube.executor import Executor


data = {
    "global": {"name": "hello", "image": "python:3-slim",},
    "before": {"command_list": ["ls",]},
}

Executor(data).execute()
