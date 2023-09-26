import datetime
from enum import Enum

from pytest import raises, mark

from nyoibo import Entity, fields
from nyoibo.entities.meta_entity import MetaEntity
from nyoibo.exceptions import PrivateFieldError, RequiredValueError


class Types(Enum):
    value0 = 'value0'
    value1 = 'value1'
    value2 = 'value2'


class Rate(Entity):
    _value = fields.StrField(mutable=True)
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
        _value = fields.IntField(private=False, mutable=True)

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
        _value = fields.IntField(private=False, mutable=True)

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
        _value = fields.StrField(mutable=True)
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
        _value = fields.StrField(mutable=True)

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


def test_with_required_field():
    class Model(Entity):
        _value = fields.StrField(required=True)

    with raises(RequiredValueError):
        Model()


def test_fields_with_aliases():
    class MyModel(Entity):
        _first_name = fields.StrField(alias='nombres')
        _last_name = fields.StrField(alias='apellidos')

    instance0 = MyModel(nombres='julián', apellidos='cortés')
    instance1 = MyModel(first_name='julián', last_name='cortés')

    assert instance0.first_name == 'julián'
    assert instance0.last_name == 'cortés'
    assert instance1.first_name == 'julián'
    assert instance1.last_name == 'cortés'


def test_instance_from_dict_with_aliases():
    class MyModel(Entity):
        _first_name = fields.StrField(alias='nombres')
        _last_name = fields.StrField(alias='apellidos')

    data = {
        'nombres': 'julián',
        'apellidos': 'cortés'
    }
    instance = MyModel(**data)

    assert instance.first_name == 'julián'
    assert instance.last_name == 'cortés'


def test_prioritize_field_alias():
    class MyModel(Entity):
        _first_name = fields.StrField(alias='nombres')
        _last_name = fields.StrField(alias='apellidos')

    instance = MyModel(first_name='some name', nombres='julián')

    assert instance.first_name == 'julián'


def test_instance_from_dict_with_tuple_field():
    class License(Entity):
        _category = fields.StrField()

        def __eq__(self, other):
            return self._category == other._category

    class Owner(Entity):
        _name = fields.StrField()
        _licenses = fields.TupleField(of=License, reverse_relationship=True)

    data = {
        'name': 'test owner name',
        'licenses': (
            {
                'category': 'A1'
            },
            {
                'category': 'A2'
            }
        )
    }
    owner = Owner(**data)

    assert owner.name == 'test owner name'
    assert owner.licenses == (
        License(category='A1'),
        License(category='A2')
    )
    assert owner.licenses[0].owner == owner
    assert owner.licenses[1].owner == owner


def test_reverse_relationship():
    class License(Entity):
        _category = fields.StrField()

        def __eq__(self, other):
            return self._category == other._category

    class OwnerModel(Entity):
        _name = fields.StrField()
        _licenses = fields.TupleField(of=License, reverse_relationship=True)

        def __eq__(self, other):
            return self._name == other._name

    owner = OwnerModel(
        name='test name',
        licenses=(
            License(category='A1'),
            License(category='A2')
        )
    )

    assert owner.licenses[0].owner_model == owner
    assert owner.licenses[1].owner_model == owner


def test_reverse_relationship_with_private_field():
    class License(Entity):
        _category = fields.StrField()

        def compare_owner(self, owner):
            return self._owner == owner

        def __eq__(self, other):
            return self._category == other._category

    class Owner(Entity):
        _name = fields.StrField()
        _licenses = fields.TupleField(
            of=License,
            reverse_relationship=True,
            private=True
        )

        def __eq__(self, other):
            return self._name == other._name
    lic = License(category='A1')
    owner = Owner(
        name='test name',
        licenses=(lic,)
    )

    assert lic.compare_owner(owner) is True
    with raises(AttributeError):
        lic.owner


def test_reverse_relationship_with_none_value():
    class Model0(Entity):
        _name = fields.StrField()

    class Model1(Entity):
        _models = fields.ListField(of=Model0)

    model1 = Model1()
    assert model1.models is None
