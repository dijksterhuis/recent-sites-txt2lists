from flask import Flask, url_for, request, render_template
from get_links_from_txt_files import get_data
#TODO from requests import get

app = Flask(__name__)

@app.route('/index')
def index():
	d = get_data()
	categories = [ k for k in d.keys() ]
	return render_template('index.html',data_dict=d, cats=categories)

if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True,port=100)
