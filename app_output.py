# render_template() is a helper function that lets you render
# HTML template files that exist in the templates folder
from flask import Flask, render_template
# bring in the python code
from spotify import get_tracks

app = Flask(__name__)
# add a debugger
app.config["DEBUG"] = True

# when you go to the main url, it will render the index.html
# that lives inside the templates folder
@app.route('/')
def index():
	songs = get_tracks()
	return render_template('index_output.html', songs = songs)