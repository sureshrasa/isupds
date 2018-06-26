#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#

from decoders.stream_decoder import *
from isup_parameters.LastDivertingLineIdentityParameter import *

from isup_parameters.LastDivertingLineIdentityFlag import *

from isup_parameters.NatureOfAddress import *
from isup_parameters.ScreeningIndicator import *
from isup_parameters.AddressPresentationRestricted import *
from isup_parameters.AddressSignalsParameter import *
from isup_parameters.AddressSignalsDecoder import *

class LastDivertingLineIdentityDecoder:

    @staticmethod
    def getTag():
        return 0x0FC
    @staticmethod
    def decode(stream):
        flags = set()
        natureOfAddress = NatureOfAddressDict.lookup(stream.readField(7))

        if (stream.readField(1)):
            flags.add(LastDivertingLineIdentityFlag.OddAddressSignals)


        screeningIndicator = ScreeningIndicatorDict.lookup(stream.readField(2))

        addressPresentationRestricted = AddressPresentationRestrictedDict.lookup(stream.readField(2))

        stream.readField(3)

        if (stream.readField(1)):
            flags.add(LastDivertingLineIdentityFlag.NumberIncomplete)


        addressSignals = []
        while(stream.hasMore()):
            addressSignalsParameter = AddressSignalsDecoder.decode(stream)
            # LastDivertingLineIdentityFlag::OddAddressSignals is TRUE if there are an ODD number of addressSignals
            # (We also need to skip any padding in this case)
            if (stream.hasMore() or (LastDivertingLineIdentityFlag.OddAddressSignals not in flags)):
                addressSignals.append(addressSignalsParameter)
        return LastDivertingLineIdentityParameter(flags,
            natureOfAddress, screeningIndicator, addressPresentationRestricted, addressSignals)
