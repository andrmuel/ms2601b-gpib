from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="ms2601b",
    version="0.0.1",
    author="Andreas Müller",
    author_email="code@0x7.ch",
    description="Control MS2601B spectrum analyzer via GPIB.",
    packages=find_packages(),
    long_description=long_description,
    install_requires=["ipython>=7.21.0"],
)
