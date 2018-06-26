#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#

from enum import IntEnum, unique

@unique
class TransmissionMediumRequirement(IntEnum):
    Speech = 0
    Unrestricted64kbps = 2
    Audio31kHz = 3
    UNRECOGNISED = 0xFFFF

class TransmissionMediumRequirementDict:
    _dict = {
    0 : TransmissionMediumRequirement.Speech,
    2 : TransmissionMediumRequirement.Unrestricted64kbps,
    3 : TransmissionMediumRequirement.Audio31kHz    }

    @staticmethod
    def lookup(ordinal):
        return TransmissionMediumRequirementDict._dict.get(ordinal, ordinal)