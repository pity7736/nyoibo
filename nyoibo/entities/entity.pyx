from nyoibo cimport fields
from .meta_entity import MetaEntity


class Entity(metaclass=MetaEntity):

    def __init__(self, **kwargs):
        cdef str key
        cdef fields.Field field
        for key, field in self._fields.items():
            key = key.replace('_', '', 1)
            value = kwargs.get(key, None)
            if value is None:
                value = field.default_value
            if field.immutable is True or field.private is True:
                key = f'_{key}'
                value = field.parse(value)
            setattr(self, key, value)
