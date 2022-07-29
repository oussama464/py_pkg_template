from setuptools import setup
from setuptools import find_packages

try:
    with open("README.md") as f:
        long_description = f.read()
except IOError:
    long_description = ""

try:
    with open("requirements.txt") as f:
        requirements = [x.strip() for x in f.read().splitlines() if x.strip()]
except IOError:
    requirements = []

setup(
    name="mypkg",
    version="1.0.0",
    author="ouss",
    author_email="ouss.miss@gmail.com",
    description="sample package showing how to pakage data files",
    long_description=long_description,
    packages=find_packages(exclude=('test/*', 'testing/*')),
    # include_package_data=True, set it to true if you want to use MANIFEST.in instead of package_data
    install_requires=requirements,
    package_data={"mypkg": ["*.json"],
                  "mypkg.pkg1": ["*.json"]},
    entry_points={
        "console_scripts": [
            "hello-world-cli = mypkg.main:main",
        ]
    }


)
