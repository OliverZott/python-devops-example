from setuptools import find_packages
from setuptools import setup

setup(
    name="Velosaurus Dummy Project",
    version="1.0.0",
    description="Just a dummy project for some pipeline and package deployment testing",
    long_description="Just a dummy project for some pipeline and package deployment testing",
    author="Oliver Zott",
    author_email="zott_oliver@web.de",
    url="https://github.com/OliverZott/python-devops-example",
    packages=find_packages(),
    install_requires=[
        # Add any dependencies your project requires
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
