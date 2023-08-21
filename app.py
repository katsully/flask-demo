# render_template() is a helper function that lets you render
# HTML template files that exist in the templates folder
from flask import Flask, render_template

app = Flask(__name__)

# when you go to the main url, it will render the index.html
# that lives inside the templates folder
@app.route('/')
def index():
	return render_template('index_basic.html')