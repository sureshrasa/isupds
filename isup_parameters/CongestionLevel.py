#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#

from enum import IntEnum, unique

@unique
class CongestionLevel(IntEnum):
    Spare = 0
    CongestionLevel1Exceeded = 1
    CongestionLevel2Exceeded = 2
    UNRECOGNISED = 0xFFFF

class CongestionLevelDict:
    _dict = {
    0 : CongestionLevel.Spare,
    1 : CongestionLevel.CongestionLevel1Exceeded,
    2 : CongestionLevel.CongestionLevel2Exceeded    }

    @staticmethod
    def lookup(ordinal):
        return CongestionLevelDict._dict.get(ordinal, ordinal)