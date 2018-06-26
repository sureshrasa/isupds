from enum import IntEnum, unique

import pygtrie

@unique
class NumberType(IntEnum):
    UkGeo = 0,
    UkNonGeo = 1,
    UkMobile = 2,
    UkCorp = 3,
    UkPersonal = 4,
    UkPaging = 5,
    UkFreephone = 6,
    UkSpecific = 7,
    UkOther = 8,
    International =9,
    Other = -1

@unique
class NumberFormat(IntEnum):
    Valid = 0,
    Invalid = 1

class NumberTypeCalc:
    _telNumberToTypeTree = pygtrie.CharTrie()
    _telNumberToTypeTree["+441"] = NumberType.UkGeo
    _telNumberToTypeTree["+442"] = NumberType.UkGeo
    _telNumberToTypeTree["+4430"] = NumberType.UkNonGeo
    _telNumberToTypeTree["+4433"] = NumberType.UkNonGeo
    _telNumberToTypeTree["+4434"] = NumberType.UkNonGeo
    _telNumberToTypeTree["+4437"] = NumberType.UkNonGeo
    _telNumberToTypeTree["+4455"] = NumberType.UkCorp
    _telNumberToTypeTree["+4407"] = NumberType.UkGeo
    _telNumberToTypeTree["+4456"] = NumberType.UkNonGeo
    _telNumberToTypeTree["+4470"] = NumberType.UkPersonal
    _telNumberToTypeTree["+4476"] = NumberType.UkPaging
    _telNumberToTypeTree["+4471"] = NumberType.UkMobile
    _telNumberToTypeTree["+4472"] = NumberType.UkMobile
    _telNumberToTypeTree["+4473"] = NumberType.UkMobile
    _telNumberToTypeTree["+4474"] = NumberType.UkMobile
    _telNumberToTypeTree["+4475"] = NumberType.UkMobile
    _telNumberToTypeTree["+4477"] = NumberType.UkMobile
    _telNumberToTypeTree["+4478"] = NumberType.UkMobile
    _telNumberToTypeTree["+4479"] = NumberType.UkMobile
    _telNumberToTypeTree["+4480"] = NumberType.UkFreephone
    _telNumberToTypeTree["+4482"] = NumberType.UkNonGeo
    _telNumberToTypeTree["+44843"] = NumberType.UkNonGeo
    _telNumberToTypeTree["+44844"] = NumberType.UkNonGeo
    _telNumberToTypeTree["+44845"] = NumberType.UkNonGeo
    _telNumberToTypeTree["+44870"] = NumberType.UkNonGeo
    _telNumberToTypeTree["+44871"] = NumberType.UkNonGeo
    _telNumberToTypeTree["+44872"] = NumberType.UkNonGeo
    _telNumberToTypeTree["+44873"] = NumberType.UkNonGeo
    _telNumberToTypeTree["+4490"] = NumberType.UkNonGeo
    _telNumberToTypeTree["+4491"] = NumberType.UkNonGeo
    _telNumberToTypeTree["+4498"] = NumberType.UkNonGeo
    _telNumberToTypeTree["uk:"] = NumberType.UkSpecific
    _telNumberToTypeTree["+44"] = NumberType.UkOther
    _telNumberToTypeTree["+"] = NumberType.International

    @staticmethod
    def getType(number):
        key, result = NumberTypeCalc._telNumberToTypeTree.longest_prefix(number)
        return NumberType.Other if key is None else result
    
    _digitLengths = {
                  NumberType.UkGeo:(12,13),
                  NumberType.UkNonGeo:(12,13),
                  NumberType.UkFreephone:(12,13),
                  NumberType.UkCorp:(12,13),
                  NumberType.UkMobile:(13,13),
                  NumberType.UkPaging:(13,13),
                  NumberType.UkPersonal:(13,13),
                  NumberType.UkOther:(12,13),
                  NumberType.UkSpecific:(14,18),
                  NumberType.International:(14,20),
                  NumberType.Other:(1,20)
                  }
    
    @staticmethod
    def getDigitLength(numType):
        return NumberTypeCalc._digitLengths.get(numType, None) 
        
    @staticmethod
    def getFormat(numType, e164):
        e164Len = len(e164)
        limits = NumberTypeCalc.getDigitLength(numType)
        
        return NumberFormat.Invalid if e164Len < limits[0] or e164Len > limits[1] else NumberFormat.Valid
