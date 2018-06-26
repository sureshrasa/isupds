#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#

from enum import IntEnum, unique

@unique
class RedirectionIndicator(IntEnum):
    NoRedirection = 0
    CallRerouted = 1
    CallReroutedAllInformationPresentationRestricted = 2
    CallDiverted = 3
    CallDivertedPresentationRestricted = 4
    CallReroutedRedirectionNumberPresentationRestricted = 5
    CallDiversiondRedirectionNumberPresentationRestricted = 6
    UNRECOGNISED = 0xFFFF

class RedirectionIndicatorDict:
    _dict = {
    0 : RedirectionIndicator.NoRedirection,
    1 : RedirectionIndicator.CallRerouted,
    2 : RedirectionIndicator.CallReroutedAllInformationPresentationRestricted,
    3 : RedirectionIndicator.CallDiverted,
    4 : RedirectionIndicator.CallDivertedPresentationRestricted,
    5 : RedirectionIndicator.CallReroutedRedirectionNumberPresentationRestricted,
    6 : RedirectionIndicator.CallDiversiondRedirectionNumberPresentationRestricted    }

    @staticmethod
    def lookup(ordinal):
        return RedirectionIndicatorDict._dict.get(ordinal, ordinal)