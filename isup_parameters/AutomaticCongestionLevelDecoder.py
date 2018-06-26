#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#

from decoders.stream_decoder import *
from isup_parameters.AutomaticCongestionLevelParameter import *


from isup_parameters.CongestionLevel import *

class AutomaticCongestionLevelDecoder:

    @staticmethod
    def getTag():
        return 0x027
    @staticmethod
    def decode(stream):

        congestionLevel = CongestionLevelDict.lookup(stream.readField(8))

        return AutomaticCongestionLevelParameter(
            congestionLevel)
