#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#

from decoders.stream_decoder import *
from isup_parameters.UserServiceInformationParameter import *


from isup_parameters.OctetsParameter import *
from isup_parameters.OctetsDecoder import *

class UserServiceInformationDecoder:

    @staticmethod
    def getTag():
        return 0x01D
    @staticmethod
    def decode(stream):

        octets = []
        while(stream.hasMore()):
            octetsParameter = OctetsDecoder.decode(stream)
            octets.append(octetsParameter)
        return UserServiceInformationParameter(
            octets)
