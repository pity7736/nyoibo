from pytest import raises

from nyoibo import Entity, fields
from nyoibo.exceptions import PrivateField


def test_entity():

    class Rate(Entity):
        _value = fields.StrField()

    rate = Rate(value='0.25')

    assert rate.value == '0.25'


def test_fields_must_be_private():
    with raises(PrivateField):
        class Example(Entity):
            value = fields.StrField()
