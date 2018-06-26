#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#
class HopCounterParameter:
    def __init__(self, 
        hopCounter):
        self._hopCounter = hopCounter

    def __str__(self):
        return ("HopCounterParameter["

        + str(self.hopCounter)      + "]")


    @staticmethod
    def getTag():
        return 0x03D



    @property
    def hopCounter(self):
        return self._hopCounter
