#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#

from decoders.stream_decoder import *
from isup_parameters.OptionalBackwardCallIndicatorsParameter import *

from isup_parameters.OptionalBackwardCallIndicatorsFlag import *

class OptionalBackwardCallIndicatorsDecoder:

    @staticmethod
    def getTag():
        return 0x029
    @staticmethod
    def decode(stream):
        flags = set()
        if (stream.readField(1)):
            flags.add(OptionalBackwardCallIndicatorsFlag.InbandInformationIndicator)


        if (stream.readField(1)):
            flags.add(OptionalBackwardCallIndicatorsFlag.CallDiversionMayOccurIndicator)


        if (stream.readField(1)):
            flags.add(OptionalBackwardCallIndicatorsFlag.SimpleSegmentationIndicator)


        if (stream.readField(1)):
            flags.add(OptionalBackwardCallIndicatorsFlag.MlppUserIndicator)


        stream.readField(4)

        return OptionalBackwardCallIndicatorsParameter(flags
)
