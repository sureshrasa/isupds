#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#
class AddressSignalsParameter:
    def __init__(self, 
        digit):
        self._digit = digit

    def __str__(self):
        return ("AddressSignalsParameter["

        + str(self.digit)      + "]")




    @property
    def digit(self):
        return self._digit
