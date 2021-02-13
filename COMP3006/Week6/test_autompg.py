import unittest

import autompg
from autompg import *

class testautoMPG(unittest.TestCase):

    def teststr(self):
        hooptie=AutoMPG("Ford","Pinto",1978,3.4)
        self.assertEqual(hooptie.__str__(),"AutoMPG(Ford,Pinto,1978,3.4)")

    def testrepr(self):
        hooptie=AutoMPG("Ford","Pinto",1978,3.4)
        self.assertEqual(hooptie.__repr__(),"{make:Ford, model:Pinto, year:1978, mpg:3.4}")

    def testeq(self):
        hooptie=AutoMPG("Ford","Pinto",1978,3.4)
        hooptie2=AutoMPG("Ford","Pinto",1978,3.5)
        hooptie3=AutoMPG("Chevy","Elcamino",1978,3.4)
        self.assertNotEqual(hooptie,hooptie2)
        self.assertNotEqual(hooptie,None)
        self.assertNotEqual(hooptie2,hooptie3)
        self.assertNotEqual(hooptie,hooptie3)
        self.assertEqual(hooptie,hooptie)

    def testlt(self):
        hooptie=AutoMPG("Ford","Pinto",1978,3.4)
        hooptie2=AutoMPG("Ford","Pinto",1978,3.5)
        hooptie3=AutoMPG("Chevy","Elcamino",1978,3.4)
        self.assertLess(hooptie,hooptie2)
        self.assertLess(hooptie3,hooptie2)
        self.assertLess(hooptie3,hooptie)

    def testhash(self):
        hooptie=AutoMPG("Ford","Pinto",1978,3.4)
        self.assertIsNotNone(hash(hooptie))
