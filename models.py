from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///IssueTracker.db')


#creating the users table
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    fullname = Column(String)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    is_admin = Column(Boolean, default=False)

def create_database(self):
        Base.metadata.create_all(engine)
