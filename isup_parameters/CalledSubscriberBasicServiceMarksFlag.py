#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#

from enum import IntEnum, unique

@unique
class CalledSubscriberBasicServiceMarksFlag(IntEnum):
    AdminOrMaintenanceCallBarring = 0
    SubscriberControlledIncomingCallsBarred = 1
    PrearrangedIncomingCallsBarred = 2
    PermanentIncomingCallsBarred = 3
    TemporaryOutOfService = 4
    IncomingCallsBarredExceptForOperator = 5
    CalledSubscriberFacilityInformation = 6
    CallingSubscriberFacilityInformation = 7
    PermanentOutgoingCallsBarred = 8
    OutgoingLocalCallsBarred = 9
    OutgoingNationalCallsBarred = 10
    OutgoingInternationalCallsBarred = 11
    OperatorCallsBarred = 12
    SupplementaryFacilityCallsBarred = 13
    DigitMasking = 14
    CallsToPremiumPhonesBarred = 15
    Operator = 16
    UNRECOGNISED = 0xFFFF

class CalledSubscriberBasicServiceMarksFlagDict:
    _dict = {
    0 : CalledSubscriberBasicServiceMarksFlag.AdminOrMaintenanceCallBarring,
    1 : CalledSubscriberBasicServiceMarksFlag.SubscriberControlledIncomingCallsBarred,
    2 : CalledSubscriberBasicServiceMarksFlag.PrearrangedIncomingCallsBarred,
    3 : CalledSubscriberBasicServiceMarksFlag.PermanentIncomingCallsBarred,
    4 : CalledSubscriberBasicServiceMarksFlag.TemporaryOutOfService,
    5 : CalledSubscriberBasicServiceMarksFlag.IncomingCallsBarredExceptForOperator,
    6 : CalledSubscriberBasicServiceMarksFlag.CalledSubscriberFacilityInformation,
    7 : CalledSubscriberBasicServiceMarksFlag.CallingSubscriberFacilityInformation,
    8 : CalledSubscriberBasicServiceMarksFlag.PermanentOutgoingCallsBarred,
    9 : CalledSubscriberBasicServiceMarksFlag.OutgoingLocalCallsBarred,
    10 : CalledSubscriberBasicServiceMarksFlag.OutgoingNationalCallsBarred,
    11 : CalledSubscriberBasicServiceMarksFlag.OutgoingInternationalCallsBarred,
    12 : CalledSubscriberBasicServiceMarksFlag.OperatorCallsBarred,
    13 : CalledSubscriberBasicServiceMarksFlag.SupplementaryFacilityCallsBarred,
    14 : CalledSubscriberBasicServiceMarksFlag.DigitMasking,
    15 : CalledSubscriberBasicServiceMarksFlag.CallsToPremiumPhonesBarred,
    16 : CalledSubscriberBasicServiceMarksFlag.Operator    }

    @staticmethod
    def lookup(ordinal):
        return CalledSubscriberBasicServiceMarksFlagDict._dict.get(ordinal, ordinal)