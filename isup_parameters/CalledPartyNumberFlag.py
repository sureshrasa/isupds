#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#

from enum import IntEnum, unique

@unique
class CalledPartyNumberFlag(IntEnum):
    OddAddressSignals = 0
    InternalNetworkNumberIndicator = 1
    UNRECOGNISED = 0xFFFF

class CalledPartyNumberFlagDict:
    _dict = {
    0 : CalledPartyNumberFlag.OddAddressSignals,
    1 : CalledPartyNumberFlag.InternalNetworkNumberIndicator    }

    @staticmethod
    def lookup(ordinal):
        return CalledPartyNumberFlagDict._dict.get(ordinal, ordinal)