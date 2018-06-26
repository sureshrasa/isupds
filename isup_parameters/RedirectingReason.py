#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#

from enum import IntEnum, unique

@unique
class RedirectingReason(IntEnum):
    Unknown = 0
    UserBusy = 1
    NoReply = 2
    Unconditional = 3
    UNRECOGNISED = 0xFFFF

class RedirectingReasonDict:
    _dict = {
    0 : RedirectingReason.Unknown,
    1 : RedirectingReason.UserBusy,
    2 : RedirectingReason.NoReply,
    3 : RedirectingReason.Unconditional    }

    @staticmethod
    def lookup(ordinal):
        return RedirectingReasonDict._dict.get(ordinal, ordinal)