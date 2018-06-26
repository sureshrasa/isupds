#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#

from decoders.stream_decoder import *
from isup_parameters.OriginalCalledNumberParameter import *

from isup_parameters.OriginalCalledNumberFlag import *

from isup_parameters.NatureOfAddress import *
from isup_parameters.AddressPresentationRestricted import *
from isup_parameters.AddressSignalsParameter import *
from isup_parameters.AddressSignalsDecoder import *

class OriginalCalledNumberDecoder:

    @staticmethod
    def getTag():
        return 0x028
    @staticmethod
    def decode(stream):
        flags = set()
        natureOfAddress = NatureOfAddressDict.lookup(stream.readField(7))

        if (stream.readField(1)):
            flags.add(OriginalCalledNumberFlag.OddAddressSignals)


        stream.readField(2)

        addressPresentationRestricted = AddressPresentationRestrictedDict.lookup(stream.readField(2))

        stream.readField(3)

        stream.readField(1)

        addressSignals = []
        while(stream.hasMore()):
            addressSignalsParameter = AddressSignalsDecoder.decode(stream)
            # OriginalCalledNumberFlag::OddAddressSignals is TRUE if there are an ODD number of addressSignals
            # (We also need to skip any padding in this case)
            if (stream.hasMore() or (OriginalCalledNumberFlag.OddAddressSignals not in flags)):
                addressSignals.append(addressSignalsParameter)
        return OriginalCalledNumberParameter(flags,
            natureOfAddress, addressPresentationRestricted, addressSignals)
