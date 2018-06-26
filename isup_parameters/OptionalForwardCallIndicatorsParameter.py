#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#
from isup_parameters.OptionalForwardCallIndicatorsFlag import *
from isup_parameters.ClosedUserGroupIndicator import *
class OptionalForwardCallIndicatorsParameter:
    def __init__(self, flags, 
        closedUserGroupIndicator):
        self._closedUserGroupIndicator = closedUserGroupIndicator
        self._flags = flags

    def __str__(self):
        return ("OptionalForwardCallIndicatorsParameter["
        + str(self.flags)+ ","
        + str(self.closedUserGroupIndicator)      + "]")


    @staticmethod
    def getTag():
        return 0x08

    @property
    def flags(self):
        return self._flags


    @property
    def closedUserGroupIndicator(self):
        return self._closedUserGroupIndicator
