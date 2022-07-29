from setuptools import setup
from setuptools import find_packages

setup(
    name="mypkg",
    version="1.0.0",
    author="ouss",
    author_email="ouss.miss@gmail.com",
    description="sample package showing how to pakage data files",
    packages=find_packages(exclude=('test/*', 'testing/*')),
    # include_package_data=True, set it to true if you want to use MANIFEST.in instead of package_data
    # install_requires=[]
    package_data={"mypkg": ["*.json"],
                  "mypkg.pkg1": ["*.json"]},
    entry_points={
        "console_scripts": [
            "hello-world-cli = mypkg.main:main",
        ]
    }


)
