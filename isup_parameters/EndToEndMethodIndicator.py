#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#

from enum import IntEnum, unique

@unique
class EndToEndMethodIndicator(IntEnum):
    NoEndToEndMethodAvailable = 0
    PassAlongMethodAvailable = 1
    SccpMethodAvailable = 2
    PassAlongAndSccpMethodsAvailable = 3
    UNRECOGNISED = 0xFFFF

class EndToEndMethodIndicatorDict:
    _dict = {
    0 : EndToEndMethodIndicator.NoEndToEndMethodAvailable,
    1 : EndToEndMethodIndicator.PassAlongMethodAvailable,
    2 : EndToEndMethodIndicator.SccpMethodAvailable,
    3 : EndToEndMethodIndicator.PassAlongAndSccpMethodsAvailable    }

    @staticmethod
    def lookup(ordinal):
        return EndToEndMethodIndicatorDict._dict.get(ordinal, ordinal)