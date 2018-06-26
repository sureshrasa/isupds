#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#

from enum import IntEnum, unique

@unique
class OriginalCalledNumberFlag(IntEnum):
    OddAddressSignals = 0
    UNRECOGNISED = 0xFFFF

class OriginalCalledNumberFlagDict:
    _dict = {
    0 : OriginalCalledNumberFlag.OddAddressSignals    }

    @staticmethod
    def lookup(ordinal):
        return OriginalCalledNumberFlagDict._dict.get(ordinal, ordinal)