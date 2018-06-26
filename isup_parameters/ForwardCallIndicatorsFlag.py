#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#

from enum import IntEnum, unique

@unique
class ForwardCallIndicatorsFlag(IntEnum):
    InternationalCall = 0
    InterworkingEncountered = 1
    EndToEndInformationAvailable = 2
    IsdnUserPartUsedAllTheWay = 3
    OriginatingAccessIsdn = 4
    UNRECOGNISED = 0xFFFF

class ForwardCallIndicatorsFlagDict:
    _dict = {
    0 : ForwardCallIndicatorsFlag.InternationalCall,
    1 : ForwardCallIndicatorsFlag.InterworkingEncountered,
    2 : ForwardCallIndicatorsFlag.EndToEndInformationAvailable,
    3 : ForwardCallIndicatorsFlag.IsdnUserPartUsedAllTheWay,
    4 : ForwardCallIndicatorsFlag.OriginatingAccessIsdn    }

    @staticmethod
    def lookup(ordinal):
        return ForwardCallIndicatorsFlagDict._dict.get(ordinal, ordinal)