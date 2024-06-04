from setuptools import setup, find_packages

setup(
    name="gifify",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "imageio",
        "matplotlib",
    ],
    long_description="Wrap an iterator to make a gif out of matplotlib plots",
)
