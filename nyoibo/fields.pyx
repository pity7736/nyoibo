
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
