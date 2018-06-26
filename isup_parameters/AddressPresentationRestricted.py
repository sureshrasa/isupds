#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#

from enum import IntEnum, unique

@unique
class AddressPresentationRestricted(IntEnum):
    Allowed = 0
    Restricted = 1
    NotAvailable = 2
    RestrictedByNetwork = 3
    UNRECOGNISED = 0xFFFF

class AddressPresentationRestrictedDict:
    _dict = {
    0 : AddressPresentationRestricted.Allowed,
    1 : AddressPresentationRestricted.Restricted,
    2 : AddressPresentationRestricted.NotAvailable,
    3 : AddressPresentationRestricted.RestrictedByNetwork    }

    @staticmethod
    def lookup(ordinal):
        return AddressPresentationRestrictedDict._dict.get(ordinal, ordinal)