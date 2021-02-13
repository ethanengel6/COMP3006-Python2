import unittest

import blackjack3
from blackjack3 import *

class testHand(unittest.TestCase):

    def testscore(self):
        ha3=Hand([3,4])
        self.assertEqual(ha3.score(),(7,0))

    def testscore2(self):
        ha4=Hand([3,4,1])
        self.assertEqual(ha4.score(),(18,1))

    def testscore3(self):
        ha5=Hand([10,3,4,1])
        self.assertEqual(ha5.score(),(18,0))

    def testscore4(self):
        ha6=Hand([10,13])
        self.assertEqual(ha6.score(),(20,0))

    def testBust(self):
        ha=Hand([10,10,10])
        self.assertTrue(ha.is_bust())

    def testnotBust(self):
        ha2=Hand([10,10])
        self.assertFalse(ha2.is_bust())

    def testnotBlackjack(self):
        ha7=Hand([10,13])
        self.assertFalse(ha7.is_blackjack())

    def testBlackjack(self):
        ha8=Hand([1,13])
        self.assertTrue(ha8.is_blackjack())


class testStrategy(unittest.TestCase):

    def testStand(self):#standing when over the threshold
        s=Strategy(16,True)
        self.assertTrue(s.stand(Hand([10,10])))

    def testStand2(self):#standing on a soft ace
        s=Strategy(16,True)
        self.assertTrue(s.stand(Hand([1,5])))

    def testStand(self):#Not standing when under the threshhold
        s=Strategy(16,True)
        self.assertFalse(s.stand(Hand([10,5])))

    def testStand(self):#not standing on a soft ace
        s=Strategy(16,False)
        self.assertFalse(s.stand(Hand([1,5])))
