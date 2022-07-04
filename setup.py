from setuptools import setup, find_packages

setup(
    name="cute",
    version="0.0.1",
    author="Nathan Hubens",
    author_email="nathan.hubens@umons.ac.be",
    description="A package to convert your Jupyter Notebook",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)