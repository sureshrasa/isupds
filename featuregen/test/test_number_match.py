'''
Created on 14 Jun 2018

@author: suresh
'''
import unittest
from featuregen.number_match import NumberMatchCalc, NumberMatch

telnumA1 = "+442031623000"
telnumA2 = "+442031621234"
telnumA3 = "+44203162"
telnumB1 = "+441923123456"
telnumB2 = "+44100"
telnumC1 = "+1410000099"
telnumC2 = "+1515"
telnumC3 = "+1410000088"

class Test(unittest.TestCase):

    def testEqual(self):
        self.assertEqual(NumberMatchCalc.getNumberMatch(telnumA1, telnumA1), NumberMatch.Equal)
        self.assertEqual(NumberMatchCalc.getNumberMatch(telnumB1, telnumB1), NumberMatch.Equal)

    def testNotEqual(self):
        self.assertEqual(NumberMatchCalc.getNumberMatch(telnumA2, telnumC1), NumberMatch.NotEqual)
        self.assertEqual(NumberMatchCalc.getNumberMatch(telnumC1, telnumB2), NumberMatch.NotEqual)
        
    def testSameRange(self):
        self.assertEqual(NumberMatchCalc.getNumberMatch(telnumA1, telnumA2), NumberMatch.SameRange)
        self.assertEqual(NumberMatchCalc.getNumberMatch(telnumA1, telnumA3), NumberMatch.SameRange)
        
    def testSameCountry(self):
        self.assertEqual(NumberMatchCalc.getNumberMatch(telnumA1, telnumB1), NumberMatch.SameCountry)
        self.assertEqual(NumberMatchCalc.getNumberMatch(telnumC1, telnumC2), NumberMatch.SameCountry)
        self.assertEqual(NumberMatchCalc.getNumberMatch(telnumC1, telnumC3), NumberMatch.SameCountry)
        
if __name__ == "__main__":
    unittest.main()