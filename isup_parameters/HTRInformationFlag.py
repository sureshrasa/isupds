#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#

from enum import IntEnum, unique

@unique
class HTRInformationFlag(IntEnum):
    OddAddressSignals = 0
    UNRECOGNISED = 0xFFFF

class HTRInformationFlagDict:
    _dict = {
    0 : HTRInformationFlag.OddAddressSignals    }

    @staticmethod
    def lookup(ordinal):
        return HTRInformationFlagDict._dict.get(ordinal, ordinal)