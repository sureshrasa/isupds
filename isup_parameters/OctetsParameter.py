#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#
class OctetsParameter:
    def __init__(self, 
        octet):
        self._octet = octet

    def __str__(self):
        return ("OctetsParameter["

        + str(self.octet)      + "]")




    @property
    def octet(self):
        return self._octet
