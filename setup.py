from setuptools import find_packages, setup

setup(
    name="your_project_name",
    version="1.0.0",
    description="A short description of your project",
    author="Your Name",
    author_email="your_email@example.com",
    url="https://github.com/your_username/your_project",
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
