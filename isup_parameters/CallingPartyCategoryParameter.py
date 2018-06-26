#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#
from isup_parameters.CallingPartyCategory import *
class CallingPartyCategoryParameter:
    def __init__(self, 
        callingPartyCategory):
        self._callingPartyCategory = callingPartyCategory

    def __str__(self):
        return ("CallingPartyCategoryParameter["

        + str(self.callingPartyCategory)      + "]")


    @staticmethod
    def getTag():
        return 0x09



    @property
    def callingPartyCategory(self):
        return self._callingPartyCategory
