#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#

from decoders.stream_decoder import *
from isup_parameters.NationalForwardCallIndicatorsParameter import *

from isup_parameters.NationalForwardCallIndicatorsFlag import *

class NationalForwardCallIndicatorsDecoder:

    @staticmethod
    def getTag():
        return 0x0FE
    @staticmethod
    def decode(stream):
        flags = set()
        if (stream.readField(1)):
            flags.add(NationalForwardCallIndicatorsFlag.CliBlocking)


        if (stream.readField(1)):
            flags.add(NationalForwardCallIndicatorsFlag.NetworkTranslatedAddress)


        if (stream.readField(1)):
            flags.add(NationalForwardCallIndicatorsFlag.PriorityAccess)


        if (stream.readField(1)):
            flags.add(NationalForwardCallIndicatorsFlag.Protection)


        stream.readField(4)

        stream.readField(8)

        return NationalForwardCallIndicatorsParameter(flags
)
