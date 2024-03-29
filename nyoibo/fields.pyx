import datetime
import json
from decimal import Decimal, InvalidOperation
from typing import Iterable

from nyoibo.entities.meta_entity import MetaEntity
from nyoibo.exceptions import FieldValueError, RequiredValueError, \
    StrLengthError, IntMinValueError, IntMaxValueError


cdef class Field:
    """Base Field

    This is the base for all field types.

    Attributes:
        _internal_type: each ``Field`` subclass must to override this attribute
            with the internal type that field represent.
        _exceptions (tuple): possible exception that could be raised when
            field tries to cast to ``_internal_type``.

    Args:
        private (bool): set if field is private or not. When ``private=True``
            getter and setters will not be created. ``False`` by default.
        mutable (bool): set if field is mutable or not. When ``mutable=False``
            setter will not be created. ``False`` by default.
        default_value (any): default value to field.
        choices (Enum): value to this field must be a Enum key or Enum value.
        required (bool): validate if value is not None. ``False`` by default.
    """

    _internal_type = None
    _exceptions = (TypeError, ValueError)

    def __init__(self, private=False, mutable=False, default_value=None,
                 choices=None, required=False, alias=None):
        self.default_value = default_value
        self.private = private
        self.mutable = mutable
        self.choices = choices
        self.required = required
        self.alias = alias
        self.name = ''
        self.model = None

    def __set_name__(self, owner, name):
        self.name = name.replace('_', '', 1)
        self.model = owner

    cpdef public parse(self, value):
        """Parse and cast to ``_internal_type``

        Args:
            value (any): value to parse.

        Returns:
            ``_internal_type`` if the casting was successful

        Raises:
            FieldValueError: if the casting failed.
            RequiredValueError: if a field has required = True and value is None
        """
        try:
            value = self._parse(value)
            if value and self.choices:
                return self.choices(value)
            if isinstance(value, self._internal_type):
                return value
            if value is None:
                if self.required is True:
                    raise RequiredValueError(
                        f'missing required value for <{self.name}> field in model <{self.model.__name__}>'
                    )
                return value
            return self._internal_type(value)
        except self._exceptions:
            raise FieldValueError(f'{type(value)} is not a valid value for '
                                  f'{self.__class__.__name__}')

    cdef _parse(self, value):
        """This method is to be overriding if some Field need do some checks or
            validations before ``parse`` is executed.

        Args:
            value (any): value to parse

        Returns:
            ``_internal_type`` if the casting was successful

        Raises:
            FieldValueError: if the casting failed.

        """
        return value


cdef class StrField(Field):
    """Field for string values

    Args:
        max_length (int): maximum lenght for str value

    Raises:
        AssertionError: if ``max_length`` is less than 0.
    """

    _internal_type = str

    def __init__(self, int max_length=0, *args, **kwargs):
        assert max_length >= 0, 'max_length must to be >= 0'
        self.max_length = max_length
        super().__init__(*args, **kwargs)

    cdef _parse(self, value):
        """
        Parse and cast to str

        Args:
            value (any): value to cas

        Returns:
            (str): casted value

        Raises:
            StrLengthError: if ``max_length`` was set and ``len(value)`` is greater than ``max_length``.
        """
        if self.max_length and len(value) > self.max_length:
            raise StrLengthError(f'length value ({len(value)}) is greater than max_value ({self.max_length})')
        return value


cdef class IntField(Field):
    """Field for integer values

    Args:
        min_value (int): minimum value
        max_value (int): maximum value

    Raises:
        AssertionError: if ``min_value`` or ``max_value`` are no integer.
    """

    _internal_type = int

    def __init__(self, min_value=None, max_value=None, *args, **kwargs):
        assert min_value is None or isinstance(min_value, int), 'min_value must be an integer'
        assert max_value is None or isinstance(max_value, int), 'max_value must be an integer'
        self.min_value = min_value
        self.max_value = max_value
        super().__init__(*args, **kwargs)

    cpdef public parse(self, value):
        """Parse and cast to integers

        Args:
            value(any): value to cast

        Returns:
            (int) casted value

        Raises:
            IntMinValueError: if ``min_value`` was set and ``value`` is less than ``min_value``.
            IntMaxValueError: if ``max_value`` was set and ``value`` is greater than ``max_value``.

        """
        value = super(IntField, self).parse(value)
        if self.min_value is not None and value < self.min_value:
            raise IntMinValueError(f'value ({value}) must be >= min_value ({self.min_value})')
        if self.max_value is not None and value > self.max_value:
            raise IntMaxValueError(f'value ({value}) must be <= max_value ({self.max_value})')
        return value

    cdef _parse(self, value):
        if isinstance(value, str):
            value = float(value)
        return value


cdef class BoolField(Field):
    """Field for boolean values
    """

    _internal_type = bool

    cdef _parse(self, value):
        if value in ('false', 'False'):
            return False
        return value


cdef class DateField(Field):
    """Field for ``datetime.date`` values

    Values could be ``datetime.date`` or isoformat string.

    Args:
        formats(iterable): string formats  following `strptime format codes
        <https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes>`_

    """

    _internal_type = datetime.date

    def __init__(self, formats: Iterable[str, ...] = (), **kwargs):
        super().__init__(**kwargs)
        self._formats = formats

    cdef _parse(self, value):
        if isinstance(value, str):
            for str_format in self._formats:
                try:
                    return datetime.datetime.strptime(value, str_format).date()
                except ValueError:
                    continue
            return datetime.date.fromisoformat(value)
        elif isinstance(value, datetime.datetime):
            value = value.date()
        return value


cdef class DatetimeField(Field):
    """Field for datetime.datetime values

    Values could be datetime.datetime or isoformat string.

    Args:
        formats(iterable): string formats  following `strptime format codes
        <https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes>`_

    """

    _internal_type = datetime.datetime

    def __init__(self, formats: Iterable[str, ...] = (), **kwargs):
        super().__init__(**kwargs)
        self._formats = formats

    cdef _parse(self, value):
        if isinstance(value, str):
            for str_format in self._formats:
                try:
                    return datetime.datetime.strptime(value, str_format)
                except ValueError:
                    continue
            return datetime.datetime.fromisoformat(value)
        return value


cdef class FloatField(Field):
    """Field for float values
    """

    _internal_type = float


cdef class DecimalField(Field):
    """Field for Decimal values
    """

    _internal_type = Decimal
    _exceptions = (TypeError, InvalidOperation)


cdef class LinkField(Field):
    """Field for link between other ``Entity``

    Args:
        to (Entity): Entity instance

    Raises:
        ValueError: if ``to`` is not a subclass of :ref:``entity``
    """

    def __init__(self, to, *args, **kwargs):
        if issubclass(type(to), MetaEntity) is False:
            raise ValueError('to must be an Entity subclass')
        super(LinkField, self).__init__(*args, **kwargs)
        self.to = to

    cpdef public parse(self, value):
        if isinstance(value, self.to):
            return value
        if value is None:
            if self.required is True:
                raise RequiredValueError('value is required')
            return value
        if isinstance(value, dict):
            if value:
                return self.to(**value)
            return None
        raise FieldValueError(f'{type(value)} is not a valid value for '
                              f'{self.__class__.__name__}')


cdef class DictField(Field):
    """Field for dict values
    """

    _internal_type = dict


cdef class JSONField(Field):
    """Field for json values.
    """

    _internal_type = str

    cdef _parse(self, value):
        try:
            return json.dumps(value)
        except self._exceptions:
            raise FieldValueError(f'data {value} is not serializable')


cdef class TupleField(Field):
    """
    Field for tuple values

    Args:
        of: Type of items. All items going to be cast to ``of`` type.
        reverse_relationship (bool): create a reverse relation with ``of``.

    Raises:
        ValueError: if of is ``None`` and ``reverse_relationship`` is True
    """

    _internal_type = tuple

    def __init__(self, of=None, reverse_relationship=False, *args, **kwargs):
        if reverse_relationship and of is None:
            raise ValueError('to make a reverse relationship, `of` parameter must to be set')
        super().__init__(*args, **kwargs)
        self.of = of
        self.reverse_relationship = reverse_relationship

    cdef _parse(self, value):
        if value and self.of:
            items = []
            for item in value:
                if isinstance(item, self.of):
                    items.append(item)
                    continue
                if isinstance(item, dict):
                    items.append(self.of(**item))
                else:
                    try:
                        items.append(self.of(item))
                    except self._exceptions:
                        raise FieldValueError(f"type {type(item)} of {item} value is not a valid type of {self.of}")
            value = items
        return value


cdef class ListField(TupleField):
    """
    Field for list values

    Args:
        of: Type of items. All items going to be cast to ``of`` type.
                reverse_relationship (bool): create a reverse relation with ``of``.

    Raises:
        ValueError: if of is ``None`` and ``reverse_relationship`` is True
    """

    _internal_type = list
