#
#  Author(s): Suresh Rasakulasuriar
#
#  Copyright: © Resilientplc.com Ltd. 2018 - All Rights Reserved
#

from enum import IntEnum, unique

@unique
class CallingPartyCategory(IntEnum):
    Unknown = 0
    FrenchLanguageOperator = 1
    EnglishLanguageOperator = 2
    GermanLanguageOperator = 3
    RussianLanguageOperator = 4
    SpanishLanguageOperator = 5
    OrdinarySubscriber = 10
    PrioritySubscriber = 11
    OssOperator = 252
    UNRECOGNISED = 0xFFFF

class CallingPartyCategoryDict:
    _dict = {
    0 : CallingPartyCategory.Unknown,
    1 : CallingPartyCategory.FrenchLanguageOperator,
    2 : CallingPartyCategory.EnglishLanguageOperator,
    3 : CallingPartyCategory.GermanLanguageOperator,
    4 : CallingPartyCategory.RussianLanguageOperator,
    5 : CallingPartyCategory.SpanishLanguageOperator,
    10 : CallingPartyCategory.OrdinarySubscriber,
    11 : CallingPartyCategory.PrioritySubscriber,
    252 : CallingPartyCategory.OssOperator    }

    @staticmethod
    def lookup(ordinal):
        return CallingPartyCategoryDict._dict.get(ordinal, ordinal)