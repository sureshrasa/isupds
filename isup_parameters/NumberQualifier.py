#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#

from enum import IntEnum, unique

@unique
class NumberQualifier(IntEnum):
    AdditionalCalledNumber = 1
    UNRECOGNISED = 0xFFFF

class NumberQualifierDict:
    _dict = {
    1 : NumberQualifier.AdditionalCalledNumber    }

    @staticmethod
    def lookup(ordinal):
        return NumberQualifierDict._dict.get(ordinal, ordinal)