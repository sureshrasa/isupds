#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#

from enum import IntEnum, unique

@unique
class BroadbandNarrowbandInterworking(IntEnum):
    PassOn = 0
    DiscardMessage = 1
    ReleaseCall = 2
    Reserved = 3
    UNRECOGNISED = 0xFFFF

class BroadbandNarrowbandInterworkingDict:
    _dict = {
    0 : BroadbandNarrowbandInterworking.PassOn,
    1 : BroadbandNarrowbandInterworking.DiscardMessage,
    2 : BroadbandNarrowbandInterworking.ReleaseCall,
    3 : BroadbandNarrowbandInterworking.Reserved    }

    @staticmethod
    def lookup(ordinal):
        return BroadbandNarrowbandInterworkingDict._dict.get(ordinal, ordinal)