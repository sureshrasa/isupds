#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#

from enum import IntEnum, unique

@unique
class IsdnUserPartPreferenceIndicator(IntEnum):
    IsdnUserPartPreferredAllTheWay = 0
    IsdnUserPartNotRequiredAllTheWay = 1
    IsdnUserPartRequiredAllTheWay = 2
    UNRECOGNISED = 0xFFFF

class IsdnUserPartPreferenceIndicatorDict:
    _dict = {
    0 : IsdnUserPartPreferenceIndicator.IsdnUserPartPreferredAllTheWay,
    1 : IsdnUserPartPreferenceIndicator.IsdnUserPartNotRequiredAllTheWay,
    2 : IsdnUserPartPreferenceIndicator.IsdnUserPartRequiredAllTheWay    }

    @staticmethod
    def lookup(ordinal):
        return IsdnUserPartPreferenceIndicatorDict._dict.get(ordinal, ordinal)