#Creating and adding your own custom Python packages to PyPi (Python 3.7.2)
######Author: [Joe Tilsed](http://linkedin.com/in/joetilsed) | Created: 04.02.2019 | Last Updated: 04.02.2019

###Requirements:
- setuptools
- wheel
- twine

###Helpful Articles:
- [Packaging Python Projects — Python Packaging User Guide](https://packaging.python.org/tutorials/packaging-projects/)

###File Structure:
- [README.md](./README.md)

###Generating the distribution:
*python setup.py sdist bdist_wheel*

###Uploading the distributions to PyPi:
- TEST
    - *python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/**
- PROD
    - *python -m twine upload --repository-url https://pypi.org/legacy/ dist/**
