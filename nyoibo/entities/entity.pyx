from nyoibo cimport fields
from .meta_entity import MetaEntity


class Entity(metaclass=MetaEntity):

    def __init__(self, **kwargs):
        cdef str key
        cdef fields.StrField field
        for key, field in self._fields.items():
            value = kwargs.get(key, None)
            setattr(self, key, value)
