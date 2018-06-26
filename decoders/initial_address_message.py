from isup_parameters import *
from isup_parameters.IsupParameterDecoder import IsupParameterDecoder
from decoders.stream_decoder import StreamDecoderSlice
from featuregen.parameter_traits import ParameterTraits

class InitialAddressMessage:
    def __init__(self, stream):
        self._natureOfConnectionIndictors = stream.readField(8)
        self._forwardCallIndicators = ForwardCallIndicatorsDecoder.decode(stream)
        self._callingPartyCategory = CallingPartyCategoryDecoder.decode(stream)
        self._transmissionMediumRequirement = TransmissionMediumRequirementDecoder.decode(stream)
        stream.readField(8) #cpnOffset
        optionalOffset = stream.readField(8)
        self._calledPartyNumber = CalledPartyNumberDecoder.decode(StreamDecoderSlice(stream, stream.readField(8)))
        self._isUkSpecificParamPresent = False
        self._isDiverted = False
        self._signalSignature = []

        self._optionalParams = {}
        if (optionalOffset > 0):
            while (stream.hasMore()):
                tag = stream.readField(8)
                if (tag == 0):
                    break;
                
                size = stream.readField(8)
                if (size == 0):
                    break;
                
                self._signalSignature.append(tag)
                self._optionalParams[tag] = IsupParameterDecoder.decode(tag, size, StreamDecoderSlice(stream, size))
                self._isUkSpecificParamPresent = self._isUkSpecificParamPresent or ParameterTraits.isUkSpecificParam(tag)
                self._isDiverted = self._isDiverted or ParameterTraits.containsDiversion(tag)
                
            self._signalSignature = ".".join(map(lambda t:format(t, 'x'), self._signalSignature))
              
    @property
    def isUkSpecificParamsPresent(self):
        return self._isUkSpecificParamPresent

    @property
    def isDiverted(self):
        return self._isDiverted

    @property
    def natureOfConnectionIndictors(self):
        return self._natureOfConnectionIndictors

    @property
    def forwardCallIndicators(self):
        return self._forwardCallIndicators

    @property
    def callingPartyCategory(self):
        return self._callingPartyCategory

    @property
    def transmissionMediumRequirement(self):
        return self._transmissionMediumRequirement

    @property
    def calledPartyNumber(self):
        return self._calledPartyNumber

    def getOptionalParam(self, tag):
        return self._optionalParams.get(tag)
    
    @property
    def signalSignature(self):
        return self._signalSignature

    def __str__(self):
        return ("IAM["
        + str(self.natureOfConnectionIndictors) + ","
        + str(self.forwardCallIndicators) + ","
        + str(self.callingPartyCategory) + ","
        + str(self.transmissionMediumRequirement) + ","
        + str(self.calledPartyNumber) + ","
        + ",".join(map(str, self._optionalParams.values())) + "]")
