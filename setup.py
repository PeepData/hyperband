from setuptools import find_packages, setup

__version__ = "0.1"

setup(
    name="hyperband",
    version=__version__,
    packages=find_packages(exclude=["tests"]),
    entry_points={"console_scripts": ["hyperband = hyperband.__main__:cli"]},
)
