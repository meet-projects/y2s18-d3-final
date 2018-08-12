from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

###########################################user
class User(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key = True)
    name = Column(String)
    passward = Column(Integer)
    skills = Column(String)


    def __repr__(self):
        return ("User name: {},\n"
        	"User passward:{}\n"
        	"User skills".format(
        		self.name,
        		self.passward,
        		self.skills ))

#########################################comment

class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key = True)
    comment_content = Column(String)


    def __repr__(self):
        return ("comment content: {}".format(
        		self.comment))

###########################################post

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key = True)
    post_name = Column(String)


    def __repr__(self):
        return ("post_name: {}".format(
        		self.post))


