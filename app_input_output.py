# render_template() is a helper function that lets you render
# HTML template files that exist in the templates folder
from flask import Flask, render_template, request
# bring in the python code
from spotify_input import get_tracks

app = Flask(__name__, '/static')
# add a debugger
app.config["DEBUG"] = True

# give a default year since the get_tracks function now requires a year argument
year='2021'

# when you go to the main url, it will render the index.html
# that lives inside the templates folder
@app.route('/')
def index():
	songs = get_tracks(year)
	return render_template('index_input_output.html', songs=songs, year=year)

@app.route('/', methods = ['POST'])
def index_post():
	year = request.form['year']
	songs = get_tracks(year)
	return render_template('index_input_output.html', songs=songs, year=year)
		