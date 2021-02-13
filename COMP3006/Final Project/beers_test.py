import unittest

import beers
from beers import *

class test_beer_list(unittest.TestCase):

    def teststr(self):
        brew = Beer(29,38,"Stout",4.4)
        self.assertEqual(brew.__str__(),"Beer(beer_id=29, brewery_id=38, style='Stout', abv=4.4)")

    def testrepr(self):
        brew2=Beer(29,38,"Stout",4.4)
        self.assertEqual(brew2.__repr__(),"Beer(beer_id=29, brewery_id=38, style='Stout', abv=4.4)")

    def test_beer_cleanup(self):
        ret=BeerList.cleanup_beer_type(self,"Pale dirt lawn mower wheaties elbow")
        self.assertEqual(ret,"Pale Wheat Ale")

    def test_beer_cleanup2(self):
        ret = BeerList.cleanup_beer_type(self,"may the Schwarz be with you")
        self.assertEqual(ret,"Dark Seasonal")

    def test_beer_cleanup3(self):
        ret = BeerList.cleanup_beer_type(self,"IpAd 10")
        self.assertEqual(ret,"IPA")

    def test_beer_cleanup4(self):
        ret = BeerList.cleanup_beer_type(self,"Hefeweizen")
        self.assertEqual(ret,"Wheat Beer")

    def test_beer_cleanup5(self):
        ret = BeerList.cleanup_beer_type(self,"Pale Ale")
        self.assertEqual(ret,"General Ales")

    def test_beer_cleanup6(self):
        ret = BeerList.cleanup_beer_type(self,"Wir sollen das Bier lagern")
        self.assertEqual(ret,"Lager")

    def test_beer_cleanup7(self):
        ret = BeerList.cleanup_beer_type(self,"Muenchner Pilsener")
        self.assertEqual(ret,"Pilsner")

    def test_beer_cleanup8(self):
        ret = BeerList.cleanup_beer_type(self,"bestoutfielder")
        self.assertEqual(ret,"Stout")

    def test_beer_cleanup9(self):
        ret = BeerList.cleanup_beer_type(self,"French fries & a porterhouse steak!")
        self.assertEqual(ret,"Porter")

    def test_beer_cleanup10(self):
        ret = BeerList.cleanup_beer_type(self,"Ciderhouse Rules")
        self.assertEqual(ret,"Cider")

    def test_beer_cleanup11(self):
        ret = BeerList.cleanup_beer_type(self,"Barney, where's my fruity pebbles?")
        self.assertEqual(ret,"Fruit or Vegetable")

    def test_beer_cleanup12(self):
        ret = BeerList.cleanup_beer_type(self,"Roggenstoff")
        self.assertEqual(ret,"Rye Beer")

    def test_beer_cleanup13(self):
        ret = BeerList.cleanup_beer_type(self,"Nesbitt")
        self.assertEqual(ret,"ESB")

    def test_beer_cleanup14(self):
        ret = BeerList.cleanup_beer_type(self,"Realschule")
        self.assertEqual(ret,"Kolsch")

    def test_beer_cleanup15(self):
        ret = BeerList.cleanup_beer_type(self,"Mead Notebooks")
        self.assertEqual(ret,"Herbed / Mead")

    def test_beer_cleanup16(self):
        ret = BeerList.cleanup_beer_type(self,"Flibbedy Flobbedy")
        self.assertIsNone(ret)

class file_clean(unittest.TestCase):

    def test_first_row(self):
        ret = not_first_row(["derelict","pegleg","kickstand","id"])
        self.assertFalse(ret,"id")

    def test_other_rows(self):
        ret= not_first_row(["derelict","pegleg","kickstand","lard"])
        self.assertTrue(ret,"id")

    def test_not_empty(self):
        ret = abv_not_empty([1,"", 5,7,8])
        self.assertFalse(ret,"")

    def test_empty(self):
        ret = abv_not_empty([1,".05", 5,7,8])
        self.assertTrue(ret,"")
