#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#
from isup_parameters.NationalForwardCallIndicatorsFlag import *
class NationalForwardCallIndicatorsParameter:
    def __init__(self, flags
):
        self._flags = flags

    def __str__(self):
        return ("NationalForwardCallIndicatorsParameter["
        + str(self.flags)      + "]")


    @staticmethod
    def getTag():
        return 0x0FE

    @property
    def flags(self):
        return self._flags

