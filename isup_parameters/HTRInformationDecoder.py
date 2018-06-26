#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#

from decoders.stream_decoder import *
from isup_parameters.HTRInformationParameter import *

from isup_parameters.HTRInformationFlag import *

from isup_parameters.NatureOfAddress import *
from isup_parameters.AddressSignalsParameter import *
from isup_parameters.AddressSignalsDecoder import *

class HTRInformationDecoder:

    @staticmethod
    def getTag():
        return 0x082
    @staticmethod
    def decode(stream):
        flags = set()
        natureOfAddress = NatureOfAddressDict.lookup(stream.readField(7))

        if (stream.readField(1)):
            flags.add(HTRInformationFlag.OddAddressSignals)


        stream.readField(4)

        stream.readField(3)

        stream.readField(1)

        addressSignals = []
        while(stream.hasMore()):
            addressSignalsParameter = AddressSignalsDecoder.decode(stream)
            # HTRInformationFlag::OddAddressSignals is TRUE if there are an ODD number of addressSignals
            # (We also need to skip any padding in this case)
            if (stream.hasMore() or (HTRInformationFlag.OddAddressSignals not in flags)):
                addressSignals.append(addressSignalsParameter)
        return HTRInformationParameter(flags,
            natureOfAddress, addressSignals)
