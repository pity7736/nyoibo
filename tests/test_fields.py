from pytest import mark

from nyoibo import Entity, fields


class TestEntity(Entity):
    _name = fields.StrField()
    _value = fields.IntField()


str_values = (
    ('10.5', '10.5'),
    (10, '10'),
    (15.2, '15.2')
)


@mark.parametrize('value, expected_result', str_values)
def test_parse_str_value(value, expected_result):
    entity = TestEntity(name=value)

    assert entity.name == expected_result


int_values = (
    ('10', 10),
    (10, 10),
    (15.2, 15),
)


@mark.parametrize('value, expected_result', int_values)
def test_parse_int_value(value, expected_result):
    entity = TestEntity(value=value)

    assert entity.value == expected_result
