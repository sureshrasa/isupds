#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#
class DiagnosticsParameter:
    def __init__(self, 
        diagnostic):
        self._diagnostic = diagnostic

    def __str__(self):
        return ("DiagnosticsParameter["

        + str(self.diagnostic)      + "]")




    @property
    def diagnostic(self):
        return self._diagnostic
