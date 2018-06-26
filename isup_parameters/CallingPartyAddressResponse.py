#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#

from enum import IntEnum, unique

@unique
class CallingPartyAddressResponse(IntEnum):
    CallingPartyAddressNotIncluded = 0
    CallingPartyAddressNotAvailable = 1
    Spare = 2
    CallingPartyAddressIncluded = 3
    UNRECOGNISED = 0xFFFF

class CallingPartyAddressResponseDict:
    _dict = {
    0 : CallingPartyAddressResponse.CallingPartyAddressNotIncluded,
    1 : CallingPartyAddressResponse.CallingPartyAddressNotAvailable,
    2 : CallingPartyAddressResponse.Spare,
    3 : CallingPartyAddressResponse.CallingPartyAddressIncluded    }

    @staticmethod
    def lookup(ordinal):
        return CallingPartyAddressResponseDict._dict.get(ordinal, ordinal)