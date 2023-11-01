from pytest import raises

from nyoibo import fields, Entity
from nyoibo.exceptions import RequiredValueError


def test_required_value():
    class Model(Entity):
        _field_name = fields.StrField(required=True)

    with raises(RequiredValueError) as e:
        Model()

    assert str(e.value) == ('missing required value for <field_name> field in '
                            'model <Model>')
