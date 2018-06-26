#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#

from decoders.stream_decoder import *
from isup_parameters.InformationIndicatorsParameter import *

from isup_parameters.InformationIndicatorsFlag import *

from isup_parameters.CallingPartyAddressResponse import *

class InformationIndicatorsDecoder:

    @staticmethod
    def getTag():
        return 0x0F
    @staticmethod
    def decode(stream):
        flags = set()
        callingPartyAddressResponse = CallingPartyAddressResponseDict.lookup(stream.readField(2))

        if (stream.readField(1)):
            flags.add(InformationIndicatorsFlag.HoldProvided)


        stream.readField(2)

        if (stream.readField(1)):
            flags.add(InformationIndicatorsFlag.CallingPartysCategoryResponse)


        if (stream.readField(1)):
            flags.add(InformationIndicatorsFlag.ChargeInformationResponse)


        if (stream.readField(1)):
            flags.add(InformationIndicatorsFlag.SolicitedInformation)


        stream.readField(4)

        stream.readField(4)

        return InformationIndicatorsParameter(flags,
            callingPartyAddressResponse)
