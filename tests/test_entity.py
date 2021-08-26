import datetime
from enum import Enum

from pytest import raises, mark

from nyoibo import Entity, fields
from nyoibo.entities.meta_entity import MetaEntity
from nyoibo.exceptions import PrivateFieldError


class Types(Enum):
    value0 = 'value0'
    value1 = 'value1'
    value2 = 'value2'


class Rate(Entity):
    _value = fields.StrField(immutable=False)
    _other_value = fields.StrField()
    _default = fields.StrField(default_value='hello world')
    _other_default = fields.IntField(default_value=1)
    _private = fields.StrField(private=True)
    _immutable = fields.StrField()
    _type = fields.StrField(choices=Types)


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
    with raises(PrivateFieldError):
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
        _value = fields.IntField(private=False)

        def get_value(self):
            return self._value + 5

    getter = Getter(value=5)

    assert getter.value == 10
    assert getter.get_value() == 10


def test_override_setter():
    class Setter(Entity):
        _value = fields.IntField(private=False, immutable=False)

        def set_value(self, value):
            self._value = value + 5

    setter = Setter(value=5)

    assert setter.value == 10
    assert setter.get_value() == 10

    setter.value = 10
    assert setter.value == 15
    assert setter.get_value() == 15


def test_override_setter_with_parsing():
    class Setter(Entity):
        _value = fields.IntField(private=False, immutable=False)

        def set_value(self, value):
            value = Setter._value.parse(value)
            self._value = value + 5

    setter = Setter(value=5)

    assert setter.value == 10
    assert setter.get_value() == 10

    setter.value = '10'
    assert setter.value == 15
    assert setter.get_value() == 15


def test_set_value_from_other_field():
    class Setter(Entity):
        _value = fields.StrField(immutable=False)
        _other_value = fields.StrField()

        def set_value(self, value):
            value = Setter._value.parse(value)
            self._value = value
            self._other_value = f'{value} world'

    obj = Setter(value='hi')

    assert obj.value == 'hi'
    assert obj.other_value == 'hi world'


def test_set_value_from_other_field_with_different_order():
    class Setter(Entity):
        _other_value = fields.StrField()
        _value = fields.StrField(immutable=False)

        def set_value(self, value):
            value = Setter._value.parse(value)
            self._value = value
            self._other_value = f'{value} world'

    obj = Setter(value='hi')

    assert obj.value == 'hi'
    assert obj.other_value == 'hi world'


def test_set_none_to_immutable_field_if_value_is_not_passed():
    rate = Rate()
    assert rate.other_value is None


def test_private_value_is_assigned():
    class Private(Entity):
        _add = fields.IntField()
        _value = fields.IntField(private=False)

        def get_value(self):
            return self._add + self._value

    private = Private(add=5, value=5)

    assert private.value == 10


def test_choices():
    entity = Rate(type='value0')

    assert entity.type == Types.value0


wrong_link_to_values = (
    'hi',
    123,
    str,
    int,
    datetime.date
)


@mark.parametrize('to', wrong_link_to_values)
def test_wrong_to_in_link_field(to):
    with raises(ValueError) as e:
        class Example(Entity):
            _value = fields.LinkField(to=to)
    assert str(e.value) == 'to must be an Entity subclass'


def test_link_to_entity_with_other_metaclass():
    class OtherMetaEntity(MetaEntity):
        pass

    class Entity0(Entity, metaclass=OtherMetaEntity):
        _value = fields.StrField()

    class Entity1(Entity):
        _entity0 = fields.LinkField(to=Entity0)


def test_instance_entity_from_dict_with_link_field():
    class Model0(Entity):
        _value = fields.StrField()
        _int_value = fields.IntField()

    class Model1(Entity):
        _link = fields.LinkField(to=Model0)
        _name = fields.StrField()

    data = {
        'name': 'test',
        'link': {
            'value': 'hi world',
            'int_value': '5',
            'different_field': 'some value'
        }
    }
    instance = Model1(**data)
    assert instance.name == 'test'
    assert instance.link.value == 'hi world'
    assert instance.link.int_value == 5


def test_instance_entity_from_dict_with_empty_link_field_data():
    class Model0(Entity):
        _value = fields.StrField()
        _int_value = fields.IntField()

    class Model1(Entity):
        _link = fields.LinkField(to=Model0)
        _name = fields.StrField()

    data = {
        'name': 'test',
        'link': {}
    }
    instance = Model1(**data)
    assert instance.name == 'test'
    assert instance.link is None


def test_instance_entity_from_dict_with_link_field_in_2_depth():
    class Model0(Entity):
        _value = fields.StrField()
        _int_value = fields.IntField()

    class Model1(Entity):
        _link = fields.LinkField(to=Model0)
        _name = fields.StrField()

    class Model2(Entity):
        _value = fields.StrField()
        _link = fields.LinkField(to=Model1)

    data = {
        'value': 'some value',
        'link': {
            'name': 'test',
            'link': {
                'value': 'hi world',
                'int_value': '5',
                'different_field': 'some value'
            }
        }
    }
    instance = Model2(**data)
    assert instance.value == 'some value'
    assert instance.link.name == 'test'
    assert instance.link.link.value == 'hi world'
    assert instance.link.link.int_value == 5
