import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="iotdb-session",
    version="0.10.1",
    author="Julian Feinauer",
    author_email="jfeinauer@apache.org",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://iotdb.apache.org",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'apache-iotdb==0.10.1',
        'six==1.15.0',
        'thrift==0.13.0'''
    ],
    python_requires='>=3.6',
)
