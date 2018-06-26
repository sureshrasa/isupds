#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#
from isup_parameters.CalledSubscriberBasicServiceMarksFlag import *
class CalledSubscriberBasicServiceMarksParameter:
    def __init__(self, flags, 
        tariffGroup):
        self._tariffGroup = tariffGroup
        self._flags = flags

    def __str__(self):
        return ("CalledSubscriberBasicServiceMarksParameter["
        + str(self.flags)+ ","
        + str(self.tariffGroup)      + "]")


    @staticmethod
    def getTag():
        return 0x0FA

    @property
    def flags(self):
        return self._flags


    @property
    def tariffGroup(self):
        return self._tariffGroup
