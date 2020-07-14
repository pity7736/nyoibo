from typing import Dict, Any

from nyoibo.exceptions import PrivateField
from nyoibo.fields import Field


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
        for attr, value in namespace.items():
            if isinstance(value, Field):
                if not attr.startswith('_'):
                    raise PrivateField('Fields must be private')

                MetaEntity._set_getters_and_setters(
                    attr,
                    fields,
                    getters_setters,
                    value,
                    namespace
                )

        namespace.update(getters_setters)
        namespace['_fields'] = fields
        return super().__new__(mcs, name, bases, namespace)

    @staticmethod
    def _set_getters_and_setters(attr, fields, getters_setters, value,
                                 namespace):
        if value.private is False:
            field_name = attr.replace('_', '', 1)
            fields[field_name] = value
            getter_name = f'get_{field_name}'
            getter = namespace.get(getter_name) or create_getter(attr=attr)
            getters_setters[getter_name] = getter
            setter = None
            if value.immutable is False:
                setter_name = f'set_{field_name}'
                setter = namespace.get(setter_name) or create_setter(attr=attr)
                getters_setters[setter_name] = setter
            getters_setters[field_name] = property(getter, setter)
