#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#

from enum import IntEnum, unique

@unique
class InformationIndicatorsFlag(IntEnum):
    HoldProvided = 0
    CallingPartysCategoryResponse = 1
    ChargeInformationResponse = 2
    SolicitedInformation = 3
    UNRECOGNISED = 0xFFFF

class InformationIndicatorsFlagDict:
    _dict = {
    0 : InformationIndicatorsFlag.HoldProvided,
    1 : InformationIndicatorsFlag.CallingPartysCategoryResponse,
    2 : InformationIndicatorsFlag.ChargeInformationResponse,
    3 : InformationIndicatorsFlag.SolicitedInformation    }

    @staticmethod
    def lookup(ordinal):
        return InformationIndicatorsFlagDict._dict.get(ordinal, ordinal)