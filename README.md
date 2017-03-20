MongoAdapter
===============

MongoAdapter is a Python module containing optimized data adapters for importing
data from Mongo databases into NumPy arrays and Pandas DataFrame. It was
previously a part of the IOPro project.

Build Requirements
------------------

Building MongoAdapter requires a number of dependencies. In addition to a C/C++ dev
environment, the following modules are needed, which can be installed via conda:

* NumPy 1.11
* Pandas
* mongo-driver 0.7.1 (C lib)

Building Conda Package
----------------------

Note: If building under Windows, make sure the following commands are issued
within the Visual Studio command prompt for version of Visual Studio that
matches the version of Python you're building for.  Python 2.6 and 2.7 needs
Visual Studio 2008, Python 3.3 and 3.4 needs Visual Studio 2010, and Python
3.5 needs Visual Studio 2015.

1. Install [Docker](https://docs.docker.com/engine/installation/). Add the current user to the `docker` group and restart the daemon, so that `docker` commands can be executed without root privileges

1. Build MongoAdapter using the following command:
```
conda build buildscripts/condarecipe --python 3.5
```

1. MongoAdapter can now be installed from the built conda package:
```
conda install mongoadapter --use-local
```

Building By Hand
----------------

Note: If building under Windows, make sure the following commands are issued
within the Visual Studio command prompt for version of Visual Studio that
matches the version of Python you're building for.  Python 2.6 and 2.7 needs
Visual Studio 2008, Python 3.3 and 3.4 needs Visual Studio 2010, and Python
3.5 needs Visual Studio 2015.

For building MongoAdapter for local development/testing:

1. Install most of the above dependencies into environment called 'mongoadapter':
```
conda env create -f environment.yml
```

Be sure to activate new mongoadapter environment before proceeding.

1. Build MongoAdapter using Cython/distutils:
```
python setup.py build_ext --inplace
```

Testing
-------

To get a test database running, execute the following command (after [installing Docker](https://docs.docker.com/engine/installation/)):
```
docker run --rm --name mongo-db --publish 27017:27017 mongo:3.0
```
The Docker image is a ~300MB download. Once downloaded it should take about 5 seconds for the database to start.

The MongoAdapter tests will generate their own test data by creating a
collection called 'MongoAdapter_tests' in the Mongo database specified by the
above parameters. In another terminal, tests can be run by calling the mongoadapter
module's test function:
```python
python -Wignore -c 'import mongoadapter; mongoadapter.test()'
```
