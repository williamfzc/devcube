from setuptools import setup, find_packages
from devcube import (
    __AUTHOR__,
    __AUTHOR_EMAIL__,
    __VERSION__,
    __PROJECT_NAME__,
)

with open("requirements.txt", encoding="utf-8") as f:
    requirements = [
        each.strip() for each in f.readlines() if not each.startswith("git+")
    ]

setup(
    name=__PROJECT_NAME__,
    version=__VERSION__,
    author=__AUTHOR__,
    author_email=__AUTHOR_EMAIL__,
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    python_requires=">=3.6",
    install_requires=requirements,
    entry_points={"console_scripts": ["devcube = devcube.cli:main"]},
)
