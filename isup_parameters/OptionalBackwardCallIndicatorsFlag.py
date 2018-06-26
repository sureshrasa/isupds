#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#

from enum import IntEnum, unique

@unique
class OptionalBackwardCallIndicatorsFlag(IntEnum):
    InbandInformationIndicator = 0
    CallDiversionMayOccurIndicator = 1
    SimpleSegmentationIndicator = 2
    MlppUserIndicator = 3
    UNRECOGNISED = 0xFFFF

class OptionalBackwardCallIndicatorsFlagDict:
    _dict = {
    0 : OptionalBackwardCallIndicatorsFlag.InbandInformationIndicator,
    1 : OptionalBackwardCallIndicatorsFlag.CallDiversionMayOccurIndicator,
    2 : OptionalBackwardCallIndicatorsFlag.SimpleSegmentationIndicator,
    3 : OptionalBackwardCallIndicatorsFlag.MlppUserIndicator    }

    @staticmethod
    def lookup(ordinal):
        return OptionalBackwardCallIndicatorsFlagDict._dict.get(ordinal, ordinal)