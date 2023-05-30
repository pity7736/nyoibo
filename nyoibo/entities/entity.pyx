from nyoibo cimport fields
from .meta_entity import MetaEntity
from ..utils import camel_to_snake_case


class Entity(metaclass=MetaEntity):
    """Entity.

    This class must be superclass for classes that you want create getters or
    setters.
    All fields must starts with ``_``.

    Args:
        kwargs: values to fields.

    Raises:
        FieldValueError: if the casting failed.
        PrivateFieldError: if a field does not start with ``_``.
            This exception is raised when program starts.
    """

    def __init__(self, **kwargs):
        cdef str key
        cdef fields.Field field
        for key, field in self._fields.items():
            key = key.replace('_', '', 1)
            value = kwargs.get(field.alias) or kwargs.get(key)
            if value is None:
                value = field.default_value
            if field.mutable is False or field.private is True:
                key = f'_{key}'
                current_value = getattr(self, key)
                if issubclass(type(current_value), fields.Field):
                    current_value = None
                value = field.parse(current_value or value)

            setattr(self, key, value)
            if isinstance(field, fields.TupleField) and field.reverse_relationship:
                for subfield in value:
                    setattr(subfield, f'_{camel_to_snake_case(self.__class__.__name__)}', self)
