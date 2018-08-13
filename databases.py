# Database related imports
# Make sure to import your tables!
from model import Base, User, Post

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# You can change the name of your database, just change project.db to whatever you want (make sure to include .db at the end!)
# Make sure you have the same name for the database in the app.py file!
engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Your database functions are located under here (querying, adding items, etc.)

# Example of adding a student:
def add_User(username, password, user_skills):
    user_object = User(name=username,
     password=password,
     skills= user_skills)
    session.add(user_object)
    session.commit()

def query_all_users():
    users = session.query(
    	User).all()
    return users

def query_user_by_name(username):
	name = session.query(
		User).filter_by(name=username).first()
	return name

def delete_user_by_id(user_id):
    post = session.query(User).filter_by(id_table=user_id).delete()
    session.commit()

def delete_all_users():
    session.query(User).delete()
    session.commit

def add_Post(post_string):
    post_object = Post(post_string=post_string)
    session.add(post_object)
    session.commit()

def query_all_posts():
    posts = session.query(
        Post).all()
    return posts

def query_post_by_id(post_id):
    post = session.query(Post).filter_by(id_table=post_id).first()
    return post

def delete_all_posts():
    session.query(Post).delete()
    session.commit


def delete_post_by_id(post_id):
    post = session.query(Post).filter_by(id_table=post_id).delete()
    session.commit()


