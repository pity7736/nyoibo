
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
