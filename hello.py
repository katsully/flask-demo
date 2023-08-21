# import the Flask object from the flask library
from flask import Flask

# create a Flask application with the name app
# __name__ is a recognized python variable that holds the name of the current Python module
# we need to know the current python module because Flask will get set up inside a 
# different directory so we need to know the location of this one
app = Flask(__name__)

# / is the main URL (ie localhost:8000)
@app.route('/')
# hello() is defined as a view function
# it returns the string Hello, World!
def hello():
	# this returns a HTTP response
	return "Hello, World"