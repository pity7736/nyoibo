from nyoibo cimport fields
from .meta_entity import MetaEntity


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
            value = kwargs.get(key, None)
            if value is None:
                value = field.default_value
            if field.mutable is False or field.private is True:
                key = f'_{key}'
                current_value = getattr(self, key)
                print('current value 0', current_value, type(current_value))
                if issubclass(type(current_value), fields.Field):
                    # raise ValueError()
                    print('current value 1', current_value, type(current_value))
                    current_value = None
                value = field.parse(current_value or value)
            value = self._additional_value(key, field, value)
            setattr(self, key, value)

    def _additional_value(self, key, field, value):
        """additional value

        This is useful if you want change the behavior
        by inheritance.
        """
        return value
