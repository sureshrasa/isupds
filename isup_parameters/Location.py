#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#

from enum import IntEnum, unique

@unique
class Location(IntEnum):
    User = 0
    PrivateNetworkServingLocalUser = 1
    PublicNetworkServingLocalUser = 2
    TransitNetwork = 3
    PublicNetworkServingRemoteUser = 4
    PrivateNetworkServingRemoteUser = 5
    InternationalNetwork = 7
    NetworkBeyondInterworkingPoint = 10
    UNRECOGNISED = 0xFFFF

class LocationDict:
    _dict = {
    0 : Location.User,
    1 : Location.PrivateNetworkServingLocalUser,
    2 : Location.PublicNetworkServingLocalUser,
    3 : Location.TransitNetwork,
    4 : Location.PublicNetworkServingRemoteUser,
    5 : Location.PrivateNetworkServingRemoteUser,
    7 : Location.InternationalNetwork,
    10 : Location.NetworkBeyondInterworkingPoint    }

    @staticmethod
    def lookup(ordinal):
        return LocationDict._dict.get(ordinal, ordinal)