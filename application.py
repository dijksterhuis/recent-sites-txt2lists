from flask import Flask, url_for, request, render_template
from get_links_from_txt_files import get_data

#TODO from requests import get
# -- get site name etc.

application = Flask(__name__)

@application.route('/')
def index():
    d = get_data()
    categories = [ k for k in d.keys() ]
    if len(categories) >= 1: return render_template('list.html',data_dict=d, cats=categories) 
    else: return render_template('empty.html')

@application.route('/add-one')
def add_one():
    return render_template('empty.html')

@application.route('/add-many')
def add_many():
    return render_template('empty.html')

@application.route('/edit')
def edit():
    return render_template('empty.html')

if __name__ == '__main__':
    application.debug = True
    application.run()
