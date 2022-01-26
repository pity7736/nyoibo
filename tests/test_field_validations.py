from pytest import raises

from nyoibo import fields
from nyoibo.exceptions import RequiredValueError


def test_required_value():
    field = fields.StrField(required=True)
    with raises(RequiredValueError) as e:
        field.parse(None)

    assert str(e.value) == 'value is required'
