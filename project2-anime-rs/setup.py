from setuptools import setup, find_packages
with open("requirements.txt") as f:
    requirements = f.read().splitlines()


setup(
    name = "MLOps-Project-01",
    version="0.1",
    author = "Dilip Rathod",
    packages = find_packages(),
    install_requires = requirements,
)