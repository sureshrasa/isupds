#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#

from enum import IntEnum, unique

@unique
class MessageCompatibilityInformationFlag(IntEnum):
    TransitAtIntermediateExchange = 0
    ReleaseCall = 1
    SendNotification = 2
    DiscardMessage = 3
    PassOnNotPossible = 4
    Extension = 5
    UNRECOGNISED = 0xFFFF

class MessageCompatibilityInformationFlagDict:
    _dict = {
    0 : MessageCompatibilityInformationFlag.TransitAtIntermediateExchange,
    1 : MessageCompatibilityInformationFlag.ReleaseCall,
    2 : MessageCompatibilityInformationFlag.SendNotification,
    3 : MessageCompatibilityInformationFlag.DiscardMessage,
    4 : MessageCompatibilityInformationFlag.PassOnNotPossible,
    5 : MessageCompatibilityInformationFlag.Extension    }

    @staticmethod
    def lookup(ordinal):
        return MessageCompatibilityInformationFlagDict._dict.get(ordinal, ordinal)