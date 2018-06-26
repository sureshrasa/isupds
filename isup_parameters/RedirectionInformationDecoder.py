#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#

from decoders.stream_decoder import *
from isup_parameters.RedirectionInformationParameter import *


from isup_parameters.RedirectionIndicator import *
from isup_parameters.OriginalRedirectionReason import *
from isup_parameters.RedirectionCounter import *
from isup_parameters.RedirectingReason import *

class RedirectionInformationDecoder:

    @staticmethod
    def getTag():
        return 0x013
    @staticmethod
    def decode(stream):

        redirectionIndicator = RedirectionIndicatorDict.lookup(stream.readField(3))

        stream.readField(1)

        originalRedirectionReason = OriginalRedirectionReasonDict.lookup(stream.readField(4))

        redirectionCounter = RedirectionCounter(stream.readField(3))

        stream.readField(1)

        redirectingReason = RedirectingReasonDict.lookup(stream.readField(4))

        return RedirectionInformationParameter(
            redirectionIndicator, originalRedirectionReason, redirectionCounter, redirectingReason)
