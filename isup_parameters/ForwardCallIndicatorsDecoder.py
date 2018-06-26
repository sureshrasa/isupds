#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#

from decoders.stream_decoder import *
from isup_parameters.ForwardCallIndicatorsParameter import *

from isup_parameters.ForwardCallIndicatorsFlag import *

from isup_parameters.IsdnUserPartPreferenceIndicator import *

class ForwardCallIndicatorsDecoder:

    @staticmethod
    def getTag():
        return 0x07
    @staticmethod
    def decode(stream):
        flags = set()
        if (stream.readField(1)):
            flags.add(ForwardCallIndicatorsFlag.InternationalCall)


        stream.readField(2)

        if (stream.readField(1)):
            flags.add(ForwardCallIndicatorsFlag.InterworkingEncountered)


        if (stream.readField(1)):
            flags.add(ForwardCallIndicatorsFlag.EndToEndInformationAvailable)


        if (stream.readField(1)):
            flags.add(ForwardCallIndicatorsFlag.IsdnUserPartUsedAllTheWay)


        isdnUserPartPreferenceIndicator = IsdnUserPartPreferenceIndicatorDict.lookup(stream.readField(2))

        if (stream.readField(1)):
            flags.add(ForwardCallIndicatorsFlag.OriginatingAccessIsdn)


        stream.readField(2)

        stream.readField(5)

        return ForwardCallIndicatorsParameter(flags,
            isdnUserPartPreferenceIndicator)
