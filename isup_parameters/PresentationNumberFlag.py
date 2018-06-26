#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#

from enum import IntEnum, unique

@unique
class PresentationNumberFlag(IntEnum):
    OddAddressSignals = 0
    PresentationNumberPreferred = 1
    UNRECOGNISED = 0xFFFF

class PresentationNumberFlagDict:
    _dict = {
    0 : PresentationNumberFlag.OddAddressSignals,
    1 : PresentationNumberFlag.PresentationNumberPreferred    }

    @staticmethod
    def lookup(ordinal):
        return PresentationNumberFlagDict._dict.get(ordinal, ordinal)