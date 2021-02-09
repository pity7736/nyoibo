Nyoibo
======

.. image:: https://readthedocs.org/projects/nyoibo/badge/?version=latest
    :target: https://nyoibo.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://circleci.com/gh/pity7736/nyoibo.svg?style=shield
    :target: https://circleci.com/gh/pity7736/nyoibo

Nyoibo is an easy way to avoid repetitive code with "private" attributes in
Python.

`See full documentation <https://nyoibo.readthedocs.io/en/latest/>`_


Installation
------------

You can install nyoibo with pip. Nyoibo requires python 3.6 or later.

``pip install nyoibo``


What does "nyoibo" mean?
------------------------

Nyoibo is a mystical staff given to Son Goku by his grandfather Son Gohan.

.. image:: ./nyoibo.png
   :width: 300px
   :height: 300px
   :alt: nyoibo


Usage
-----

Instead of doing this:

.. code-block:: python

    class Example:

        def __init__(self, value=None, other_value=None, default='hello')
            self._value = value
            self._other_value = other_value
            self._default = default

        def get_value(self):
            return self._value

        value = property(get_value)

        def get_other_value(self):
            return self._other_value

        def set_other_value(self, value):
            self._other_value = value

        other_value = property(get_other_value, set_other_value)

        def do_something(self):
            return f'{self._default} world'


You can do this:

.. code-block:: python

    from nyoibo import Entity, fields


    class Example(Entity):
        _value = fields.StrField()
        _other_value = fields.IntField(immutable=False)
        _default = fields.StrField(private=True, default_value='hello')

        def do_something(self):
            return f'{self._default} world'

In both cases you could use this code like this:

.. code-block:: python

    example = Example(value='some value', other_value=10)

    assert example.value == 'some value'
    assert example.get_value() == 'some value'
    assert example.get_other_value() == 10
    example.other_value = 15
    assert example.get_other_value() == 15
    assert example.do_something() == 'hello world'


Why not use dataclass decorator?
--------------------------------

``@dataclass`` decorator helps to avoid to write the ``__init__`` method but if you
want to use this approach (information hiding and encapsulation), you need to
write getters and setters anyway. Furthermore, with ``nyoibo`` you get extra
features like casting to right value (due to static typing), validations
(coming soon), override ``__init__`` method and so on.

Above example with ``dataclass`` decorator:

.. code-block:: python

    from dataclasses import dataclass


    @dataclass
    class Example:
        _value: str
        _other_value: int
        _default: str = 'hello'

        def get_value(self):
            return self._value

        value = property(get_value)

        def get_other_value(self):
            return self._other_value

        def set_other_value(self, value):
            self._other_value = value

        other_value = property(get_other_value, set_other_value)

        def do_something(self):
            return f'{self._default} world'

Even this code doesn't work becasue ``__init__`` method has ``_value``,
``_other_value`` and ``_default`` arguments. Therefore the instantation will be:

.. code-block:: python

    example = Example(_value='some value', _other_value=10)


TODO
----

- Custom validation for fields
- Arrays fields (lists, tuples)
- DictField
- JsonField
- Container field

License
-------

Distributed under the terms of the LGPLv3 license.

See `license <https://github.com/pity7736/nyoibo/blob/master/LICENSE>`_.
