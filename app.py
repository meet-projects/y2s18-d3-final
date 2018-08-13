
from flask import Flask, render_template, url_for, redirect, request, session as flask_session
from flask.ext.session import Session
from databases import *

# Starting the flask app
app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# App routing code here
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/log-in', methods=['GET','POST'])
def log_in():
	if request.method == 'POST':
		name = request.form['uname']
		password = request.form['psw']
		user = query_by_name_and_password(name, password)
		print(user)
		if user is not None and user.password == password:
			flask_session['user_id'] = user.id_table
			return redirect(url_for('home'))
		else :
			return render_template('log_in.html')
	else:		
		return render_template('log_in.html')

@app.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
	if request.method == 'POST':
		name = request.form['username'] 
		password = request.form['psw']
		add_User(name,password)
		return redirect(url_for('home'))

	else:
		return render_template('sign_up.html')


# Running the Flask app
if __name__ == "__main__":
    app.run(debug=True)



   #psot request , 