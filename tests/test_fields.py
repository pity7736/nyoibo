import datetime
from decimal import Decimal

from pytest import mark, raises

from nyoibo import Entity, fields


class TestEntity(Entity):
    _name = fields.StrField()
    _value = fields.IntField()
    _is_valid = fields.BoolField()
    _date = fields.DateField()
    _datetime = fields.DatetimeField()
    _points = fields.FloatField()
    _rate = fields.DecimalField()
    _private = fields.StrField(private=True)


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
    ('15.2', 15),
)


@mark.parametrize('value, expected_result', int_values)
def test_parse_int_value(value, expected_result):
    entity = TestEntity(value=value)

    assert entity.value == expected_result


bool_values = (
    (True, True),
    (False, False),
    (1, True),
    (0, False),
    ('True', True),
    ('False', False),
    ('false', False),
)


@mark.parametrize('value, expected_result', bool_values)
def test_parse_bool_value(value, expected_result):
    entity = TestEntity(is_valid=value)

    assert entity.is_valid == expected_result


date_values = (
    (datetime.date(2020, 7, 7), datetime.date(2020, 7, 7)),
    ('2020-07-07', datetime.date(2020, 7, 7)),
)


@mark.parametrize('value, expected_result', date_values)
def test_parse_date_value(value, expected_result):
    entity = TestEntity(date=value)

    assert entity.date == expected_result


datetime_values = (
    (
        datetime.datetime(2020, 7, 7, 22, 29, 30),
        datetime.datetime(2020, 7, 7, 22, 29, 30)
    ),
    (
        '2020-07-07T22:29:30',
        datetime.datetime(2020, 7, 7, 22, 29, 30)
    ),
)


@mark.parametrize('value, expected_result', datetime_values)
def test_parse_datetime_value(value, expected_result):
    entity = TestEntity(datetime=value)

    assert entity.datetime == expected_result


float_values = (
    (2.5, 2.5),
    (2, 2.0),
    ('2.5', 2.5)
)


@mark.parametrize('value, expected_result', float_values)
def test_parse_float_value(value, expected_result):
    entity = TestEntity(points=value)

    assert entity.points == expected_result


decimal_values = (
    (Decimal('2.5'), Decimal('2.5')),
    ('2.5', Decimal('2.5')),
    (2, Decimal('2')),
)


@mark.parametrize('value, expected_result', decimal_values)
def test_parse_decimal_values(value, expected_result):
    entity = TestEntity(rate=value)

    assert entity.rate == expected_result


def test_private_field():
    entity = TestEntity(private='some value')
    with raises(AttributeError):
        print(entity.private)


def test_private_field_getter():
    entity = TestEntity(private='some value')
    with raises(AttributeError):
        print(entity.get_private())
