'''
Created on 14 Jun 2018

@author: suresh
'''

from isup_parameters import *
from isup_parameters.RedirectionCounter import RedirectionCounter

class ParameterTraits:
    _ukSpecificParamTags = [
            NationalForwardCallIndicatorsParameter.getTag(),
            PresentationNumberParameter.getTag(),
            LastDivertingLineIdentityParameter.getTag(),
            #PartialCallingLineIdentityParameter.getTag(),
            CalledSubscriberBasicServiceMarksParameter.getTag(),
            #CallingSubscriberBasicServiceMarksParameter.getTag(),
            #CallingSubscribersOriginatingFacilityMarksParameter.getTag(),
            #CalledSubscriberTerminatingFacilityMarksParameter.getTag(),
            #NationalRequestInformationIndicatorsParameter.getTag(),
            NationalInformationIndicatorsParameter.getTag()
            ]
    
    _containsDiversionTags = [
            RedirectingNumberParameter.getTag(),
            RedirectionInformationParameter.getTag(),
            OriginalCalledNumberParameter.getTag()
            ]
    
    @staticmethod
    def isUkSpecificParam(tag):
        return tag in ParameterTraits._ukSpecificParamTags

    @staticmethod
    def containsDiversion(tag):
        return tag in ParameterTraits._containsDiversionTags
 