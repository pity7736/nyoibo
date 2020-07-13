
cdef class Field:
    cdef readonly default_value
    cdef readonly private
    cpdef public parse(self, value)


cdef class StrField(Field):
    pass


cdef class IntField(Field):
    pass
