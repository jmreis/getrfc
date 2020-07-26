import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="get_rfc",
    version="0.0.1",
    author="Jair reis",
    author_email="jmsrpython@protonmail.com",
    description="A simple module for get RFC",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jmreis/pygetrfc",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)