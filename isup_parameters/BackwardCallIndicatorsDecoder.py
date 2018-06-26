#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#

from decoders.stream_decoder import *
from isup_parameters.BackwardCallIndicatorsParameter import *

from isup_parameters.BackwardCallIndicatorsFlag import *

from isup_parameters.ChargeIndicator import *
from isup_parameters.CalledPartysStatusIndicator import *
from isup_parameters.CalledPartysCategoryIndicator import *
from isup_parameters.EndToEndMethodIndicator import *
from isup_parameters.SccpMethodIndicator import *

class BackwardCallIndicatorsDecoder:

    @staticmethod
    def getTag():
        return 0x011
    @staticmethod
    def decode(stream):
        flags = set()
        chargeIndicator = ChargeIndicatorDict.lookup(stream.readField(2))

        calledPartysStatusIndicator = CalledPartysStatusIndicatorDict.lookup(stream.readField(2))

        calledPartysCategoryIndicator = CalledPartysCategoryIndicatorDict.lookup(stream.readField(2))

        endToEndMethodIndicator = EndToEndMethodIndicatorDict.lookup(stream.readField(2))

        if (stream.readField(1)):
            flags.add(BackwardCallIndicatorsFlag.InterworkingIndicator)


        if (stream.readField(1)):
            flags.add(BackwardCallIndicatorsFlag.EndToEndInformationIndicator)


        if (stream.readField(1)):
            flags.add(BackwardCallIndicatorsFlag.IsdnUserPartIndicator)


        if (stream.readField(1)):
            flags.add(BackwardCallIndicatorsFlag.HoldingIndicator)


        if (stream.readField(1)):
            flags.add(BackwardCallIndicatorsFlag.IsdnAccessIndicator)


        if (stream.readField(1)):
            flags.add(BackwardCallIndicatorsFlag.EchoControlDeviceIndicator)


        sccpMethodIndicator = SccpMethodIndicatorDict.lookup(stream.readField(2))

        return BackwardCallIndicatorsParameter(flags,
            chargeIndicator, calledPartysStatusIndicator, calledPartysCategoryIndicator, endToEndMethodIndicator, sccpMethodIndicator)
