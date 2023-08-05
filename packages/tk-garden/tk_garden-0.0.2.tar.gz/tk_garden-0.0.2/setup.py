import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tk_garden",
    version="0.0.2",
    author="TechKids Coding School",
    author_email="techkidsvn@gmail.com",
    description="TK Garden Bot Controllers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/edtechkidsvn/tk-garden",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    install_requires=[
      ]
)