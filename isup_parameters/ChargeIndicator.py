#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#

from enum import IntEnum, unique

@unique
class ChargeIndicator(IntEnum):
    NoIndication = 0
    NoCharge = 1
    Charge = 2
    Spare = 3
    UNRECOGNISED = 0xFFFF

class ChargeIndicatorDict:
    _dict = {
    0 : ChargeIndicator.NoIndication,
    1 : ChargeIndicator.NoCharge,
    2 : ChargeIndicator.Charge,
    3 : ChargeIndicator.Spare    }

    @staticmethod
    def lookup(ordinal):
        return ChargeIndicatorDict._dict.get(ordinal, ordinal)