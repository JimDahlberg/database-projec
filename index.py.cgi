#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os, sys, inspect

# Import modules for CGI handling
import cgi, cgitb


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


def products(limits):
    template = env.get_template('products.html')
    try:
        print template.render(title='BestBuy', products=[
            {'brand': 'brand', 'name': 'Name', 'size': 'XXXL', 'price': 2323, 'color': "red"},
            {'brand': 'brand', 'name': 'Name', 'size': 'XL', 'price': 2323, 'color': "red"},
        ])
    except Exception as e:
        print e


def categories(limits):
    template = env.get_template('categories.html')
    try:
        print template.render(title='BestBuy', categories=[
            {'title': 'Herr', 'children': [
                {'url': '', 'name': 'Herr kalsong'},
                {'url': '', 'name': 'Herr Troja'}
            ]},
            {'title': 'Dam', 'children': [
                {'url': '', 'name': 'Dam vaska'},
                {'url': '', 'name': 'Dam troja'}
            ]}
        ])
    except Exception as e:
        print e


def cart(items):
    template = env.get_template('cart.html')
    try:
        print template.render(title='BestBuy (cart)', cart=[
            {'brand': 'brand', 'name': 'Name', 'size': 'XXXL', 'price': 2323, 'color': "red"},
            {'brand': 'brand', 'name': 'Name', 'size': 'XL', 'price': 2323, 'color': "red"},
        ])
    except Exception as e:
        print e


# Create instance of FieldStorage
form = cgi.FieldStorage()


action = form.getvalue('action')

if action == 'category':
    categories("")
elif action == 'cart':
    cart("")
else:
    products("")
