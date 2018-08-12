
from flask import Flask, render_template, url_for, redirect, request, session

# Add functions you need from databases.py to the next line!
from databases import add_student, get_all_students

# Starting the flask app
app = Flask(__name__)

# App routing code here
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/log-in')
def log_in():
	return render_template('log_in.html')

@app.route('/user/<int:user_id>')
def display_user(user_id,user):
    return render_template('user.html', user_id=user_id,user=query_by_id(user_id))

# Running the Flask app
if __name__ == "__main__":
    app.run(debug=True)
