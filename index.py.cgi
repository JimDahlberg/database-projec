#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os, sys, inspect

# Import modules for CGI handling
import cgi, cgitb

# Import our utilitiy functions
from utilities import get_products_filtered, get_products_search, get_products_ids, get_categories, get_subcategories

print "Content-Type: text/html; charset=UTF-8\n"

# realpath() will make your script run, even if you symlink it :)
cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0]))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)


from jinja2 import Environment, FileSystemLoader, select_autoescape
env = Environment(
    loader=FileSystemLoader(os.path.join(cmd_folder, 'templates')),
    autoescape=select_autoescape(['html', 'xml'])
)


def products(limits, filters=None):
    template = env.get_template('products.html')
    data = get_products_filtered(filters)
    # Limit the length of the output to 20, otherwise its horrendous.
    if len(data) > 20:
        data = data[:20]
    try:
        #print template.render(title='BestBuy', products=[
        #    {'brand': 'brand', 'name': 'Name', 'size': 'XXXL', 'price': 2323, 'color': "red"},
        #    {'brand': 'brand', 'name': 'Name', 'size': 'XL', 'price': 2323, 'color': "red"},
        #])
        print template.render(title='BestBuy', products=data)
    except Exception as e:
        print e


def categories(limits):
    template = env.get_template('categories.html')
    data = get_categories()

    try:
        #print template.render(title='BestBuy', categories=[
        #    {'title': 'Heasasdasdasdasdrr', 'children': [
        #        {'url': '', 'name': 'Herr kalsong'},
        #        {'url': '', 'name': 'Herr Troja'}
        #    ]},
        #    {'title': 'Dam', 'children': [
        #        {'url': '', 'name': 'Dam vaska'},
        #        {'url': '', 'name': 'Dam troja'}
        #    ]}
        #])
			  print template.render(title='BestBuy', categories=data)
    except Exception as e:
        print e

# Need to do same thing as above but for subcategories. call the get_subcategories() function with gender and main category as parameters
def subcategories(limits, gender, category):
    template = env.get_template('subcategories.html')
    data = get_subcategories(gender, category)

    try:
        print template.render(title='BestBuy', categories=data)
    except Exception as e:
        print e


def cart():
    from os import environ
    cart = []
    try:
        if 'HTTP_COOKIE' in environ:
            for cookie in [x.strip() for x in environ['HTTP_COOKIE'].split(';')]:
                (key, value) = cookie.split('=')
                if key == "cart":
                    value = map(int, value.strip("[]").split("%2C"))
                    cart = get_products_ids(value)
        template = env.get_template('cart.html')
        print template.render(title='BestBuy (cart)', cart=cart, price=23)
        """print template.render(title='BestBuy (cart)', cart=[
            {'brand': 'brand', 'name': 'Name', 'size': 'XXXL', 'price': 2323, 'color': "red"},
            {'brand': 'brand', 'name': 'Name', 'size': 'XL', 'price': 2323, 'color': "red"},
        ])"""
    except Exception as e:
        print e


def checkout():
    try:
        order = {'email': form.getvalue('email'),
            'name': form.getvalue('name'), 'address': form.getvalue('address'),
            'zipcode': form.getvalue('zipcode'), 'town': form.getvalue('town'),
            'items': form.getvalue('items')}
        #print order
        template = env.get_template('checkout.html')
        print template.render(title='BestBuy', address=form.getvalue('address').decode('utf-8'))
    except Exception as e:
        print e


# Create instance of FieldStorage
form = cgi.FieldStorage()
action = form.getvalue('action')

if action == 'category':
    categories("")
elif action == 'cart':
    cart()
elif action == 'checkout':
    checkout()
elif action == 'subcategory':
    gender = form.getvalue('gender')
    category = form.getvalue('category')
    subcategories("", gender, category)
elif action == 'filtered_products':
    filters = {'gender': form.getvalue('gender'), 'type': form.getvalue('category'), 'subtype': form.getvalue('subcategory')}
    products("", filters)
elif action == 'search': # Not done. Not even started actually :)
    words = None
    search("", words)
else:
    products("")
