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

<<<<<<< HEAD
# Example of adding a student:
def add_User(username, password, user_skills):
    user_object = User(name=username,
     password=password,
=======
# Example of adding a user:
def add_User(user_name, user_passward, user_skills):
    print("Added a user!")
    user = User(name=user_name,
     passward=user_passward,
>>>>>>> 1d35a3499519230215eab0787d07380312fd17ad
     skills= user_skills)
    session.add(user_object)
    session.commit()
<<<<<<< HEAD

def query_all_users():
=======
###########################################user
def get_all_Users():
>>>>>>> 1d35a3499519230215eab0787d07380312fd17ad
    users = session.query(
    	User).all()
    return users

<<<<<<< HEAD
def query_user_by_name(username):
	name = session.query(
		User).filter_by(name=username).first()
	return name

def delete_user_by_id(user_id):
    post = session.query(User).filter_by(id_table=user_id).delete()
=======
def get_User_by_name():
	user = session.query(
		User).filter_by(name=user_name).first()
	return user
############################################comment
def add_Comment(comment_content):
    print("Added a comment!")
    comment = Cumment(comment=comment_content,)
    session.add(comment)
>>>>>>> 1d35a3499519230215eab0787d07380312fd17ad
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


<<<<<<< HEAD
=======
def get_all_Comments():
    comment = session.query(
        Cumment).all()
    return get_all_Comments
###############################################post

def add_Post(post_name):
    print("Added a post!")
    post = Post(post=post_name,)
    session.add(post)
    session.commit()

def get_Post():
    post = session.query(
        Post).first()
    return get_Post


def get_all_Posts():
    post = session.query(
        Post).all()
    return get_all_Posts



#add_User("mousa","pass","reuning")
#print(get_all_Users())
>>>>>>> 1d35a3499519230215eab0787d07380312fd17ad
