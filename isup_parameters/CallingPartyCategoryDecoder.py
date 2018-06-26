#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#

from decoders.stream_decoder import *
from isup_parameters.CallingPartyCategoryParameter import *


from isup_parameters.CallingPartyCategory import *

class CallingPartyCategoryDecoder:

    @staticmethod
    def getTag():
        return 0x09
    @staticmethod
    def decode(stream):

        callingPartyCategory = CallingPartyCategoryDict.lookup(stream.readField(8))

        return CallingPartyCategoryParameter(
            callingPartyCategory)
