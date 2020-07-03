from jedi.inference.gradual.annotation import py__annotations__

from .meta_entity import MetaEntity


class Entity(metaclass=MetaEntity):

    def __init__(self, value=None):
        self._value = value
