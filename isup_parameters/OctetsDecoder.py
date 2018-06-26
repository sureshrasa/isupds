#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#

from decoders.stream_decoder import *
from isup_parameters.OctetsParameter import *


from isup_parameters.Octet import *

class OctetsDecoder:
    @staticmethod
    def decode(stream):

        octet = Octet(stream.readField(8))

        return OctetsParameter(
            octet)
