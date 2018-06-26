#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: � Resilientplc.com Ltd. 2018 - All Rights Reserved
#

from isup_parameters.CalledSubscriberBasicServiceMarksDecoder import *
from isup_parameters.HopCounterDecoder import *
from isup_parameters.NationalForwardCallIndicatorsDecoder import *
from isup_parameters.PresentationNumberDecoder import *
from isup_parameters.GenericNumberDecoder import *
from isup_parameters.CallingPartyNumberDecoder import *
from isup_parameters.TransmissionMediumRequirementDecoder import *
from isup_parameters.MessageCompatibilityInformationDecoder import *
from isup_parameters.CauseIndicatorsDecoder import *
from isup_parameters.BackwardCallIndicatorsDecoder import *
from isup_parameters.OptionalBackwardCallIndicatorsDecoder import *
from isup_parameters.OptionalForwardCallIndicatorsDecoder import *
from isup_parameters.CallingPartyCategoryDecoder import *
from isup_parameters.AutomaticCongestionLevelDecoder import *
from isup_parameters.RedirectingNumberDecoder import *
from isup_parameters.OriginalCalledNumberDecoder import *
from isup_parameters.RedirectionInformationDecoder import *
from isup_parameters.LastDivertingLineIdentityDecoder import *
from isup_parameters.UserServiceInformationDecoder import *
from isup_parameters.ForwardCallIndicatorsDecoder import *
from isup_parameters.CalledPartyNumberDecoder import *
from isup_parameters.InformationIndicatorsDecoder import *
from isup_parameters.NationalInformationIndicatorsDecoder import *
from isup_parameters.HTRInformationDecoder import *

class IsupParameterDecoder:
    _dict = {

           CalledSubscriberBasicServiceMarksDecoder.getTag() : CalledSubscriberBasicServiceMarksDecoder.decode,
           HopCounterDecoder.getTag() : HopCounterDecoder.decode,
           NationalForwardCallIndicatorsDecoder.getTag() : NationalForwardCallIndicatorsDecoder.decode,
           PresentationNumberDecoder.getTag() : PresentationNumberDecoder.decode,
           GenericNumberDecoder.getTag() : GenericNumberDecoder.decode,
           CallingPartyNumberDecoder.getTag() : CallingPartyNumberDecoder.decode,
           TransmissionMediumRequirementDecoder.getTag() : TransmissionMediumRequirementDecoder.decode,
           MessageCompatibilityInformationDecoder.getTag() : MessageCompatibilityInformationDecoder.decode,
           CauseIndicatorsDecoder.getTag() : CauseIndicatorsDecoder.decode,
           BackwardCallIndicatorsDecoder.getTag() : BackwardCallIndicatorsDecoder.decode,
           OptionalBackwardCallIndicatorsDecoder.getTag() : OptionalBackwardCallIndicatorsDecoder.decode,
           OptionalForwardCallIndicatorsDecoder.getTag() : OptionalForwardCallIndicatorsDecoder.decode,
           CallingPartyCategoryDecoder.getTag() : CallingPartyCategoryDecoder.decode,
           AutomaticCongestionLevelDecoder.getTag() : AutomaticCongestionLevelDecoder.decode,
           RedirectingNumberDecoder.getTag() : RedirectingNumberDecoder.decode,
           OriginalCalledNumberDecoder.getTag() : OriginalCalledNumberDecoder.decode,
           RedirectionInformationDecoder.getTag() : RedirectionInformationDecoder.decode,
           LastDivertingLineIdentityDecoder.getTag() : LastDivertingLineIdentityDecoder.decode,
           UserServiceInformationDecoder.getTag() : UserServiceInformationDecoder.decode,
           ForwardCallIndicatorsDecoder.getTag() : ForwardCallIndicatorsDecoder.decode,
           CalledPartyNumberDecoder.getTag() : CalledPartyNumberDecoder.decode,
           InformationIndicatorsDecoder.getTag() : InformationIndicatorsDecoder.decode,
           NationalInformationIndicatorsDecoder.getTag() : NationalInformationIndicatorsDecoder.decode,
           HTRInformationDecoder.getTag() : HTRInformationDecoder.decode
    }

    @staticmethod
    def decode(tag, size, decoder):
        if (tag in IsupParameterDecoder._dict):
            return IsupParameterDecoder._dict[tag](decoder)

        decoder.skipBytes(size)
        return None