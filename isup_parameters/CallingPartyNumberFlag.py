#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#

from enum import IntEnum, unique

@unique
class CallingPartyNumberFlag(IntEnum):
    OddAddressSignals = 0
    NumberIncomplete = 1
    UNRECOGNISED = 0xFFFF

class CallingPartyNumberFlagDict:
    _dict = {
    0 : CallingPartyNumberFlag.OddAddressSignals,
    1 : CallingPartyNumberFlag.NumberIncomplete    }

    @staticmethod
    def lookup(ordinal):
        return CallingPartyNumberFlagDict._dict.get(ordinal, ordinal)