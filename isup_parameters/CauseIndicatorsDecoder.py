#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#

from decoders.stream_decoder import *
from isup_parameters.CauseIndicatorsParameter import *


from isup_parameters.Location import *
from isup_parameters.CodingStandard import *
from isup_parameters.Cause import *
from isup_parameters.DiagnosticsParameter import *
from isup_parameters.DiagnosticsDecoder import *

class CauseIndicatorsDecoder:

    @staticmethod
    def getTag():
        return 0x012
    @staticmethod
    def decode(stream):

        location = LocationDict.lookup(stream.readField(4))

        stream.readField(1)

        codingStandard = CodingStandardDict.lookup(stream.readField(2))

        stream.readField(1)

        cause = Cause(stream.readField(7))

        stream.readField(1)

        diagnostics = []
        while(stream.hasMore()):
            diagnosticsParameter = DiagnosticsDecoder.decode(stream)
            diagnostics.append(diagnosticsParameter)
        return CauseIndicatorsParameter(
            location, codingStandard, cause, diagnostics)
