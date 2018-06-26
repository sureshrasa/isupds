#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#

from enum import IntEnum, unique

@unique
class OriginalRedirectionReason(IntEnum):
    Unknown = 0
    UserBusy = 1
    NoReply = 2
    Unconditional = 3
    UNRECOGNISED = 0xFFFF

class OriginalRedirectionReasonDict:
    _dict = {
    0 : OriginalRedirectionReason.Unknown,
    1 : OriginalRedirectionReason.UserBusy,
    2 : OriginalRedirectionReason.NoReply,
    3 : OriginalRedirectionReason.Unconditional    }

    @staticmethod
    def lookup(ordinal):
        return OriginalRedirectionReasonDict._dict.get(ordinal, ordinal)