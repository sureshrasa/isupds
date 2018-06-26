#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#
from isup_parameters.CongestionLevel import *
class AutomaticCongestionLevelParameter:
    def __init__(self, 
        congestionLevel):
        self._congestionLevel = congestionLevel

    def __str__(self):
        return ("AutomaticCongestionLevelParameter["

        + str(self.congestionLevel)      + "]")


    @staticmethod
    def getTag():
        return 0x027



    @property
    def congestionLevel(self):
        return self._congestionLevel
