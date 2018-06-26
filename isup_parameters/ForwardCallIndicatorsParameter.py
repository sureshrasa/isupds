#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#
from isup_parameters.ForwardCallIndicatorsFlag import *
from isup_parameters.IsdnUserPartPreferenceIndicator import *
class ForwardCallIndicatorsParameter:
    def __init__(self, flags, 
        isdnUserPartPreferenceIndicator):
        self._isdnUserPartPreferenceIndicator = isdnUserPartPreferenceIndicator
        self._flags = flags

    def __str__(self):
        return ("ForwardCallIndicatorsParameter["
        + str(self.flags)+ ","
        + str(self.isdnUserPartPreferenceIndicator)      + "]")


    @staticmethod
    def getTag():
        return 0x07

    @property
    def flags(self):
        return self._flags


    @property
    def isdnUserPartPreferenceIndicator(self):
        return self._isdnUserPartPreferenceIndicator
