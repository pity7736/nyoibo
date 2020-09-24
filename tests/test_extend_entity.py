from pytest import mark

from nyoibo import Entity, fields


def test_additional_value():
    class Model(Entity):
        _int_value = fields.IntField()
        _str_value = fields.StrField()

        def _additional_value(self, key, field, value):
            if isinstance(field, fields.IntField) and value:
                return value + 1
            return value

    instance = Model(int_value=1, str_value='hi')

    assert instance.str_value == 'hi'
    assert instance.int_value == 2


immutable_params = (
    True,
    False
)


@mark.parametrize('immutable', immutable_params)
def test_additional_value_with_different_object_type(immutable):
    class Model0(Entity):
        _value = fields.StrField()

    class Related:

        def __init__(self, instance, field_name):
            self._instance = instance
            self._field_name = field_name

        def fetch(self):
            setattr(self._instance, self._field_name, Model0(value='hi world'))

    class ExtendedLinkField(fields.LinkField):
        _valid_values = (Related,)

    class Model1(Entity):
        _model0 = ExtendedLinkField(to=Model0, immutable=immutable)

        def _additional_value(self, key, field, value):
            if isinstance(field, ExtendedLinkField):
                return Related(self, key)
            return value

    instance0 = Model0(value='hi world')
    instance1 = Model1()

    assert instance0.value == 'hi world'
    assert isinstance(instance1.model0, Related)
    instance1.model0.fetch()
    assert instance1.model0.value == instance0.value
