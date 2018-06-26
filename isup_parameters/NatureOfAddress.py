#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#

from enum import IntEnum, unique

@unique
class NatureOfAddress(IntEnum):
    National = 3
    International = 4
    UkSpecific = 126
    UNRECOGNISED = 0xFFFF

class NatureOfAddressDict:
    _dict = {
    3 : NatureOfAddress.National,
    4 : NatureOfAddress.International,
    126 : NatureOfAddress.UkSpecific    }

    @staticmethod
    def lookup(ordinal):
        return NatureOfAddressDict._dict.get(ordinal, ordinal)