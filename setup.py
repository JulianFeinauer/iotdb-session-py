import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="iotdb-session-0.10.1",
    version="0.1.2",
    author="Julian Feinauer",
    author_email="j.feinauer@pragmaticminds.de",
    description="A small iotdb python client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JulianFeinauer/iotdb-session-py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'apache-iotdb==0.10.1',
        'six==1.15.0',
        'thrift==0.13.0'''
    ],
    python_requires='>=3.6',
)
