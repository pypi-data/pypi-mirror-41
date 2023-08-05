import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jassign",
    version="0.0.1",
    author="John DeNero",
    author_email="denero@berkeley.edu",
    description="Jupyter notebook assignment formatting and distribution",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/okpy/jupyter-assignment",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)