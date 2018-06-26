#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#

from decoders.stream_decoder import *
from isup_parameters.CalledSubscriberBasicServiceMarksParameter import *

from isup_parameters.CalledSubscriberBasicServiceMarksFlag import *

from isup_parameters.TariffGroup import *

class CalledSubscriberBasicServiceMarksDecoder:

    @staticmethod
    def getTag():
        return 0x0FA
    @staticmethod
    def decode(stream):
        flags = set()
        if (stream.readField(1)):
            flags.add(CalledSubscriberBasicServiceMarksFlag.AdminOrMaintenanceCallBarring)


        if (stream.readField(1)):
            flags.add(CalledSubscriberBasicServiceMarksFlag.SubscriberControlledIncomingCallsBarred)


        if (stream.readField(1)):
            flags.add(CalledSubscriberBasicServiceMarksFlag.PrearrangedIncomingCallsBarred)


        if (stream.readField(1)):
            flags.add(CalledSubscriberBasicServiceMarksFlag.PermanentIncomingCallsBarred)


        if (stream.readField(1)):
            flags.add(CalledSubscriberBasicServiceMarksFlag.TemporaryOutOfService)


        if (stream.readField(1)):
            flags.add(CalledSubscriberBasicServiceMarksFlag.IncomingCallsBarredExceptForOperator)


        if (stream.readField(1)):
            flags.add(CalledSubscriberBasicServiceMarksFlag.CalledSubscriberFacilityInformation)


        if (stream.readField(1)):
            flags.add(CalledSubscriberBasicServiceMarksFlag.CallingSubscriberFacilityInformation)


        if (stream.readField(1)):
            flags.add(CalledSubscriberBasicServiceMarksFlag.PermanentOutgoingCallsBarred)


        if (stream.readField(1)):
            flags.add(CalledSubscriberBasicServiceMarksFlag.OutgoingLocalCallsBarred)


        if (stream.readField(1)):
            flags.add(CalledSubscriberBasicServiceMarksFlag.OutgoingNationalCallsBarred)


        if (stream.readField(1)):
            flags.add(CalledSubscriberBasicServiceMarksFlag.OutgoingInternationalCallsBarred)


        if (stream.readField(1)):
            flags.add(CalledSubscriberBasicServiceMarksFlag.OperatorCallsBarred)


        if (stream.readField(1)):
            flags.add(CalledSubscriberBasicServiceMarksFlag.SupplementaryFacilityCallsBarred)


        if (stream.readField(1)):
            flags.add(CalledSubscriberBasicServiceMarksFlag.DigitMasking)


        if (stream.readField(1)):
            flags.add(CalledSubscriberBasicServiceMarksFlag.CallsToPremiumPhonesBarred)


        tariffGroup = TariffGroup(stream.readField(6))

        stream.readField(1)

        if (stream.readField(1)):
            flags.add(CalledSubscriberBasicServiceMarksFlag.Operator)


        return CalledSubscriberBasicServiceMarksParameter(flags,
            tariffGroup)
