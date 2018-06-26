#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#

from decoders.stream_decoder import *
from isup_parameters.GenericNumberParameter import *

from isup_parameters.GenericNumberFlag import *

from isup_parameters.NumberQualifier import *
from isup_parameters.NatureOfAddress import *
from isup_parameters.ScreeningIndicator import *
from isup_parameters.AddressPresentationRestricted import *
from isup_parameters.AddressSignalsParameter import *
from isup_parameters.AddressSignalsDecoder import *

class GenericNumberDecoder:

    @staticmethod
    def getTag():
        return 0x0C0
    @staticmethod
    def decode(stream):
        flags = set()
        numberQualifier = NumberQualifierDict.lookup(stream.readField(8))

        natureOfAddress = NatureOfAddressDict.lookup(stream.readField(7))

        if (stream.readField(1)):
            flags.add(GenericNumberFlag.OddAddressSignals)


        screeningIndicator = ScreeningIndicatorDict.lookup(stream.readField(2))

        addressPresentationRestricted = AddressPresentationRestrictedDict.lookup(stream.readField(2))

        stream.readField(3)

        if (stream.readField(1)):
            flags.add(GenericNumberFlag.NumberIncomplete)


        addressSignals = []
        while(stream.hasMore()):
            addressSignalsParameter = AddressSignalsDecoder.decode(stream)
            # GenericNumberFlag::OddAddressSignals is TRUE if there are an ODD number of addressSignals
            # (We also need to skip any padding in this case)
            if (stream.hasMore() or (GenericNumberFlag.OddAddressSignals not in flags)):
                addressSignals.append(addressSignalsParameter)
        return GenericNumberParameter(flags,
            numberQualifier, natureOfAddress, screeningIndicator, addressPresentationRestricted, addressSignals)
