#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#

from enum import IntEnum, unique

@unique
class CalledPartysStatusIndicator(IntEnum):
    NoIndication = 0
    SubscriberFree = 1
    ConnectWhenFree = 2
    Spare = 3
    UNRECOGNISED = 0xFFFF

class CalledPartysStatusIndicatorDict:
    _dict = {
    0 : CalledPartysStatusIndicator.NoIndication,
    1 : CalledPartysStatusIndicator.SubscriberFree,
    2 : CalledPartysStatusIndicator.ConnectWhenFree,
    3 : CalledPartysStatusIndicator.Spare    }

    @staticmethod
    def lookup(ordinal):
        return CalledPartysStatusIndicatorDict._dict.get(ordinal, ordinal)