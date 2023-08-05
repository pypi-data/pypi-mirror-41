from setuptools import setup, find_packages

with open("VERSION", "r") as fv:
    VERSION = fv.read()

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="PyDojoML",
    version=VERSION,
    author="Victor Velev",
    author_email="velev.victor@yahoo.com",
    description="A General Purpose Machine Learning Library for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/VIVelev/PyDojoML",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "numpy",
        "scipy",
        "matplotlib",
        "progressbar",
        "terminaltables",
    ],
)
