import datetime
from decimal import Decimal

from pytest import mark, raises

from nyoibo import Entity, fields
from nyoibo.exceptions import FieldValueError

str_values = (
    ('10.5', '10.5'),
    (10, '10'),
    (15.2, '15.2')
)


@mark.parametrize('value, expected_result', str_values)
def test_parse_str_value(value, expected_result):
    str_field = fields.StrField()
    assert str_field.parse(value) == expected_result


int_values = (
    ('10', 10),
    (10, 10),
    (15.2, 15),
    ('15.2', 15),
)


@mark.parametrize('value, expected_result', int_values)
def test_parse_int_value(value, expected_result):
    int_field = fields.IntField()
    assert int_field.parse(value) == expected_result


wrong_int_values = (
    'hi',
    datetime.date.today(),
    datetime.datetime.today(),
)


@mark.parametrize('value', wrong_int_values)
def test_wrong_int_value(value):
    int_field = fields.IntField()
    with raises(FieldValueError) as e:
        int_field.parse(value)
    assert str(e.value) == f'{type(value)} is not a valid value for IntField'


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
    bool_field = fields.BoolField()
    assert bool_field.parse(value) == expected_result


date_values = (
    (datetime.date(2020, 7, 7), datetime.date(2020, 7, 7)),
    ('2020-07-07', datetime.date(2020, 7, 7)),
)


@mark.parametrize('value, expected_result', date_values)
def test_parse_date_value(value, expected_result):
    date_field = fields.DateField()
    assert date_field.parse(value) == expected_result


wrong_date_values = (
    'hi',
    12354
)


@mark.parametrize('value', wrong_date_values)
def test_wrong_date_value(value):
    date_field = fields.DateField()
    with raises(FieldValueError) as e:
        date_field.parse(value)
    assert str(e.value) == f'{type(value)} is not a valid value for DateField'


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
    datetime_field = fields.DatetimeField()
    assert datetime_field.parse(value) == expected_result


wrong_datetime_values = (
    'hi',
    12354
)


@mark.parametrize('value', wrong_datetime_values)
def test_wrong_datetime_value(value):
    datetime_field = fields.DatetimeField()
    with raises(FieldValueError) as e:
        datetime_field.parse(value)
    assert str(e.value) == f'{type(value)} is not a valid value for ' \
                           'DatetimeField'


float_values = (
    (2.5, 2.5),
    (2, 2.0),
    ('2.5', 2.5)
)


@mark.parametrize('value, expected_result', float_values)
def test_parse_float_value(value, expected_result):
    float_field = fields.FloatField()
    assert float_field.parse(value) == expected_result


wrong_float_values = (
    'hi',
    datetime.date.today()
)


@mark.parametrize('value', wrong_float_values)
def test_wrong_float_value(value):
    float_field = fields.FloatField()
    with raises(FieldValueError) as e:
        float_field.parse(value)
    assert str(e.value) == f'{type(value)} is not a valid value for FloatField'


decimal_values = (
    (Decimal('2.5'), Decimal('2.5')),
    ('2.5', Decimal('2.5')),
    (2, Decimal('2')),
)


@mark.parametrize('value, expected_result', decimal_values)
def test_parse_decimal_values(value, expected_result):
    decimal_field = fields.DecimalField()
    assert decimal_field.parse(value) == expected_result


wrong_decimal_values = (
    'hi',
    datetime.date.today()
)


@mark.parametrize('value', wrong_decimal_values)
def test_wrong_decimal_value(value):
    decimal_field = fields.DecimalField()
    with raises(FieldValueError) as e:
        decimal_field.parse(value)
    assert str(e.value) == f'{type(value)} is not a valid value for ' \
                           'DecimalField'


def test_parse_link_field():
    class NewEntity(Entity):
        _value = fields.StrField()

    link_field = fields.LinkField(to=NewEntity)
    new_entity = NewEntity()
    assert link_field.parse(new_entity) == new_entity


def test_parse_none_link_field():
    class NewEntity(Entity):
        pass

    link_field = fields.LinkField(to=NewEntity)
    assert link_field.parse(None) is None


wrong_link_values = (
    '123',
    123,
    datetime.date.today()
)


@mark.parametrize('value', wrong_link_values)
def test_wrong_link_value(value):
    class Example(Entity):
        _value = fields.StrField()

    link_field = fields.LinkField(to=Example)
    with raises(FieldValueError) as e:
        link_field.parse(value)
    assert str(e.value) == f'{type(value)} is not a valid value for LinkField'


def test_parse_link_field_from_dict():
    class NewEntity(Entity):
        _field0 = fields.StrField()
        _field1 = fields.IntField()

    link_field = fields.LinkField(to=NewEntity)
    data = {
        'field0': 'hi',
        'field1': '10'
    }
    parsed = link_field.parse(data)
    assert parsed.field0 == 'hi'
    assert parsed.field1 == 10


def test_parse_link_field_from_dict_with_wrong_data():
    class NewEntity(Entity):
        _field0 = fields.StrField()
        _field1 = fields.IntField()

    link_field = fields.LinkField(to=NewEntity)
    data = {
        'field32': 'hi',
        'field2': '10'
    }
    parsed = link_field.parse(data)
    assert parsed.field0 is None
    assert parsed.field1 is None


def test_parse_dict_field():
    field = fields.DictField()
    data = {
        'name': 'Julian',
        'gender': 'male'
    }
    assert field.parse(data) == data
