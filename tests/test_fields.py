from nyoibo import Entity, fields


class TestEntity(Entity):
    _name = fields.StrField()
    _value = fields.IntField()


def test_parse_str_value():
    entity = TestEntity(name=10)

    assert entity.name == '10'


def test_parse_int_value():
    entity = TestEntity(value='10')

    assert entity.value == 10
