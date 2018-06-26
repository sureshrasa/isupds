#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#

from decoders.stream_decoder import *
from isup_parameters.RedirectingNumberParameter import *

from isup_parameters.RedirectingNumberFlag import *

from isup_parameters.NatureOfAddress import *
from isup_parameters.AddressPresentationRestricted import *
from isup_parameters.AddressSignalsParameter import *
from isup_parameters.AddressSignalsDecoder import *

class RedirectingNumberDecoder:

    @staticmethod
    def getTag():
        return 0x0B
    @staticmethod
    def decode(stream):
        flags = set()
        natureOfAddress = NatureOfAddressDict.lookup(stream.readField(7))

        if (stream.readField(1)):
            flags.add(RedirectingNumberFlag.OddAddressSignals)


        stream.readField(2)

        addressPresentationRestricted = AddressPresentationRestrictedDict.lookup(stream.readField(2))

        stream.readField(3)

        stream.readField(1)

        addressSignals = []
        while(stream.hasMore()):
            addressSignalsParameter = AddressSignalsDecoder.decode(stream)
            # RedirectingNumberFlag::OddAddressSignals is TRUE if there are an ODD number of addressSignals
            # (We also need to skip any padding in this case)
            if (stream.hasMore() or (RedirectingNumberFlag.OddAddressSignals not in flags)):
                addressSignals.append(addressSignalsParameter)
        return RedirectingNumberParameter(flags,
            natureOfAddress, addressPresentationRestricted, addressSignals)
