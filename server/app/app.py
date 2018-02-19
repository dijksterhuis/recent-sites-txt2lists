#!/usr/bin/env python

from flask import Flask, url_for, request, render_template
from get_links_from_txt_files import get_data
from argparse import ArgumentParser as ArgParser
import pymongo

#TODO from requests import get
# -- get site name etc.

app = Flask(__name__)

@app.route('/')
def index():
    d = get_data()
    categories = [ k for k in d.keys() ]
    return render_template('list.html',data_dict=d, cats=categories)

@app.route('/add-one')
def add_one():
    return('empty.html')

@app.route('/add-many')
def add_many():
    return('empty.html')

@app.route('/edit')
def edit():
    return('empty.html')

if __name__ == '__main__':
    
    parser = ArgParser(description='Flask app.')
    
    parser.add_argument('--port', type=int, default=100, help='<O> Integer value of Port (default: 100).')
    parser.add_argument('--host', type=str, default='0.0.0.0', help='<O> String value of Host (default: 0.0.0.0).')
    parser.add_argument('--debug', action='store_true', default='0.0.0.0', help='<O> String value of Host (default: 0.0.0.0).')
    parser.add_argument('--mongo_host', type=str, default='mongo', help='<O> String value of Mongo docker container name (default: mongo).')
    parser.add_argument('--mongo_port', type=str, default=27017, help='<O> Int value of Mongo docker container port (default: 27017).')
    
    args = parser.parse_args()
    
    global mongo_host, mongo_port
    mongo_host, mongo_port = args.mongo_host, args.mongo_port
    
    app.run(host=args.host, debug=args.debug, port=args.port)
