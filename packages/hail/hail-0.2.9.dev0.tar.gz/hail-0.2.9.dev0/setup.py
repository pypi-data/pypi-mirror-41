#!/usr/bin/env python

from setuptools import setup, find_packages

with open('hail/hail_pip_version') as f:
    hail_pip_version = f.read().strip()

with open("README.md", "r") as fh:
    long_description = fh.read()

install_requires = []
with open('requirements.txt') as f:
    install_requires = f.read().splitlines()

print(repr(install_requires))

setup(
    name="hail",
    version=hail_pip_version,
    author="Hail Team",
    author_email="hail-team@broadinstitute.org",
    description="Scalable library for exploring and analyzing genomic data.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://hail.is",
    packages=find_packages(),
    package_data={
        '': ['hail-all-spark.jar', 'hail_pip_version', 'hail_version']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.6",
    install_requires=install_requires
)
