
cdef class Field:
    cdef readonly default_value
    cdef readonly private
    cdef readonly immutable
    cpdef public parse(self, value)
