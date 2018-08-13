
from flask import Flask, render_template, url_for, redirect, request, session
<<<<<<< HEAD
from databases import add_User, query_all_users ,add_Post,query_all_posts
=======

# Add functions you need from databases.py to the next line!
from databases import add_User, get_all_Users
>>>>>>> 1d35a3499519230215eab0787d07380312fd17ad

# Starting the flask app
app = Flask(__name__)

# App routing code here
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/log-in')
def log_in():
	return render_template('log_in.html')

@app.route('/sign-up')
def sign_up():
	return render_template('sign_up.html')
	
# Running the Flask app
if __name__ == "__main__":
    app.run(debug=True)
