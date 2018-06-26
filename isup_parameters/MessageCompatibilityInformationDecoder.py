#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#

from decoders.stream_decoder import *
from isup_parameters.MessageCompatibilityInformationParameter import *

from isup_parameters.MessageCompatibilityInformationFlag import *

from isup_parameters.BroadbandNarrowbandInterworking import *

class MessageCompatibilityInformationDecoder:

    @staticmethod
    def getTag():
        return 0x038
    @staticmethod
    def decode(stream):
        flags = set()
        if (stream.readField(1)):
            flags.add(MessageCompatibilityInformationFlag.TransitAtIntermediateExchange)


        if (stream.readField(1)):
            flags.add(MessageCompatibilityInformationFlag.ReleaseCall)


        if (stream.readField(1)):
            flags.add(MessageCompatibilityInformationFlag.SendNotification)


        if (stream.readField(1)):
            flags.add(MessageCompatibilityInformationFlag.DiscardMessage)


        if (stream.readField(1)):
            flags.add(MessageCompatibilityInformationFlag.PassOnNotPossible)


        broadbandNarrowbandInterworking = BroadbandNarrowbandInterworkingDict.lookup(stream.readField(2))

        if (stream.readField(1)):
            flags.add(MessageCompatibilityInformationFlag.Extension)


        return MessageCompatibilityInformationParameter(flags,
            broadbandNarrowbandInterworking)
