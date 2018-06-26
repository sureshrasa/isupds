#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#

from enum import IntEnum, unique

@unique
class NationalInformationIndicatorsFlag(IntEnum):
    CallingSubscribersBasicServiceMarksResponse = 0
    CalledSubscribersBasicServiceMarksResponse = 1
    CallingSubscribersOriginatingFacilityMarksResponse = 2
    CalledSubscribersTerminatingFacilityMarksResponse = 3
    InterceptedLineIdentityResponse = 4
    InterceptedLineIdentityAndCalledSubscribersBasicServiceMarksResponse = 5
    UNRECOGNISED = 0xFFFF

class NationalInformationIndicatorsFlagDict:
    _dict = {
    0 : NationalInformationIndicatorsFlag.CallingSubscribersBasicServiceMarksResponse,
    1 : NationalInformationIndicatorsFlag.CalledSubscribersBasicServiceMarksResponse,
    2 : NationalInformationIndicatorsFlag.CallingSubscribersOriginatingFacilityMarksResponse,
    3 : NationalInformationIndicatorsFlag.CalledSubscribersTerminatingFacilityMarksResponse,
    4 : NationalInformationIndicatorsFlag.InterceptedLineIdentityResponse,
    5 : NationalInformationIndicatorsFlag.InterceptedLineIdentityAndCalledSubscribersBasicServiceMarksResponse    }

    @staticmethod
    def lookup(ordinal):
        return NationalInformationIndicatorsFlagDict._dict.get(ordinal, ordinal)