
==============
onos_grpc_demo
==============

This is the onos_grpc_demo application.


Minimum Requirements
====================

- Python 2.7


Optional Requirements
=====================

.. _pytest: http://pytest.org
.. _Sphinx: http://sphinx-doc.org

- `pytest`_ (for running the test suite)
- `Sphinx`_ (for generating documentation)


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
