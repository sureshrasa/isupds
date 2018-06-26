#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#
from isup_parameters.OptionalBackwardCallIndicatorsFlag import *
class OptionalBackwardCallIndicatorsParameter:
    def __init__(self, flags
):
        self._flags = flags

    def __str__(self):
        return ("OptionalBackwardCallIndicatorsParameter["
        + str(self.flags)      + "]")


    @staticmethod
    def getTag():
        return 0x029

    @property
    def flags(self):
        return self._flags

