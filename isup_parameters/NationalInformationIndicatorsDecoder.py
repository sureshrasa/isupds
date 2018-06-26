#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#

from decoders.stream_decoder import *
from isup_parameters.NationalInformationIndicatorsParameter import *

from isup_parameters.NationalInformationIndicatorsFlag import *

class NationalInformationIndicatorsDecoder:

    @staticmethod
    def getTag():
        return 0x0F5
    @staticmethod
    def decode(stream):
        flags = set()
        if (stream.readField(1)):
            flags.add(NationalInformationIndicatorsFlag.CallingSubscribersBasicServiceMarksResponse)


        if (stream.readField(1)):
            flags.add(NationalInformationIndicatorsFlag.CalledSubscribersBasicServiceMarksResponse)


        if (stream.readField(1)):
            flags.add(NationalInformationIndicatorsFlag.CallingSubscribersOriginatingFacilityMarksResponse)


        if (stream.readField(1)):
            flags.add(NationalInformationIndicatorsFlag.CalledSubscribersTerminatingFacilityMarksResponse)


        if (stream.readField(1)):
            flags.add(NationalInformationIndicatorsFlag.InterceptedLineIdentityResponse)


        if (stream.readField(1)):
            flags.add(NationalInformationIndicatorsFlag.InterceptedLineIdentityAndCalledSubscribersBasicServiceMarksResponse)


        stream.readField(2)

        stream.readField(8)

        return NationalInformationIndicatorsParameter(flags
)
