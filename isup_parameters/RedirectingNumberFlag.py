#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#

from enum import IntEnum, unique

@unique
class RedirectingNumberFlag(IntEnum):
    OddAddressSignals = 0
    UNRECOGNISED = 0xFFFF

class RedirectingNumberFlagDict:
    _dict = {
    0 : RedirectingNumberFlag.OddAddressSignals    }

    @staticmethod
    def lookup(ordinal):
        return RedirectingNumberFlagDict._dict.get(ordinal, ordinal)