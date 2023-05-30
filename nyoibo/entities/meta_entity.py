from typing import Dict, Any

from nyoibo.exceptions import PrivateFieldError
from nyoibo.fields import Field, TupleField

from nyoibo.utils import camel_to_snake_case


def create_getter(attr):
    def getter(self):
        return getattr(self, attr)
    return getter


def create_setter(attr):
    def setter(self, value):
        field = getattr(self.__class__, attr)
        setattr(self, attr, field.parse(value))
    return setter


class MetaEntity(type):

    def __new__(mcs, name, bases, namespace: Dict[str, Any]):
        getters_setters = {}
        fields = {}
        mcs._set_parents_fields(bases, fields)
        for attr, value in namespace.items():
            if isinstance(value, Field):
                if not attr.startswith('_'):
                    raise PrivateFieldError('Fields must be private')

                fields[attr] = value
                MetaEntity._set_getters_and_setters(
                    attr,
                    getters_setters,
                    value,
                    namespace
                )
                if isinstance(value, TupleField) and \
                        value.reverse_relationship and value.private is False:
                    class_name_snake_case = camel_to_snake_case(name)
                    setattr(
                        value.of,
                        class_name_snake_case,
                        property(create_getter(f'_{class_name_snake_case}'))
                    )

        namespace.update(getters_setters)
        namespace['_fields'] = fields
        return super().__new__(mcs, name, bases, namespace)

    @staticmethod
    def _set_parents_fields(bases, fields):
        for parent in bases:
            for field_name, field in parent._fields.items():
                fields[field_name] = field

    @staticmethod
    def _set_getters_and_setters(attr, getters_setters, field, namespace):
        field_name = attr.replace('_', '', 1)
        if field.private is False:
            getter_name = f'get_{field_name}'
            getter = namespace.get(getter_name) or create_getter(attr=attr)
            getters_setters[getter_name] = getter
            setter = None
            if field.mutable is True:
                setter_name = f'set_{field_name}'
                setter = namespace.get(setter_name) or create_setter(attr=attr)
                getters_setters[setter_name] = setter
            getters_setters[field_name] = property(getter, setter)
