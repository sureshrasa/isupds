#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#

from decoders.stream_decoder import *
from isup_parameters.AddressSignalsParameter import *


from isup_parameters.Digit import *

class AddressSignalsDecoder:
    @staticmethod
    def decode(stream):

        digit = Digit(stream.readField(4))

        return AddressSignalsParameter(
            digit)
