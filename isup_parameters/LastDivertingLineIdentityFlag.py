#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#

from enum import IntEnum, unique

@unique
class LastDivertingLineIdentityFlag(IntEnum):
    OddAddressSignals = 0
    NumberIncomplete = 1
    UNRECOGNISED = 0xFFFF

class LastDivertingLineIdentityFlagDict:
    _dict = {
    0 : LastDivertingLineIdentityFlag.OddAddressSignals,
    1 : LastDivertingLineIdentityFlag.NumberIncomplete    }

    @staticmethod
    def lookup(ordinal):
        return LastDivertingLineIdentityFlagDict._dict.get(ordinal, ordinal)