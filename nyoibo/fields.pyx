import datetime
from decimal import Decimal, InvalidOperation

from nyoibo.entities.meta_entity import MetaEntity
from nyoibo.exceptions import FieldValueError


cdef class Field:
    """Base Field

    This is the base for all field types.

    Attributes:
        _internal_type: each Field subclass must to override this attribute
            with the internal type that field represent.
        _exceptions (tuple): possible exception that could be raised when
            field tries to cast to ``_internal_type``.

    Args:
        private (bool): set if field is private or not. When private=True
            getter and setters will not be created. False by default.
        immutable (bool): set if field is immutable or not. When immutable=True
            setter will not be created. True by default.
        default_value (any): default value to field.
        choices (Enum): value to this field must be a Enum key or Enum key.
    """

    _internal_type = None
    _exceptions = (TypeError, ValueError)

    def __init__(self, private=False, immutable=True, default_value=None,
                 choices=None):
        self.default_value = default_value
        self.private = private
        self.immutable = immutable
        self.choices = choices

    cpdef public parse(self, value):
        """Parse and cast to ``_internal_type``

        Args:
            value (any): value to parse.

        Returns:
            ``_internal_type`` if the casting was successful

        Raises:
            FieldValueError: if the casting failed.
        """
        try:
            value = self._parse(value)
            if value and self.choices:
                return self.choices(value)
            if value is None or isinstance(value, self._internal_type):
                return value
            return self._internal_type(value)
        except self._exceptions:
            raise FieldValueError(f'{type(value)} is not a valid value for '
                                  f'{self.__class__.__name__}')

    cdef _parse(self, value):
        """This method is to be overriding if some Field need do some checks or
            validations before ``parse`` is executed.

        Args:
            value (any): value to parse

        Returns:
            ``_internal_type`` if the casting was successful

        Raises:
            FieldValueError: if the casting failed.

        """
        return value


cdef class StrField(Field):
    """Field for string values
    """

    _internal_type = str


cdef class IntField(Field):
    """Field for integer values"""

    _internal_type = int

    cdef _parse(self, value):
        if isinstance(value, str):
            value = float(value)
        return value


cdef class BoolField(Field):
    """Field for boolean values
    """

    _internal_type = bool

    cdef _parse(self, value):
        if value in ('false', 'False'):
            return False
        return value


cdef class DateField(Field):
    """Field for datetime.date values

    Values could be datetime.date or isoformat string.
    """

    _internal_type = datetime.date

    cdef _parse(self, value):
        if isinstance(value, str):
            return datetime.date.fromisoformat(value)
        return value


cdef class DatetimeField(Field):
    """Field for datetime.datetime values

    Values could be datetime.datetime or isoformat string.
    """

    _internal_type = datetime.datetime

    cdef _parse(self, value):
        if isinstance(value, str):
            return datetime.datetime.fromisoformat(value)
        return value


cdef class FloatField(Field):
    """Field for float values
    """

    _internal_type = float


cdef class DecimalField(Field):
    """Field for Decimal values
    """

    _internal_type = Decimal
    _exceptions = (TypeError, InvalidOperation)


cdef class LinkField(Field):
    """Field for link between other ``Entity``

    _valid_values is useful to accept others types
    by inheritance

    Args:
        to (Entity): Entity instance

    Raises:
        ValueError: if ``to`` is not a subclass of :ref:`entity`
    """
    _valid_values = ()

    def __init__(self, to, *args, **kwargs):
        if issubclass(type(to), MetaEntity) is False:
            raise ValueError('to must be an Entity subclass')
        super(LinkField, self).__init__(*args, **kwargs)
        self.to = to

    cpdef public parse(self, value):
        if value is None or isinstance(value, (self.to, *self._valid_values)):
            return value
        raise FieldValueError(f'{type(value)} is not a valid value for '
                              f'{self.__class__.__name__}')
