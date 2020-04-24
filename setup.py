import setuptools
import unittest
from src.version import __version__

# REF : https://ep2015.europython.eu/conference/talks/less-known-packaging-features-and-tricks

with open("README.txt", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as fh:
    requires = fh.readlines()

def my_test_suite():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests', pattern='test_*.py')
    return test_suite


setuptools.setup(
    name="simple-flask-app", # Replace with your own username
    version=__version__,
    author="Piyush Anand",
    author_email="piyush.anand@rediffmail.com",
    description="A simple python flask package to test things",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/anand-piyush/flask_basic_app",
    packages=setuptools.find_packages(), # used to auto-find the subpackages using __init__.py files
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires = requires,
    python_requires='>=3.8',
    test_suite = 'setup.my_test_suite',     # tests
    include_package_data = True   # include static files inside the packages like swagger yml files

)