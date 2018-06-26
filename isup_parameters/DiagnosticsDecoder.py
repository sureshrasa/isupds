#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#

from decoders.stream_decoder import *
from isup_parameters.DiagnosticsParameter import *


from isup_parameters.Diagnostic import *

class DiagnosticsDecoder:
    @staticmethod
    def decode(stream):

        diagnostic = Diagnostic(stream.readField(8))

        return DiagnosticsParameter(
            diagnostic)
