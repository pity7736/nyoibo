from typing import Dict, Any

from nyoibo.exceptions import PrivateField
from nyoibo.fields import StrField


class MetaEntity(type):

    def __new__(mcs, name, bases, namespace: Dict[str, Any]):
        for attr, value in namespace.items():
            if isinstance(value, StrField):
                if not attr.startswith('_'):
                    raise PrivateField('Fields must be private')

        return super().__new__(mcs, name, bases, namespace)
