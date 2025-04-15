from setuptools import setup, find_packages

setup(
    name="isend-python-sdk",
    version="0.1.6",
    packages=find_packages(),
    install_requires=[
        "requests"
    ],
    author="Manohar Reddy",
#   python_requires=">=3.6",
    author_email="devmanoharrr@gmail.com",
    description="Python SDK for iSend API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/devmanoharrr/isend-python-sdk",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
)