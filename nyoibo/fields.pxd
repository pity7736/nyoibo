
cdef class Field:
    cdef public default_value
    cpdef public parse(self, value)


cdef class StrField(Field):
    pass


cdef class IntField(Field):
    pass
