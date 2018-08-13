
from flask import Flask, render_template, url_for, redirect, request, session

from databases import add_User, query_all_users ,add_Post,query_all_posts

# Starting the flask app
app = Flask(__name__)

# App routing code here
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/log-in')
def log_in():
	return render_template('log_in.html')

@app.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
	if request.method == 'POST':
		return render_template('home.html')
	else:
		return render_template('sign_up.html')
# Running the Flask app
if __name__ == "__main__":
    app.run(debug=True)



   #psot request , 