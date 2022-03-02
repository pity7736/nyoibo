Usage
=====

Getting started
---------------

Nyoibo is an easy way to avoid repetitive code with "private" attributes in
Python. With this tool you can create ``__init__``, getters, setters and
properties automatically for each public and mutable field. For example:

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
        _other_value = fields.IntField(mutable=True)
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


Visibility
----------

All fields are public and immutable by default, so it will create getter,
property but not setter. You can change this behavior with ``private=True`` or
``mutable=True`` arguments on fields. Fields with ``private=True`` will not
create getter or setter. Fields with ``mutable=True`` will create getter,
setter and property.

.. code-block:: python

    from nyoibo import Entity, fields

    class Example(Entity):
        _attr = fields.StrField()
        _mutable_attr = fields.StrField(mutable=True)
        _private_attr = fields.StrField(private=True)

An ``Example`` instance will have ``get_attr`` method and ``attr`` property
for ``_attr`` field; ``get_mutable_attr``, ``set_mutable_attr`` methods and
``mutable_attr`` properties for ``_mutable_attr`` field.
So, you can get value from attr like this:

.. code-block:: python

    example = Example(attr='some value')
    print(example.attr)  # some value
    print(example.get_attr())  # some value
    # if you try to get value for private attr, AttributteError will be raised.
    print(example.private_attr)  # AttributeError

And you can set value in mutable fields like this:

.. code-block:: python

    example = Example(attr='some value', mutable_attr='other some value')
    example.mutable_attr = 'hi world'
    # or
    example.set_mutable_attr('hi world')
    print(example.mutable_attr)  # hi world
    example.attr = 'hello world'  # AttributeError


Overriding
----------

You can "override" getters or setters, all you need to do is create getter or
setter in ``get_{field_name}`` or ``set_{field_name}`` way. Example:

.. code-block:: python

    class Example(Entity):
        _private = fields.IntField(private=True)
        _public = fields.IntField()
        _mutable = fields.IntField(mutable=True)

        def get_public(self):
            if self._private:
                return self._private + self._public
            return self._public

        def set_mutable(self, value):
            self._mutable = value + self.public
            # or if you want parse and cast value to right type.
            self._mutable = Example._mutable.parse(value) + self.public


    example = Example(private=10, public=10, mutable=10)
    print(example.public)  # 20
    print(example.mutable)  # 10
    example.mutable = 20
    print(example.mutable)  # 40


Fields
------

Nyoibo has several fields type (you can check all types in :ref:`fields`).
Each field has an internal Python type and it will try to parse and cast to
this Python type. So ``StrField`` will cast to ``str``, ``IntField`` will cast
to ``int``, ``FloatField`` to ``float`` and so on. Let's see an example:

.. code-block:: python

    from nyoibo import Entity, fields

    class Example(Entity):
        _str_field = fields.StrField()
        _int_field = fields.IntField()
        _float_field = fields.FloatField()
        _date_field = fields.DateField()


    example = Example(
        str_field=123,
        int_field='123',
        float_field='123.5',
        date_field='2020-07-21'
    )
    print(example.str_field)  # '123'
    print(example.int_field)  # 123
    print(example.float_field)  # 123.5
    print(example.date_field)  # datetime.date(2020, 7, 21)

If nyoibo can't cast to right type, it will raise ``FieldValueError``.
Example using above code:

.. code-block:: python

    # this will raise FieldValueError
    example = Example(
        str_field=123,
        int_field='123',
        float_field='123.5',
        date_field=123  # wrong type value
    )

.. important::
    Parsing and casting is made both constructor and setter.
