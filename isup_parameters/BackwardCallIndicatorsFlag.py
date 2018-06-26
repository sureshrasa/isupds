#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#

from enum import IntEnum, unique

@unique
class BackwardCallIndicatorsFlag(IntEnum):
    InterworkingIndicator = 0
    EndToEndInformationIndicator = 1
    IsdnUserPartIndicator = 2
    HoldingIndicator = 3
    IsdnAccessIndicator = 4
    EchoControlDeviceIndicator = 5
    UNRECOGNISED = 0xFFFF

class BackwardCallIndicatorsFlagDict:
    _dict = {
    0 : BackwardCallIndicatorsFlag.InterworkingIndicator,
    1 : BackwardCallIndicatorsFlag.EndToEndInformationIndicator,
    2 : BackwardCallIndicatorsFlag.IsdnUserPartIndicator,
    3 : BackwardCallIndicatorsFlag.HoldingIndicator,
    4 : BackwardCallIndicatorsFlag.IsdnAccessIndicator,
    5 : BackwardCallIndicatorsFlag.EchoControlDeviceIndicator    }

    @staticmethod
    def lookup(ordinal):
        return BackwardCallIndicatorsFlagDict._dict.get(ordinal, ordinal)