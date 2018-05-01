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
	''' SQL '''

	result = [{'title' : genders[0], 'children': children[0]}, {'title': genders[1], 'children': children[1]}]
	return result

def get_subcategories(gender, category):
	df = pd.read_csv('data/Products.csv')
	types = df[(df['gender'] == gender) & (df['type'] == category)]['subtype'].unique().tolist()
	children = [{'url': '', 'name': name} for name in types]
	result = [{'gender' : gender, 'category': category, 'children': children}]
	''' SQL '''

	return result

def write_order(order):
	df = pd.read_csv('data/Orders.csv')
	# Get new order ID
	orderID = df['orderid'].max() + 1

	# Get the name and so on for the customer.
	#firstname = order['name']
	#lastname = order['name']
	firstname, lastname = order['name'].split()
	email = order['email']
	address = order['address']
	zipcode = order['zipcode']
	town = order['town']
	# write line by line for each item
	for item in order['items']:
		df.iloc[-1] = [	orderID, firstname, lastname, address, town, zipcode, item['id'], item['brand'], 
						item['type'], item['subtype'], item['color'], item['gender'], item['price'], item['size'], item['amount']]
	df.to_csv('data/NewOrders.csv')

def get_20_most_popular():
	# Group by article # and sum of amount in Orders.
	# grab the top 20 from Products and return as dict
	df = pd.read_csv('data/Orders.csv')
	top20_ids = df.groupby(['id']).sum().loc[:,['amount']].sort_values('amount', ascending=False).iloc[:20].index.tolist()
	df = pd.read_csv('data/Products.csv')

	return df.iloc[top20_ids,:].to_dict('records')


def main():

	#test = get_products_filtered({'color': 'Red', 'brand': 'WESC', 'price': 1599, 'size': 'XS'})
	#test = get_products_filtered({'type': 'Bags', 'subtype': 'Leather bag'})
	#test = get_products_search(['Red', 'Jack and Jones'])
	#write_order('test')
	#print(get_categories())
	#print(get_subcategories('Female', 'Bags'))
	#print(get_20_most_popular())
	


if __name__ == '__main__':
	main()
