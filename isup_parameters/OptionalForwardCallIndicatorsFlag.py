#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#

from enum import IntEnum, unique

@unique
class OptionalForwardCallIndicatorsFlag(IntEnum):
    SimpleSegmentationIndicator = 0
    ConnectedLineIdentityRequestIndicator = 1
    UNRECOGNISED = 0xFFFF

class OptionalForwardCallIndicatorsFlagDict:
    _dict = {
    0 : OptionalForwardCallIndicatorsFlag.SimpleSegmentationIndicator,
    1 : OptionalForwardCallIndicatorsFlag.ConnectedLineIdentityRequestIndicator    }

    @staticmethod
    def lookup(ordinal):
        return OptionalForwardCallIndicatorsFlagDict._dict.get(ordinal, ordinal)