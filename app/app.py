#/usr/bin/env python

from flask import Flask, url_for, request, render_template
from get_links_from_txt_files import get_data
import redis

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
	app.run(host='0.0.0.0',debug=True,port=100)
