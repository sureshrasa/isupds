#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#

from decoders.stream_decoder import *
from isup_parameters.CalledPartyNumberParameter import *

from isup_parameters.CalledPartyNumberFlag import *

from isup_parameters.NatureOfAddress import *
from isup_parameters.AddressSignalsParameter import *
from isup_parameters.AddressSignalsDecoder import *

class CalledPartyNumberDecoder:

    @staticmethod
    def getTag():
        return 0x04
    @staticmethod
    def decode(stream):
        flags = set()
        natureOfAddress = NatureOfAddressDict.lookup(stream.readField(7))

        if (stream.readField(1)):
            flags.add(CalledPartyNumberFlag.OddAddressSignals)


        stream.readField(4)

        stream.readField(3)

        if (stream.readField(1)):
            flags.add(CalledPartyNumberFlag.InternalNetworkNumberIndicator)


        addressSignals = []
        while(stream.hasMore()):
            addressSignalsParameter = AddressSignalsDecoder.decode(stream)
            # CalledPartyNumberFlag::OddAddressSignals is TRUE if there are an ODD number of addressSignals
            # (We also need to skip any padding in this case)
            if (stream.hasMore() or (CalledPartyNumberFlag.OddAddressSignals not in flags)):
                addressSignals.append(addressSignalsParameter)
        return CalledPartyNumberParameter(flags,
            natureOfAddress, addressSignals)
