#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#

from enum import IntEnum, unique

@unique
class GenericNumberFlag(IntEnum):
    OddAddressSignals = 0
    NumberIncomplete = 1
    UNRECOGNISED = 0xFFFF

class GenericNumberFlagDict:
    _dict = {
    0 : GenericNumberFlag.OddAddressSignals,
    1 : GenericNumberFlag.NumberIncomplete    }

    @staticmethod
    def lookup(ordinal):
        return GenericNumberFlagDict._dict.get(ordinal, ordinal)