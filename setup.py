import os

from setuptools import setup


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "kaggle-tabbular-nov21",
    version = "0.0.0",
    author = "Shivam Pandey",
    author_email = "pandeyshivam2017robotics@gmail.com",
    description = ("Kaggle tabular challenge series: november 2021 edition."),
    license = "AGPLv3",
    keywords = "DeepLearning Pytorch Datasets Kaggle",
    url = "https://github.com/ShivamPR21/kaggle-tabular-challenge-nov2021.git",
    packages=[],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: AGPLv3 License",
    ],
)
