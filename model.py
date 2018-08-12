from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Place your database schema code here

# Example code:
class User(Base):
    __tablename__ = "users"
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