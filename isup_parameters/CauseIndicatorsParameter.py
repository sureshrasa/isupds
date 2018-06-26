#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#
from isup_parameters.Location import *
from isup_parameters.CodingStandard import *


class CauseIndicatorsParameter:
    def __init__(self, 
        location,
        codingStandard,
        cause,
        diagnostics):
        self._location = location
        self._codingStandard = codingStandard
        self._cause = cause
        self._diagnostics = diagnostics

    def __str__(self):
        return ("CauseIndicatorsParameter["

        + str(self.location)      + ","
        + str(self.codingStandard)      + ","
        + str(self.cause)      + ","
        + "<" + ",".join(map(str, self.diagnostics)) + ">"      + "]")


    @staticmethod
    def getTag():
        return 0x012



    @property
    def location(self):
        return self._location



    @property
    def codingStandard(self):
        return self._codingStandard



    @property
    def cause(self):
        return self._cause



    @property
    def diagnostics(self):
        return self._diagnostics
