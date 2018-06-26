#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#

from enum import IntEnum, unique

@unique
class CodingStandard(IntEnum):
    ITU_T = 0
    ISO_IEC = 1
    National = 2
    SpecificToIdentifiedLocation = 3
    UNRECOGNISED = 0xFFFF

class CodingStandardDict:
    _dict = {
    0 : CodingStandard.ITU_T,
    1 : CodingStandard.ISO_IEC,
    2 : CodingStandard.National,
    3 : CodingStandard.SpecificToIdentifiedLocation    }

    @staticmethod
    def lookup(ordinal):
        return CodingStandardDict._dict.get(ordinal, ordinal)