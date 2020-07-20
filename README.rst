Nyoibo
======

.. image:: https://readthedocs.org/projects/nyoibo/badge/?version=latest
    :target: https://nyoibo.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://circleci.com/gh/pity7736/nyoibo.svg?style=shield
    :target: https://circleci.com/gh/pity7736/nyoibo

Nyoibo is to avoid boilerplate easily working with "private" attributes
in python.

`See full documentation <https://nyoibo.readthedocs.io/en/latest/>`_

Basic Usage
-----------

.. code-block:: python

    from nyoibo import Entity, fields


    class Example(Entity):
        _value = fields.StrField()
        _other_value = fields.IntField(private=False)
        _default = fields.StrField(default_value='hello world')

        def do_something(self):
            return f'{self._value} world'

    example = Example(value='hi', other_value=10)

    assert example.other_value == 10
    assert example.get_other_value() == 10
    assert exmaple.do_something() == 'hi world'


License
-------

Distributed under the terms of the GPLv3 license.

See `license <https://github.com/pity7736/nyoibo/blob/master/LICENSE>`_.
