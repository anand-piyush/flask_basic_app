import setuptools
from src import __version__

with open("README.txt", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="simple-flask-app", # Replace with your own username
    version=__version__,
    author="Piyush Anand",
    author_email="piyush.anand@rediffmail.com",
    description="A simple python flask package to test things",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/anand-piyush/flask_basic_app",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)