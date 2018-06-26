#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#

from decoders.stream_decoder import *
from isup_parameters.TransmissionMediumRequirementParameter import *


from isup_parameters.TransmissionMediumRequirement import *

class TransmissionMediumRequirementDecoder:

    @staticmethod
    def getTag():
        return 0x02
    @staticmethod
    def decode(stream):

        transmissionMediumRequirement = TransmissionMediumRequirementDict.lookup(stream.readField(8))

        return TransmissionMediumRequirementParameter(
            transmissionMediumRequirement)
