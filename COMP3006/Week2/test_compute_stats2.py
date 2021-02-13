import unittest

import compute_stats2
from compute_stats2 import *




class testStats(unittest.TestCase):

    def testNone(self):
        ret=compute_stats2.compute_stats(None)
        self.assertIsNone(ret)

    def testEmpty(self):
        ret=compute_stats2.compute_stats([])
        self.assertIsNone(ret)

    def testSingleton(self):
        ret=compute_stats2.compute_stats([7])
        self.assertAlmostEqual(ret,(7,7,7.0,7.0))

    def testOddLength(self):
        ret=compute_stats2.compute_stats([1,3,10,12,14])
        self.assertAlmostEqual(ret,(1,14,8.0,10.0))

    def testEvenLength(self):
        ret=compute_stats2.compute_stats([1,3,4,12])
        self.assertAlmostEqual(ret,(1,12,5.0,3.5))
