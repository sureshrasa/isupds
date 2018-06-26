#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#

from enum import IntEnum, unique

@unique
class CalledPartysCategoryIndicator(IntEnum):
    NoIndication = 0
    OrdinarySubscriber = 1
    PayPhone = 2
    Spare = 3
    UNRECOGNISED = 0xFFFF

class CalledPartysCategoryIndicatorDict:
    _dict = {
    0 : CalledPartysCategoryIndicator.NoIndication,
    1 : CalledPartysCategoryIndicator.OrdinarySubscriber,
    2 : CalledPartysCategoryIndicator.PayPhone,
    3 : CalledPartysCategoryIndicator.Spare    }

    @staticmethod
    def lookup(ordinal):
        return CalledPartysCategoryIndicatorDict._dict.get(ordinal, ordinal)