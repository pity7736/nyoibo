import datetime
from decimal import Decimal

cdef class Field:

    _internal_type = None

    cpdef public parse(self, value):
        if value is None or type(value) is self._internal_type:
            return value
        return self._internal_type(value)


cdef class StrField(Field):

    _internal_type = str


cdef class IntField(Field):

    _internal_type = int

    cpdef public parse(self, value):
        if isinstance(value, str):
            value = float(value)

        # I implemented super in python 2 form because cython
        # has an issue with super without arguments
        # https://github.com/cython/cython/issues/3726
        return super(IntField, self).parse(value)


cdef class BoolField(Field):

    _internal_type = bool

    cpdef public parse(self, value):
        if value in ('false', 'False'):
            return False
        return super(BoolField, self).parse(value)


cdef class DateField(Field):

    _internal_type = datetime.date

    cpdef public parse(self, value):
        if isinstance(value, str):
            return datetime.date.fromisoformat(value)
        return super(DateField, self).parse(value)


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
