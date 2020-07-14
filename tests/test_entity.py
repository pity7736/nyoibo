from pytest import raises

from nyoibo import Entity, fields
from nyoibo.exceptions import PrivateField


class Rate(Entity):
    _value = fields.StrField()
    _other_value = fields.StrField()
    _default = fields.StrField(default_value='hello world')
    _other_default = fields.IntField(default_value=1)
    _private = fields.StrField(private=True)
    _immutable = fields.StrField(immutable=True)


def test_get_value():
    rate = Rate(value='0.25', other_value='hello world')

    assert rate.value == '0.25'
    assert rate.get_value() == '0.25'
    assert rate.other_value == 'hello world'


def test_get_uninitialized_value():
    rate = Rate()

    assert rate.value is None
    assert rate.other_value is None


def test_set_value():
    rate = Rate()
    rate.value = '0.25'

    assert rate.value == '0.25'
    rate.set_value('0.1')
    assert rate.value == '0.1'


def test_fields_must_be_private():
    with raises(PrivateField):
        class Example(Entity):
            value = fields.StrField()


def test_default_values():
    rate = Rate()

    assert rate.default == 'hello world'
    assert rate.other_default == 1


def test_private_field():
    entity = Rate(private='some value')
    with raises(AttributeError):
        print(entity.private)


def test_private_field_getter():
    entity = Rate(private='some value')
    with raises(AttributeError):
        print(entity.get_private())


def test_immutable_field():
    entity = Rate(immutable='some value')

    assert entity.immutable == 'some value'
    with raises(AttributeError):
        entity.immutable = 'other value'

    with raises(AttributeError):
        entity.set_immutable('other value2')


def test_override_getter():
    class Getter(Entity):
        _value = fields.IntField()

        def get_value(self):
            return self._value + 5

    getter = Getter(value=5)

    assert getter.value == 10
    assert getter.get_value() == 10


def test_override_setter():
    class Setter(Entity):
        _value = fields.IntField()

        def set_value(self, value):
            self._value = value + 5

    setter = Setter(value=5)

    assert setter.value == 10
    assert setter.get_value() == 10

    setter.value = 10
    assert setter.value == 15
    assert setter.get_value() == 15
