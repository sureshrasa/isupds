#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#
from isup_parameters.RedirectingNumberFlag import *
from isup_parameters.NatureOfAddress import *
from isup_parameters.AddressPresentationRestricted import *

class RedirectingNumberParameter:
    def __init__(self, flags, 
        natureOfAddress,
        addressPresentationRestricted,
        addressSignals):
        self._natureOfAddress = natureOfAddress
        self._addressPresentationRestricted = addressPresentationRestricted
        self._addressSignals = addressSignals
        self._flags = flags

    def __str__(self):
        return ("RedirectingNumberParameter["
        + str(self.flags)+ ","
        + str(self.natureOfAddress)      + ","
        + str(self.addressPresentationRestricted)      + ","
        + "<" + ",".join(map(str, self.addressSignals)) + ">"      + "]")


    @staticmethod
    def getTag():
        return 0x0B

    @property
    def flags(self):
        return self._flags


    @property
    def natureOfAddress(self):
        return self._natureOfAddress



    @property
    def addressPresentationRestricted(self):
        return self._addressPresentationRestricted



    @property
    def addressSignals(self):
        return self._addressSignals
