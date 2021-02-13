import unittest

import blackjack
from blackjack import *

class testScore(unittest.TestCase):
    #[ 3, 12 ] → (13, 0)
    def testplainPair(self):
        ret=blackjack.score([3,12])
        self.assertEqual(ret,(13,0))

    #[ 5, 5, 10 ] → (20, 0)
    def testplainTriple(self):
        ret=blackjack.score([5,5,10])
        self.assertEqual(ret,(20,0))

    #[ 11, 10, 1 ] → (21, 0)
    def testoneAce(self):
        ret=blackjack.score([11,10,1])
        self.assertEqual(ret,(21,0))

    #[ 1, 5 ] → (16, 1)
    def testsoftPair(self):
        ret=blackjack.score([1,5])
        self.assertEqual(ret,(16,1))

    #[ 1, 1, 5 ] → (17, 1)
    def testsoftTriple(self):
        ret=blackjack.score([1,1,5])
        self.assertEqual(ret,(17,1))

        #[ 1, 1, 1, 7 ] → (20, 1)
    def testsoft4(self):
        ret=blackjack.score([1,1,1,7])
        self.assertEqual(ret,(20,1))

    #[ 7, 8, 10 ] → (25, 0)
    def testbustTriple(self):
        ret=blackjack.score([7,8,10])
        self.assertEqual(ret,(25,0))


class testStand(unittest.TestCase):

        def testplainPairover(self):
            self.assertTrue=(blackjack.stand(18,True,[10,12]))

        def testplainPairOver2(self):
            self.assertTrue=(blackjack.stand(18,False,[10,12]))

        def testplainPairUnder(self):
            self.assertFalse=(blackjack.stand(18,False,[3,12]))

        def testplainPairUnder2(self):
            self.assertFalse=(blackjack.stand(18,True,[3,12]))

        def testsoftTie1(self):
            self.assertFalse=(blackjack.stand(18,False,[1,7]))

        def testsoftTie2(self):
            self.assertTrue=(blackjack.stand(18,True,[1,7]))
