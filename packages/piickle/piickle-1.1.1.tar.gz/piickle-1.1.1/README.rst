=======
piickle
=======

The one true Pickler, it takes the pickle and encodes the bits and a space
and a pickle emoji.

Installation
============
From PyPi::

    $ pip install piickle

Basic Usage
===========
Use the library directly:

.. code-block:: python

    import piickle

    piickle.dump(object, file) # Same as the python pickle.dump()
    piickle.dumps(object) # Same as the python pickle.dumps()
    piickle.load(file) # Same as the python pickle.load()
    piickle.loads(string) # Same as the python pickle.loads()

or use the monkey patch feature:

.. code-block:: python

    import pickle
    import piickle

    pickle.dump(object, file)
    pickle.dumps(object)
    pickle.load(file)
    pickle.loads(string)

Features
========
* A truly horrible pun
