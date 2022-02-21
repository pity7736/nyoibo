
class NyoiboError(Exception):
    pass


class PrivateFieldError(NyoiboError):
    pass


class FieldValueError(NyoiboError):
    pass


class RequiredValueError(FieldValueError):
    pass


class StrLengthError(FieldValueError):
    pass
