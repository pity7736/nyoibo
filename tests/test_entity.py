from nyoibo import Entity, fields


def test_entity():

    class Rate(Entity):
        _value = fields.StrField()

    rate = Rate(value='0.25')

    assert rate.value == '0.25'
