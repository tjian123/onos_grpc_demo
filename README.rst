
==============
onos_grpc_demo
==============

This is the onos_grpc_demo application.


Minimum Requirements
====================

.. _pyyaml: http://www.pyyaml.org
.. _grpcio: http://grpc.io

- `PyYAML`_ (for reading the yaml config)
- `grpcio`_ (for rpc)

- Python 2.7


Optional Requirements
=====================

.. _pytest: http://pytest.org
.. _Sphinx: http://sphinx-doc.org
.. _Grpcio-tools: https://pypi.python.org/pypi/grpcio-tools

- `pytest`_ (for running the test suite)
- `Sphinx`_ (for generating documentation)
- `grpc_tools`_ (for generating python sources from protobuf file)

Recommend Setup
===============

1. create virtual env:

.. code-block:: console

    $ python setup.py virtualenv

2. prepare environment:

.. code-block:: console

    $ source venv/bin/activate
    $ pip install -r requirements.txt

3. install:

.. code-block:: console

    $ python setup.py install

4. running:

.. code-block:: console

    $ python -m onos_grpc_demo

Note:

1. If you need to generate source code, you can reference to the './src/onos_grpc_demo/proto/compile.txt'. For it just for
test use, I skips makefile.
2. Auto-generated codes don't hava '__init__.py', So i was confused of how to keep mutil level directories.

Basic Setup
===========

Install for the current user:

.. code-block:: console

    $ python setup.py install --user


Run the application:

.. code-block:: console

    $ python -m onos_grpc_demo --help


Run the test suite:

.. code-block:: console
   
    $ pytest test/


Build documentation:

.. code-block:: console

    $ cd doc && make html
    
    
Deploy the application in a self-contained `Virtualenv`_ environment:

.. _Virtualenv: https://virtualenv.readthedocs.org

.. code-block:: console

    $ python deploy.py /path/to/apps
    $ cd /path/to/apps/onos_grpc_demo && bin/cli --help
