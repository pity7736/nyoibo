
class NyoiboError(Exception):
    pass


class PrivateField(NyoiboError):
    pass


class IntValueError(NyoiboError):
    pass


class DateValueError(NyoiboError):
    pass
