from typing import Dict, Any

from nyoibo.exceptions import PrivateField
from nyoibo.fields import StrField


def create_getter(attr):
    def getter(self):
        return getattr(self, attr)
    return getter


def create_setter(attr):
    def setter(self, value):
        setattr(self, attr, value)
    return setter


class MetaEntity(type):

    def __new__(mcs, name, bases, namespace: Dict[str, Any]):
        getters_setters = {}
        fields = {}
        for attr, value in namespace.items():
            if isinstance(value, StrField):
                if not attr.startswith('_'):
                    raise PrivateField('Fields must be private')

                field_name = attr.replace('_', '', 1)
                fields[field_name] = value
                getter = create_getter(attr=attr)
                getters_setters[f'get_{field_name}'] = getter
                setter = create_setter(attr=attr)
                getters_setters[f'set_{field_name}'] = setter
                getters_setters[field_name] = property(getter, setter)

        namespace.update(getters_setters)
        namespace['_fields'] = fields
        return super().__new__(mcs, name, bases, namespace)
