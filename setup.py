from setuptools import setup, find_packages

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path):
    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        requirements = [req for req in requirements if req != HYPHEN_E_DOT]
    return requirements


setup(
    name="mlproject",
    version="0.0.1",
    author="Theodore Abossolo",
    author_email="tamglabs@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)