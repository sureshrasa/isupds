#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#
from isup_parameters.GenericNumberFlag import *
from isup_parameters.NumberQualifier import *
from isup_parameters.NatureOfAddress import *
from isup_parameters.ScreeningIndicator import *
from isup_parameters.AddressPresentationRestricted import *

class GenericNumberParameter:
    def __init__(self, flags, 
        numberQualifier,
        natureOfAddress,
        screeningIndicator,
        addressPresentationRestricted,
        addressSignals):
        self._numberQualifier = numberQualifier
        self._natureOfAddress = natureOfAddress
        self._screeningIndicator = screeningIndicator
        self._addressPresentationRestricted = addressPresentationRestricted
        self._addressSignals = addressSignals
        self._flags = flags

    def __str__(self):
        return ("GenericNumberParameter["
        + str(self.flags)+ ","
        + str(self.numberQualifier)      + ","
        + str(self.natureOfAddress)      + ","
        + str(self.screeningIndicator)      + ","
        + str(self.addressPresentationRestricted)      + ","
        + "<" + ",".join(map(str, self.addressSignals)) + ">"      + "]")


    @staticmethod
    def getTag():
        return 0x0C0

    @property
    def flags(self):
        return self._flags


    @property
    def numberQualifier(self):
        return self._numberQualifier



    @property
    def natureOfAddress(self):
        return self._natureOfAddress



    @property
    def screeningIndicator(self):
        return self._screeningIndicator



    @property
    def addressPresentationRestricted(self):
        return self._addressPresentationRestricted



    @property
    def addressSignals(self):
        return self._addressSignals
