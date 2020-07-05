
cdef class Field:
    cpdef public parse(self, value)


cdef class StrField(Field):
    pass


cdef class IntField(Field):
    pass
