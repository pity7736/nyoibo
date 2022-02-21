
cdef class Field:
    cdef readonly default_value
    cdef readonly private
    cdef readonly mutable
    cdef readonly choices
    cdef bint required
    cpdef public parse(self, value)
    cdef _parse(self, value)


cdef class StrField(Field):
    cdef int max_length

cdef class LinkField(Field):
    cdef readonly to
