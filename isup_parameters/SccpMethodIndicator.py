#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#

from enum import IntEnum, unique

@unique
class SccpMethodIndicator(IntEnum):
    NoIndication = 0
    ConnectionlessMethodAvailable = 1
    ConnectionOrientedMethodAvailable = 2
    ConnectionlessAndConnectionOrientedMethodsAvailable = 3
    UNRECOGNISED = 0xFFFF

class SccpMethodIndicatorDict:
    _dict = {
    0 : SccpMethodIndicator.NoIndication,
    1 : SccpMethodIndicator.ConnectionlessMethodAvailable,
    2 : SccpMethodIndicator.ConnectionOrientedMethodAvailable,
    3 : SccpMethodIndicator.ConnectionlessAndConnectionOrientedMethodsAvailable    }

    @staticmethod
    def lookup(ordinal):
        return SccpMethodIndicatorDict._dict.get(ordinal, ordinal)