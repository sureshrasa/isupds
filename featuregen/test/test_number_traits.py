'''
Created on 13 Jun 2018

@author: suresh
'''
import unittest
from featuregen.number_traits import NumberType, NumberTypeCalc


class TestNumberType(unittest.TestCase):


    def testUkGeo(self):
        self.assertEqual(NumberTypeCalc.getType("+441923876543"), NumberType.UkGeo)
        self.assertEqual(NumberTypeCalc.getType("+442031623000"), NumberType.UkGeo)
        self.assertEqual(NumberTypeCalc.getDigitLength(NumberType.UkGeo), (12,13))

    def testUkNonGeo(self):
        self.assertEqual(NumberTypeCalc.getType("+44300123456"), NumberType.UkNonGeo)
        self.assertEqual(NumberTypeCalc.getType("+44845123456"), NumberType.UkNonGeo)
        self.assertEqual(NumberTypeCalc.getDigitLength(NumberType.UkNonGeo), (12,13))

    def testUkMobile(self):
        self.assertEqual(NumberTypeCalc.getType("+447767123456"), NumberType.UkMobile)
        self.assertEqual(NumberTypeCalc.getType("+447177812345"), NumberType.UkMobile)
        self.assertEqual(NumberTypeCalc.getDigitLength(NumberType.UkMobile), (13,13))

    def testUkCorp(self):
        self.assertEqual(NumberTypeCalc.getType("+445567123456"), NumberType.UkCorp)
        self.assertEqual(NumberTypeCalc.getType("+445577812345"), NumberType.UkCorp)
        self.assertEqual(NumberTypeCalc.getDigitLength(NumberType.UkCorp), (12,13))

    def testUkPersonal(self):
        self.assertEqual(NumberTypeCalc.getType("+447067123456"), NumberType.UkPersonal)
        self.assertEqual(NumberTypeCalc.getType("+447077812345"), NumberType.UkPersonal)
        self.assertEqual(NumberTypeCalc.getDigitLength(NumberType.UkPersonal), (13,13))

    def testUkPaging(self):
        self.assertEqual(NumberTypeCalc.getType("+447667123456"), NumberType.UkPaging)
        self.assertEqual(NumberTypeCalc.getType("+447677812345"), NumberType.UkPaging)
        self.assertEqual(NumberTypeCalc.getDigitLength(NumberType.UkPaging), (13,13))

    def testUkFreephone(self):
        self.assertEqual(NumberTypeCalc.getType("+448067123456"), NumberType.UkFreephone)
        self.assertEqual(NumberTypeCalc.getType("+448007812345"), NumberType.UkFreephone)
        self.assertEqual(NumberTypeCalc.getDigitLength(NumberType.UkFreephone), (12,13))

    def testUkSpecific(self):
        self.assertEqual(NumberTypeCalc.getType("uk:7512307767123456"), NumberType.UkSpecific)
        self.assertEqual(NumberTypeCalc.getType("uk:7677801098762345"), NumberType.UkSpecific)
        self.assertEqual(NumberTypeCalc.getDigitLength(NumberType.UkSpecific), (14,18))

    def testUkOther(self):
        self.assertEqual(NumberTypeCalc.getType("+440"), NumberType.UkOther)
        self.assertEqual(NumberTypeCalc.getType("+440001"), NumberType.UkOther)
        self.assertEqual(NumberTypeCalc.getDigitLength(NumberType.UkOther), (12, 13))

    def testInternational(self):
        self.assertEqual(NumberTypeCalc.getType("+417767123456"), NumberType.International)
        self.assertEqual(NumberTypeCalc.getType("+17677812345"), NumberType.International)
        self.assertEqual(NumberTypeCalc.getDigitLength(NumberType.International), (14,20))
        
    def testOther(self):
        self.assertEqual(NumberTypeCalc.getType("7123456"), NumberType.Other)
        self.assertEqual(NumberTypeCalc.getType("12345"), NumberType.Other)
        self.assertEqual(NumberTypeCalc.getDigitLength(NumberType.Other), (1,20))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()