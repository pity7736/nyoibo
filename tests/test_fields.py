import datetime

from pytest import mark

from nyoibo import Entity, fields


class TestEntity(Entity):
    _name = fields.StrField()
    _value = fields.IntField()
    _is_valid = fields.BoolField()
    _date = fields.DateField()
    _datetime = fields.DatetimeField()


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
