#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: � Resilientplc.com Ltd. 2018 - All Rights Reserved
#
class Octet:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    def __str__(self):
        return "Octet[" + str(self._value) + "]"