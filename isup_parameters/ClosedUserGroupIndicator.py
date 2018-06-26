#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#

from enum import IntEnum, unique

@unique
class ClosedUserGroupIndicator(IntEnum):
    NonClosedUserGroupCall = 0
    Spare = 1
    OutgoingAccessAllowed = 2
    OutgoingAccessNotAllowed = 3
    UNRECOGNISED = 0xFFFF

class ClosedUserGroupIndicatorDict:
    _dict = {
    0 : ClosedUserGroupIndicator.NonClosedUserGroupCall,
    1 : ClosedUserGroupIndicator.Spare,
    2 : ClosedUserGroupIndicator.OutgoingAccessAllowed,
    3 : ClosedUserGroupIndicator.OutgoingAccessNotAllowed    }

    @staticmethod
    def lookup(ordinal):
        return ClosedUserGroupIndicatorDict._dict.get(ordinal, ordinal)