from setuptools import setup, find_packages

setup(
    name="gifify",
    version="0.0.3",
    packages=find_packages(),
    install_requires=[
        "imageio",
        "matplotlib",
        "ipython",
    ],
    long_description="Wrap an iterator to make a gif out of matplotlib plots",
)
