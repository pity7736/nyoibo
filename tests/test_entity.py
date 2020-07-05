from pytest import raises

from nyoibo import Entity, fields
from nyoibo.exceptions import PrivateField


class Rate(Entity):
    _value = fields.StrField()
    _other_value = fields.StrField()


def test_get_value():
    rate = Rate(value='0.25', other_value='hello world')

    assert rate.value == '0.25'
    assert rate.get_value() == '0.25'
    assert rate.other_value == 'hello world'


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
