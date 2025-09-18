from setuptools import setup, find_packages

setup(
    name="mwinfo",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["pyyaml"],
    entry_points={
        "console_scripts": [
            "mwinfo = mwinfo.cli:main",
        ],
    },
)
    