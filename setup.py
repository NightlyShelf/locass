import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="src",
    version="Beta 0.1",
    author="NightlyShelf",
    description="Simple localization manager",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.4',
    py_modules=["src"],
    package_dir={'':'locass/src'},
    install_requires=[]
)