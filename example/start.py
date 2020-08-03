from devcube.executor import Executor
from devcube.container import Container


container = Container("haha", "python:3-slim", "/bin/bash", "/usr/src/app")
executor = Executor(container)
executor.execute()
