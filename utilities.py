#!/usr/bin/env python

import pandas as pd
import numpy as np


def get_products_filtered(categories=None):
	df = pd.read_csv('data/Products.csv')
	if categories is not None:
		for category in categories.keys():
			df = df[df[category] == categories[category]]

	''' SQL '''
	return df.to_dict('records')

def get_products_search(values):
	df = pd.read_csv('data/Products.csv')
	df = df[df.isin(values).any(1)]
	''' SQL '''

	return df.to_dict('records')

def get_products_ids(ids):
	df = pd.read_csv('data/Products.csv')
	df = df.loc[df['id'].isin(ids)]
	''' SQL '''

	return df.to_dict('records')

def get_categories():
	df = pd.read_csv('data/Products.csv')
	genders = df['gender'].unique()
	types = [df[(df['gender'] == genders[0])]['type'].unique().tolist(), df[(df['gender'] == genders[1])]['type'].unique().tolist()]
	children = [[{'url': '', 'name': name} for name in types[0]],[{'url': '', 'name': name} for name in types[1]]]

	result = [{'title' : genders[0], 'children': children[0]}, {'title': genders[1], 'children': children[1]}]
	return result

def get_subcategories(gender, category):
	df = pd.read_csv('data/Products.csv')

	types = df[(df['gender'] == gender) & (df['type'] == category)]['subtype'].unique().tolist()

	children = [{'url': '', 'name': name} for name in types]

	result = [{'gender' : gender, 'category': category, 'children': children}]
	return result

def main():

	test = get_products_filtered({'color': 'Red', 'brand': 'WESC', 'price': 1599, 'size': 'XS'})

	test = get_products_filtered({'type': 'Bags', 'subtype': 'Leather bag'})

	test = get_products_search(['Red', 'Jack and Jones'])

	print(get_categories())
	#print(get_subcategories('Female', 'Bags'))


if __name__ == '__main__':
	main()
