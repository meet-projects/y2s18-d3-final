# Database related imports
# Make sure to import your tables!
from model import Base, Student

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# You can change the name of your database, just change project.db to whatever you want (make sure to include .db at the end!)
# Make sure you have the same name for the database in the app.py file!
engine = create_engine('sqlite:///project.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Your database functions are located under here (querying, adding items, etc.)

# Example of adding a student:
def add_User(user_name, user_passward, user_skills):
    print("Added a user!")
    user = User(name=user_name,
     passward=user_passward,
     skills= user_skills)
    session.add(user)
    session.commit()

def get_all_Users():
    users = session.query(
    	User).all()
    return get_all_Users

def get_User_by_name():
	user = session.query(
		User).filter_by(name=user_name).first()
	return user