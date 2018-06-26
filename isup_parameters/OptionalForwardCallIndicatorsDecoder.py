#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#

from decoders.stream_decoder import *
from isup_parameters.OptionalForwardCallIndicatorsParameter import *

from isup_parameters.OptionalForwardCallIndicatorsFlag import *

from isup_parameters.ClosedUserGroupIndicator import *

class OptionalForwardCallIndicatorsDecoder:

    @staticmethod
    def getTag():
        return 0x08
    @staticmethod
    def decode(stream):
        flags = set()
        closedUserGroupIndicator = ClosedUserGroupIndicatorDict.lookup(stream.readField(2))

        if (stream.readField(1)):
            flags.add(OptionalForwardCallIndicatorsFlag.SimpleSegmentationIndicator)


        stream.readField(4)

        if (stream.readField(1)):
            flags.add(OptionalForwardCallIndicatorsFlag.ConnectedLineIdentityRequestIndicator)


        return OptionalForwardCallIndicatorsParameter(flags,
            closedUserGroupIndicator)
