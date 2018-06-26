#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#

from enum import IntEnum, unique

@unique
class ScreeningIndicator(IntEnum):
    UserProvidedNotVerified = 0
    UserProvidedVerifiedAndPassed = 1
    NetworkProvided = 3
    UNRECOGNISED = 0xFFFF

class ScreeningIndicatorDict:
    _dict = {
    0 : ScreeningIndicator.UserProvidedNotVerified,
    1 : ScreeningIndicator.UserProvidedVerifiedAndPassed,
    3 : ScreeningIndicator.NetworkProvided    }

    @staticmethod
    def lookup(ordinal):
        return ScreeningIndicatorDict._dict.get(ordinal, ordinal)