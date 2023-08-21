# Flask App Template



## Getting Started

Bringing your code to others is called **distribution**. While there are different approaches, this repository showcases a Python web application using Flask.

The flask documentation can be found [here](https://flask.palletsprojects.com/en/2.3.x/)

## Installation

1. Create a virtual environment and activate it

2. Install flask (and other needed libraries) with the requirements.txt file

   ```
   pip install -r requirements.txt
   ```

3. To confirm installation, run the following line of code 

   ```
   python -c "import flask; print(flask.__version__)"
   ```

   It should return a version number.

## Running your web application

1. First, we need to define a environmental variable FLASK_APP stating the location of the web app. For this repo, the file is called hello.py, so we would use the code 

   ```
   set FLASK_APP=hello
   ```

2. Then we need to define which environment to run it, development or production. If we select development, flask will provide an interactive debugger and will reload when code is changed. It is important to note that when deploying to production, you must use production mode, not development. To set our app to development mode (for now), type the following 

   ```
   set FLASK_ENV=development
   ```

3. To run the app use the command 

   ```
   flask run
   ```

4. You should see similar output. The highlighted URL is where your flask app is hosted. Once you type in that URL you should see 'Hello, World!'

![](C:\Users\Kat.Sullivan\flask-test\images\tempsnip.png)



## Adding HTML and CSS to your Flask App

1. Take a look at the files app.py, templates/index_basic.html and static/css/style.css. 

2. Change the flask app from hello.py to app.py by 

   ```
   set FLASK_APP=app
   ```

3. Run the app with 

   ```
   flask run
   ```

   

## Adding Output from Python Script to your Flask App

1. We will be reusing old Spotify code for this example. Take a look at spotify.py. You will need a file called spotify_keys.json with your Spotify credentials for this example to work. Note the output is wrapped in a function called get_tracks()

2. Look at the file app_output.py. We import our spotify.py file so we have access to the get_tracks() function. 

3. Take a look at templates/index_output.html We can use the variable we set up in app_output.py to build out a HTML table.

4. Change the flask app to app_output.py by 

   ```
   set FLASK_APP=app_output
   ```

5. Run the app with 

   ```
   flask run
   ```

   

## Adding Input from HTML to your Python Script

1. Take a look at templates/index_input_output.html. We are adding a form that will allow the user to input a year and receive the top tracks for that year. 

2. Inside the spotify_input.py file, we modified the get_tracks function to take an argument, *year*. So we are passing the input value from the HTML file's form, to the view function in app_input_output.py to the function get_tracks

3. Change the flask app to app_input_output.py by 

   ```
   set FLASK_APP=app_input_output
   ```

4. Run the app with 

   ```
   flask run
   ```

   

## Accessing your Flask App on your Mobile Device
You can access a Flask App from any other device that is on the same network.

1. Make sure your computer running the flask app and mobile device are on the same network

2. You will need to make sure your computer has this network marked as 'Private', not 'Public'

3. Check the ip address of your computer

4. Run the app with this additional argument 

   ```
   flask run -h xxx.xxx.x.xxx
   ```

   Where the xs represent the ip address of your computer

5. Now you can open a new browser on your mobile and use the URL xxx.xxx.x.xxx:5000
