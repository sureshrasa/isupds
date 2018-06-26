#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#
from isup_parameters.TransmissionMediumRequirement import *
class TransmissionMediumRequirementParameter:
    def __init__(self, 
        transmissionMediumRequirement):
        self._transmissionMediumRequirement = transmissionMediumRequirement

    def __str__(self):
        return ("TransmissionMediumRequirementParameter["

        + str(self.transmissionMediumRequirement)      + "]")


    @staticmethod
    def getTag():
        return 0x02



    @property
    def transmissionMediumRequirement(self):
        return self._transmissionMediumRequirement
