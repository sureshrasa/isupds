#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#
from isup_parameters.NationalInformationIndicatorsFlag import *
class NationalInformationIndicatorsParameter:
    def __init__(self, flags
):
        self._flags = flags

    def __str__(self):
        return ("NationalInformationIndicatorsParameter["
        + str(self.flags)      + "]")


    @staticmethod
    def getTag():
        return 0x0F5

    @property
    def flags(self):
        return self._flags

