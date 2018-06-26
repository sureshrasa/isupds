'''
Created on 14 Jun 2018

@author: suresh
'''
from enum import IntEnum, unique

@unique
class NumberMatch(IntEnum):
    Equal = 0,
    SameRange = 1,
    SameCountry = 2,
    NotEqual = 4
    
class NumberMatchCalc:
    @staticmethod
    def getNumberMatch(telnumA, telnumB):
        if telnumA == telnumB:
            return NumberMatch.Equal
        
        if telnumA.startswith("+44") and telnumA.startswith(telnumB[0:9], 0, 9):
            return NumberMatch.SameRange
            
        if telnumA.startswith(telnumB[0:3], 0, 3):
            return NumberMatch.SameCountry
        
        if telnumA.startswith("+1") and telnumB.startswith("+1"):
            return NumberMatch.SameCountry
        
        return NumberMatch.NotEqual
        