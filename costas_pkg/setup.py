import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Costas",
    version="0.0.1",
    author="Example Author",
    author_email="author@example.com",
    description="Long period variable star study",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/csrg-utfsm/Costas",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)