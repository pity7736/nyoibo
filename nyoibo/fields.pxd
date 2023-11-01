
cdef class Field:
    cdef readonly default_value
    cdef readonly private
    cdef readonly mutable
    cdef readonly choices
    cdef readonly alias
    cdef bint required
    cdef str name
    cdef model
    cpdef public parse(self, value)
    cdef _parse(self, value)


cdef class StrField(Field):
    cdef int max_length


cdef class IntField(Field):
    cdef min_value
    cdef max_value


cdef class LinkField(Field):
    cdef readonly to


cdef class TupleField(Field):
    cdef readonly of
    cdef readonly reverse_relationship


cdef class DateField(Field):
    cdef readonly _formats


cdef class DatetimeField(Field):
    cdef readonly _formats
