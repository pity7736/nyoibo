import datetime
import json
from decimal import Decimal

from pytest import mark, raises

from nyoibo import Entity, fields
from nyoibo.exceptions import FieldValueError, StrLengthError, \
    IntMinValueError, IntMaxValueError, RequiredValueError

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
    (datetime.datetime(2020, 7, 7), datetime.date(2020, 7, 7)),
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


date_string_formats = (
    (
        (),
        '2023-10-23',
        datetime.date(2023, 10, 23)
    ),
    (
        ('%d/%m/%Y',),
        '23/10/2023',
        datetime.date(2023, 10, 23)
    ),
    (
        ('%d/%m/%y', '%d/%m/%Y',),
        '23/10/23',
        datetime.date(2023, 10, 23)
    ),
)


@mark.parametrize('formats, value, expected_result', date_string_formats)
def test_date_formats(formats, value, expected_result):
    date_field = fields.DateField(formats=formats)
    assert date_field.parse(value) == expected_result


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


datetime_string_formats = (
    (
        (),
        '2023-10-23',
        datetime.datetime(2023, 10, 23, 0, 0, 0)
    ),
    (
        ('%d/%m/%Y',),
        '23/10/2023',
        datetime.datetime(2023, 10, 23, 0, 0, 0)
    ),
    (
        ('%d/%m/%y', '%d/%m/%Y',),
        '23/10/23',
        datetime.datetime(2023, 10, 23, 0, 0, 0)
    ),
    (
        ('%d/%m/%y', '%d/%m/%Y %H:%M',),
        '23/10/2023 22:32',
        datetime.datetime(2023, 10, 23, 22, 32, 0)
    ),
)


@mark.parametrize('formats, value, expected_result', datetime_string_formats)
def test_datetime_formats(formats, value, expected_result):
    date_field = fields.DatetimeField(formats=formats)
    assert date_field.parse(value) == expected_result


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


def test_parse_required_link_field():
    class Linked(Entity):
        _value = fields.StrField()

    link_field = fields.LinkField(to=Linked, required=True)
    with raises(RequiredValueError):
        link_field.parse(None)


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


def test_str_max_length():
    field = fields.StrField(max_length=10)
    with raises(StrLengthError) as e:
        field.parse('this is a longer string than max')

    assert str(e.value) == 'length value (32) is greater than max_value (10)'


def test_str_max_length_is_positive():
    with raises(AssertionError):
        fields.StrField(max_length=-1)


def test_int_min_value():
    field = fields.IntField(min_value=0)
    with raises(IntMinValueError) as e:
        field.parse(-1)

    assert str(e.value) == 'value (-1) must be >= min_value (0)'


def test_assert_int_min_value_is_integer():
    with raises(AssertionError):
        fields.IntField(min_value='some value')


def test_int_max_value():
    field = fields.IntField(max_value=10)
    with raises(IntMaxValueError) as e:
        field.parse(11)

    assert str(e.value) == 'value (11) must be <= max_value (10)'


def test_assert_int_max_value_is_integer():
    with raises(AssertionError):
        fields.IntField(max_value='some value')


def test_parse_json_field():
    field = fields.JSONField()
    data = {
        'name': 'Julian',
        'gender': 'male'
    }
    assert field.parse(data) == json.dumps(data)


def test_parse_json_field_with_invalid_data():
    field = fields.JSONField()
    data = datetime.date.today()
    with raises(FieldValueError) as e:
        field.parse(data)

    assert str(e.value) == f'data {data} is not serializable'


def test_parse_tuple_field():
    field = fields.TupleField()
    assert field.parse([1, 2, 3]) == (1, 2, 3)


def test_parse_tuple_field_with_type():
    field = fields.TupleField(of=int)
    assert field.parse((1, '2', 3, 4.0)) == (1, 2, 3, 4)


def test_parse_tuple_field_with_invalid_type():
    field = fields.TupleField(of=int)
    with raises(FieldValueError) as error:
        field.parse((1, 2, 3, 'hi'))

    assert str(error.value) == "type <class 'str'> of hi value is not a " \
                               "valid type of <class 'int'>"


def test_parse_tuple_field_with_entity_type():
    class Person(Entity):
        _name = fields.StrField()

    field = fields.TupleField(of=Person)
    people = (
        Person(name='john doe'),
        Person(name='jane')
    )
    assert field.parse(people) == people


def test_parse_tuple_field_with_invalid_entity_type():
    class Person(Entity):
        _name = fields.StrField()

    field = fields.TupleField(of=Person)
    people = (
        Person(name='john doe'),
        123
    )
    with raises(FieldValueError):
        field.parse(people)


def test_parse_list_field():
    field = fields.ListField()
    assert field.parse((1, 2, 3)) == [1, 2, 3]


def test_parse_list_field_with_type():
    field = fields.ListField(of=int)
    assert field.parse((1, '2', 3, 4.0)) == [1, 2, 3, 4]


def test_tuple_field_with_reverse_relationship():
    with raises(ValueError) as e:
        fields.TupleField(reverse_relationship=True)

    assert str(e.value) == 'to make a reverse relationship, ' \
                           '`of` parameter must to be set'
