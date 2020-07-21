import datetime
from decimal import Decimal

from nyoibo.exceptions import FieldValueError

cdef class Field:

    _internal_type = None

    def __init__(self, default_value=None, private=False, immutable=True,
                 choices=None):
        self.default_value = default_value
        self.private = private
        self.immutable = immutable
        self.choices = choices

    cpdef public parse(self, value):
        try:
            value = self._parse(value)
            if value and self.choices:
                return self.choices(value)
            if value is None or type(value) is self._internal_type:
                return value
            return self._internal_type(value)
        except (TypeError, ValueError):
            raise FieldValueError(f'{type(value)} is not a valid value for '
                                  f'{self.__class__.__name__}')

    cdef _parse(self, value):
        return value


cdef class StrField(Field):

    _internal_type = str


cdef class IntField(Field):

    _internal_type = int

    cdef _parse(self, value):
        if isinstance(value, str):
            value = float(value)
        return value


cdef class BoolField(Field):

    _internal_type = bool

    cdef _parse(self, value):
        if value in ('false', 'False'):
            return False
        return value


cdef class DateField(Field):

    _internal_type = datetime.date

    cdef _parse(self, value):
        if isinstance(value, str):
            return datetime.date.fromisoformat(value)
        return value


cdef class DatetimeField(Field):

    _internal_type = datetime.datetime

    cpdef public parse(self, value):
        if isinstance(value, str):
            return datetime.datetime.fromisoformat(value)
        return super(DatetimeField, self).parse(value)


cdef class FloatField(Field):

    _internal_type = float


cdef class DecimalField(Field):

    _internal_type = Decimal


cdef class LinkField(Field):

    def __init__(self, to, *args, **kwargs):
        super(LinkField, self).__init__(*args, **kwargs)
        self.to = to

    cpdef public parse(self, value):
        return value
