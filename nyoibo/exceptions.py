
class NyoiboError(Exception):
    pass


class PrivateField(NyoiboError):
    pass


class FieldValueError(NyoiboError):
    pass
