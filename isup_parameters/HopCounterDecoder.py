#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#

from decoders.stream_decoder import *
from isup_parameters.HopCounterParameter import *


from isup_parameters.HopCounter import *

class HopCounterDecoder:

    @staticmethod
    def getTag():
        return 0x03D
    @staticmethod
    def decode(stream):

        hopCounter = HopCounter(stream.readField(5))

        stream.readField(3)

        return HopCounterParameter(
            hopCounter)
