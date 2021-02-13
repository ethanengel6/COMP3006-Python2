# Ethan Engel
# COMP 3006
# Final Project - Individual Module
import argparse
import csv
import logging
from collections import namedtuple

import matplotlib.pyplot as plt
import numpy as np

Beer = namedtuple('Beer', ['beer_id', 'brewery_id', 'style', 'abv'])
beer_types = [
	"Pale Wheat Ale",
	"Dark Seasonal",
	"IPA",
	"Wheat Beer",
	"General Ales",
	"Pilsner",
	"Lager",
	"Stout",
	"Porter",
	"Cider",
	"Fruit or Vegetable",
	"Rye Beer",
	"ESB",
	"Kolsch",
	"Herbed / Mead"
]


class BeerList:
	def __init__(self):
		with open('beers.csv', 'r') as f:
			read = csv.reader(f)
			list_of_beers = []
			for row in read:
				if not_first_row(row) and abv_not_empty(row):
					row[5] = self.cleanup_beer_type(row[5])
					list_of_beers.append(row)
		logging.debug("CSV Successfully opened.")
		beers = []
		for beer in list_of_beers:
			if beer[5] is not None:
				beers.append(Beer(beer_id=int(beer[3]),
				                  brewery_id=int(beer[6]),
				                  style=beer[5],
				                  abv=round(float(beer[1]), 3)))
		self.beers = beers

	def __repr__(self):
		return self.beers

	def __str__(self):
		return str(self.__repr__())

	def cleanup_beer_type(self, dirty_beer_name):
		dirty_beer_name = dirty_beer_name.lower()
		if "pale" in dirty_beer_name and "wheat" in dirty_beer_name:
			clean_beer_name = "Pale Wheat Ale"
		elif (
				"scotch" in dirty_beer_name and "ale" in dirty_beer_name) or "schwarz" in dirty_beer_name or \
				"dubbel" in dirty_beer_name or "winter" in dirty_beer_name or "quadrupel" in dirty_beer_name or \
				"bock" \
				in dirty_beer_name:
			clean_beer_name = "Dark Seasonal"
		elif "ipa" in dirty_beer_name:
			clean_beer_name = "IPA"
		elif "weizen" in dirty_beer_name or "weiss" in dirty_beer_name or "wheat" in dirty_beer_name or "witbier" in \
				dirty_beer_name or "gose" in dirty_beer_name:
			clean_beer_name = "Wheat Beer"
		elif (
				"wheat" not in dirty_beer_name and "scotch" not in dirty_beer_name and "pumpkin" not in
				dirty_beer_name) and (
				"ale" in dirty_beer_name or "tripel" in dirty_beer_name):
			clean_beer_name = "General Ales"
		elif "altbier" in dirty_beer_name or "lager" in dirty_beer_name:
			clean_beer_name = "Lager"
		elif "pilsner" in dirty_beer_name or "pilsener" in dirty_beer_name:
			clean_beer_name = "Pilsner"
		elif "stout" in dirty_beer_name:
			clean_beer_name = "Stout"
		elif "porter" in dirty_beer_name:
			clean_beer_name = "Porter"
		elif "cider" in dirty_beer_name:
			clean_beer_name = "Cider"
		elif "fruit" in dirty_beer_name or "pumpkin" in dirty_beer_name:
			clean_beer_name = "Fruit or Vegetable"
		elif "rye" in dirty_beer_name or "roggen" in dirty_beer_name:
			clean_beer_name = "Rye Beer"
		elif "esb" in dirty_beer_name:
			clean_beer_name = "ESB"
		elif "lsch" in dirty_beer_name:
			clean_beer_name = "Kolsch"
		elif "mead" in dirty_beer_name or "herbed" in dirty_beer_name:
			clean_beer_name = "Herbed / Mead"
		else:
			return None
		return clean_beer_name


def main():
	logger = logging.getLogger()
	logger.setLevel(logging.INFO)

	parser = argparse.ArgumentParser('Outputting beer data with several sort options.')
	parser.add_argument('-o', '--ofile', dest='outfile', action='store', metavar='<outfile>',
	                    help='If this command is executed, output is written to user specified file (CSV), '
	                         'rather than '
	                         'standard output.')
	parser.add_argument('-p', dest='plot',
	                    type=int,
	                    help='If a beer type is specified, a histogram of abv values are generated for that type.  '
	                         'Options are: 1)Pale Wheat Ale 2)Dark Seasonal 3)IPA 4)Wheat Beer 5)General Ales 6)Lager '
	                         '7)Pilsner 8)Stout 9)Porter 10)Cider 11)Fruit,Vegetable or Pumpkin Ale 12)Rye 13)ESB '
	                         '14)Kolsch 15)Herbed incl. Mead')
	args = parser.parse_args()

	beers = BeerList()

	if args.outfile is None:
		print(beers)
	else:
		write_to_csv(args, beers.beers)

	if args.plot is not None:
		plot_beer_type_histogram(args, beers.beers)


def not_first_row(row):
	return row[3] != 'id'


def abv_not_empty(beer):
	return beer[1] != ""


def write_to_csv(args, beers):
	with open(args.outfile, 'w', newline="") as ff:
		onwax = csv.writer(ff)
		onwax.writerow(['beer_id', 'brewery_id', 'style', 'abv'])
		for beer in beers:
			onwax.writerow(beer)


def plot_beer_type_histogram(args, list_of_beers):
	beer_type_index = args.plot - 1
	brewarray = []
	for beer in list_of_beers:
		beer_style = beer.style
		if beer_types[beer_type_index] == beer_style:
			brewarray.append(float(beer.abv))
	plt.hist(brewarray)
	plt.title("ABV value distribution for " + beer_types[beer_type_index])
	plt.show()


if __name__ == '__main__':
	main()
