#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#
from isup_parameters.InformationIndicatorsFlag import *
from isup_parameters.CallingPartyAddressResponse import *
class InformationIndicatorsParameter:
    def __init__(self, flags, 
        callingPartyAddressResponse):
        self._callingPartyAddressResponse = callingPartyAddressResponse
        self._flags = flags

    def __str__(self):
        return ("InformationIndicatorsParameter["
        + str(self.flags)+ ","
        + str(self.callingPartyAddressResponse)      + "]")


    @staticmethod
    def getTag():
        return 0x0F

    @property
    def flags(self):
        return self._flags


    @property
    def callingPartyAddressResponse(self):
        return self._callingPartyAddressResponse
