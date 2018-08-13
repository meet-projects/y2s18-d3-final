from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

###########################################user
class User(Base):
<<<<<<< HEAD
    __tablename__ = "User"
    id_table = Column(Integer, primary_key = True)
=======
    __tablename__ = "Users"
    id = Column(Integer, primary_key = True)
>>>>>>> 1d35a3499519230215eab0787d07380312fd17ad
    name = Column(String)
    password = Column(String)
    skills = Column(String)


    def __repr__(self):
        return ("Username: {},\n"
            "password: {}, \n"
        	"skills {} .\n").format(
        		self.name,
                self.password,
        		self.skills)

<<<<<<< HEAD
=======
#########################################comment

class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key = True)
    comment_content = Column(String)
>>>>>>> 1d35a3499519230215eab0787d07380312fd17ad

class Post(Base):
    __tablename__ = "Post"
    id_table = Column(Integer, primary_key = True)
    post_string = Column(String)

    def __repr__(self):
<<<<<<< HEAD
        return ("this post says: {}.\n").format(
                self.post_string)
=======
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


>>>>>>> 1d35a3499519230215eab0787d07380312fd17ad
