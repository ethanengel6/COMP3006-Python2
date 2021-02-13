import unittest

import blackjack2
from blackjack2 import *

class testScore(unittest.TestCase):
    #[ 3, 12 ] → (13, 0)
    def testplainPair(self):
        ret=blackjack2.score([3,12])
        self.assertEqual(ret,(13, 0))

    #[ 5, 5, 10 ] → (20, 0)
    def testplainTriple(self):
        ret=blackjack2.score([5,5,10])
        self.assertEqual(ret,(20, 0))

    #[ 11, 10, 1 ] → (21, 0)
    def testoneAce(self):
        ret=blackjack2.score([11,10,1])
        self.assertEqual(ret,(21,0))

    #[ 1, 5 ] → (16, 1)
    def testsoftPair(self):
        ret=blackjack2.score([1,5])
        self.assertEqual(ret,(16,1))

    #[ 1, 1, 5 ] → (17, 1)
    def testsoftTriple(self):
        ret=blackjack2.score([1,1,5])
        self.assertEqual(ret,(17,1))

        #[ 1, 1, 1, 7 ] → (20, 1)
    def testsoft4(self):
        ret=blackjack2.score([1,1,1,7])
        self.assertEqual(ret,(20,1))

    #[ 7, 8, 10 ] → (25, 0)
    def testbustTriple(self):
        ret=blackjack2.score([7,8,10])
        self.assertEqual(ret,(25,0))


class testStand(unittest.TestCase):

        def test13HUnder(self):
            ret=blackjack2.stand([7,5],13,False,(12,0))
            self.assertEqual=(ret,(False,12))

        def test13HSoft(self):
            ret=blackjack2.stand([2,1],13,False,(13,1))
            self.assertEqual=(ret,(False,13))

        def test13HHard(self):
            ret=blackjack2.stand([10,2,1],13,False,(13,0))
            self.assertEqual=(ret,(True,13))

        def test13SUnder(self):
            ret=blackjack2.stand([7,5],13,True,(12,0))
            self.assertEqual=(ret,(False,12))

        def test13SSoft(self):
            ret=blackjack2.stand([2,1],13,True,(13,1))
            self.assertEqual=(ret,(True,13))

        def test13SHard(self):
            ret=blackjack2.stand([10,2,1],13,True,(13,0))
            self.assertEqual=(ret,(True,13))

        def test14HUnder(self):
            ret=blackjack2.stand([8,5],14,False,(13,0))
            self.assertEqual=(ret,(False,13))

        def test14HSoft(self):
            ret=blackjack2.stand([3,1],14,False,(14,1))
            self.assertEqual=(ret,(False,14))

        def test14HHard(self):
            ret=blackjack2.stand([10,3,1],14,False,(14,0))
            self.assertEqual=(ret,(True,14))

        def test14SUnder(self):
            ret=blackjack2.stand([8,5],14,True,(13,0))
            self.assertEqual=(ret,(False,13))

        def test14SSoft(self):
            ret=blackjack2.stand([3,1],14,True,(14,1))
            self.assertEqual=(ret,(True,14))

        def test14SHard(self):
            ret=blackjack2.stand([10,3,1],14,True,(14,0))
            self.assertEqual=(ret,(True,14))

        def test15HUnder(self):
            ret=blackjack2.stand([8,6],15,False,(14,0))
            self.assertEqual=(ret,(False,14))

        def test15HSoft(self):
            ret=blackjack2.stand([4,1],15,False,(15,1))
            self.assertEqual=(ret,(False,15))

        def test15HHard(self):
            ret=blackjack2.stand([10,4,1],15,False,(15,0))
            self.assertEqual=(ret,(True,15))

        def test15SUnder(self):
            ret=blackjack2.stand([8,6],15,True,(14,0))
            self.assertEqual=(ret,(False,14))

        def test15SSoft(self):
            ret=blackjack2.stand([4,1],15,True,(15,1))
            self.assertEqual=(ret,(True,15))

        def test15SHard(self):
            ret=blackjack2.stand([10,4,1],15,True,(15,0))
            self.assertEqual=(ret,(True,15))

        def test16HUnder(self):
            ret=blackjack2.stand([9,6],16,False,(15,0))
            self.assertEqual=(ret,(False,15))

        def test16HSoft(self):
            ret=blackjack2.stand([5,1],16,False,(16,1))
            self.assertEqual=(ret,(False,16))

        def test16HHard(self):
            ret=blackjack2.stand([10,5,1],16,False,(16,0))
            self.assertEqual=(ret,(True,16))

        def test16SUnder(self):
            ret=blackjack2.stand([9,6],16,True,(15,0))
            self.assertEqual=(ret,(False,15))

        def test16SSoft(self):
            ret=blackjack2.stand([5,1],16,True,(16,1))
            self.assertEqual=(ret,(True,16))

        def test16SHard(self):
            ret=blackjack2.stand([10,5,1],16,True,(16,0))
            self.assertEqual=(ret,(True,16))

        def test17HUnder(self):
            ret=blackjack2.stand([9,7],17,False,(16,0))
            self.assertEqual=(ret,(False,16))

        def test17HSoft(self):
            ret=blackjack2.stand([6,1],17,False,(17,1))
            self.assertEqual=(ret,(False,17))

        def test17HHard(self):
            ret=blackjack2.stand([10,6,1],17,False,(17,0))
            self.assertEqual=(ret,(True,17))

        def test17SUnder(self):
            ret=blackjack2.stand([9,7],17,True,(16,0))
            self.assertEqual=(ret,(False,16))

        def test17SSoft(self):
            ret=blackjack2.stand([6,1],17,True,(17,1))
            self.assertEqual=(ret,(True,17))

        def test17SHard(self):
            ret=blackjack2.stand([10,6,1],17,True,(17,0))
            self.assertEqual=(ret,(True,17))

        def test18HUnder(self):
            ret=blackjack2.stand([9,8],18,False,(17,0))
            self.assertEqual=(ret,(False,17))

        def test18HSoft(self):
            ret=blackjack2.stand([7,1],18,False,(18,1))
            self.assertEqual=(ret,(False,18))

        def test18HHard(self):
            ret=blackjack2.stand([10,7,1],18,False,(18,0))
            self.assertEqual=(ret,(True,18))

        def test118SUnder(self):
            ret=blackjack2.stand([9,8],18,True,(17,0))
            self.assertEqual=(ret,(False,17))

        def test18SSoft(self):
            ret=blackjack2.stand([7,1],18,True,(18,1))
            self.assertEqual=(ret,(True,18))

        def test18SHard(self):
            ret=blackjack2.stand([10,7,1],18,True,(18,0))
            self.assertEqual=(ret,(True,18))

        def test19HUnder(self):
                ret=blackjack2.stand([10,8],19,False,(18,0))
                self.assertEqual=(ret,(False,18))

        def test19HSoft(self):
                ret=blackjack2.stand([8,1],19,False,(19,1))
                self.assertEqual=(ret,(False,19))

        def test19HHard(self):
                ret=blackjack2.stand([10,8,1],19,False,(19,0))
                self.assertEqual=(ret,(True,19))

        def test19SUnder(self):
            ret=blackjack2.stand([10,8],19,True,(18,0))
            self.assertEqual=(ret,(False,18))

        def test19SSoft(self):
            ret=blackjack2.stand([8,1],19,True,(19,1))
            self.assertEqual=(ret,(True,19))

        def test19SHard(self):
            ret=blackjack2.stand([10,8,1],19,True,(19,0))
            self.assertEqual=(ret,(True,19))

        def test20HUnder(self):
                ret=blackjack2.stand([10,9],20,False,(19,0))
                self.assertEqual=(ret,(False,19))

        def test20HSoft(self):
                ret=blackjack2.stand([9,1],20,False,(20,1))
                self.assertEqual=(ret,(False,20))

        def test20HHard(self):
                ret=blackjack2.stand([10,9,1],20,False,(20,0))
                self.assertEqual=(ret,(True,20))

        def test20SUnder(self):
            ret=blackjack2.stand([10,9],20,True,(19,0))
            self.assertEqual=(ret,(False,19))

        def test20SSoft(self):
            ret=blackjack2.stand([9,1],20,True,(20,1))
            self.assertEqual=(ret,(True,20))

        def test20SHard(self):
            ret=blackjack2.stand([10,9,1],20,True,(20,0))
            self.assertEqual=(ret,(True,20))
