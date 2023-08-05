===============================
Pokepy
===============================

.. image:: https://badge.fury.io/py/pokepy.png
    :target: http://badge.fury.io/py/pokepy

.. image:: https://circleci.com/gh/PokeAPI/pokepy.svg?style=svg
    :target: https://circleci.com/gh/PokeAPI/pokepy

A python wrapper for `PokeAPI <https://pokeapi.co>`_

* Free software: BSD license
* Documentation: http://pokepy.rtfd.org.


Installation
------------

Nice and simple:

.. code-block:: bash

    $ pip install pokepy


Usage
-----

Even simpler:

.. code-block:: python

    >>> import pokepy
    >>> client = pokepy.V2Client()
    >>> client.get_pokemon(1)[0]
    <Pokemon - Bulbasaur>


Features
--------

* Generate Python objects from PokeAPI resources.
* Human-friendly API
