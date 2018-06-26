#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: � Resilientplc.com Ltd. 2018 - All Rights Reserved
#
from isup_parameters.HTRInformationFlag import *
from isup_parameters.NatureOfAddress import *

class HTRInformationParameter:
    def __init__(self, flags, 
        natureOfAddress,
        addressSignals):
        self._natureOfAddress = natureOfAddress
        self._addressSignals = addressSignals
        self._flags = flags

    def __str__(self):
        return ("HTRInformationParameter["
        + str(self.flags)+ ","
        + str(self.natureOfAddress)      + ","
        + "<" + ",".join(map(str, self.addressSignals)) + ">"      + "]")


    @staticmethod
    def getTag():
        return 0x082

    @property
    def flags(self):
        return self._flags


    @property
    def natureOfAddress(self):
        return self._natureOfAddress



    @property
    def addressSignals(self):
        return self._addressSignals
