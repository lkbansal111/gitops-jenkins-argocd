from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="gitops-project",
    version="0.1",
    author="Lavkush",
    packages=find_packages(),
    install_requires = requirements,
)