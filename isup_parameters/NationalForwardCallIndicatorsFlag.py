#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#

from enum import IntEnum, unique

@unique
class NationalForwardCallIndicatorsFlag(IntEnum):
    CliBlocking = 0
    NetworkTranslatedAddress = 1
    PriorityAccess = 2
    Protection = 3
    UNRECOGNISED = 0xFFFF

class NationalForwardCallIndicatorsFlagDict:
    _dict = {
    0 : NationalForwardCallIndicatorsFlag.CliBlocking,
    1 : NationalForwardCallIndicatorsFlag.NetworkTranslatedAddress,
    2 : NationalForwardCallIndicatorsFlag.PriorityAccess,
    3 : NationalForwardCallIndicatorsFlag.Protection    }

    @staticmethod
    def lookup(ordinal):
        return NationalForwardCallIndicatorsFlagDict._dict.get(ordinal, ordinal)