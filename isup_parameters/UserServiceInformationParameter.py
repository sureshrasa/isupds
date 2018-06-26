#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#
class UserServiceInformationParameter:
    def __init__(self, 
        octets):
        self._octets = octets

    def __str__(self):
        return ("UserServiceInformationParameter["

        + "<" + ",".join(map(str, self.octets)) + ">"      + "]")


    @staticmethod
    def getTag():
        return 0x01D



    @property
    def octets(self):
        return self._octets
