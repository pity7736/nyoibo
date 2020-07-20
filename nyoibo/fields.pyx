import datetime
from decimal import Decimal

from nyoibo.exceptions import IntValueError, DateValueError

cdef class Field:

    _internal_type = None
    _value_exception = Exception

    def __init__(self, default_value=None, private=False, immutable=True,
                 choices=None):
        self.default_value = default_value
        self.private = private
        self.immutable = immutable
        self.choices = choices

    cpdef public parse(self, value):
        if value and self.choices:
            return self.choices(value)

        if value is None or type(value) is self._internal_type:
            return value
        return self._internal_type(value)


cdef class StrField(Field):

    _internal_type = str


cdef class IntField(Field):

    _internal_type = int
    _value_exception = IntValueError

    cpdef public parse(self, value):
        # I implemented super in python 2 form because cython
        # has an issue with super without arguments
        # https://github.com/cython/cython/issues/3726
        try:
            if isinstance(value, str):
                value = float(value)
            result = super(IntField, self).parse(value)
        except (TypeError, ValueError):
            raise IntValueError(f'{type(value)} is not a valid value for '
                                'IntField')
        return result


cdef class BoolField(Field):

    _internal_type = bool

    cpdef public parse(self, value):
        if value in ('false', 'False'):
            return False
        return super(BoolField, self).parse(value)


cdef class DateField(Field):

    _internal_type = datetime.date

    cpdef public parse(self, value):
        try:
            if isinstance(value, str):
                return datetime.date.fromisoformat(value)
            result = super(DateField, self).parse(value)
        except (TypeError, ValueError):
            raise DateValueError(f'{type(value)} is not a valid value for '
                                 'DateField')
        return result


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
