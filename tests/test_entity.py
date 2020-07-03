from pytest import raises

from nyoibo import Entity, fields
from nyoibo.exceptions import PrivateField


class Rate(Entity):
    _value = fields.StrField()


def test_entity():
    rate = Rate(value='0.25')

    assert rate.value == '0.25'


def test_fields_must_be_private():
    with raises(PrivateField):
        class Example(Entity):
            value = fields.StrField()


def test_set_value():
    rate = Rate()
    rate.value = '0.25'

    assert rate.value == '0.25'
