#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#
from isup_parameters.MessageCompatibilityInformationFlag import *
from isup_parameters.BroadbandNarrowbandInterworking import *
class MessageCompatibilityInformationParameter:
    def __init__(self, flags, 
        broadbandNarrowbandInterworking):
        self._broadbandNarrowbandInterworking = broadbandNarrowbandInterworking
        self._flags = flags

    def __str__(self):
        return ("MessageCompatibilityInformationParameter["
        + str(self.flags)+ ","
        + str(self.broadbandNarrowbandInterworking)      + "]")


    @staticmethod
    def getTag():
        return 0x038

    @property
    def flags(self):
        return self._flags


    @property
    def broadbandNarrowbandInterworking(self):
        return self._broadbandNarrowbandInterworking
