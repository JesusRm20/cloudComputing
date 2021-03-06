import requests
from passwordHash import hashPassword
from sqlalchemy import create_engine, Column, String, Date, Integer, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import date
import passwordHash

Base = declarative_base()

engine = create_engine("postgresql://postgres:password@172.17.0.2/cloudComputing")
session = sessionmaker(bind=engine)()

class users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    lastname = Column(String)
    email = Column(String)
    username = Column(String)
    password = Column(String)
    date = Column(String)

    def __repr__(self):
        return "<users(name='%s', lastname='%s', email='%s', username='%s', password='%s', date='%s')>" % (
                               self.name, self.lastname, self.email, self.username, self.password, self.date)


def addUser(obj):
    pwd = passwordHash.hashPassword(obj['password'])
    date1 = date.today().strftime('%d/%m/%Y')
    usr = users(name=obj['firstName'],lastname=obj['lastName'], email=obj['email'], username=obj['username'], password=pwd,date=date1)
    session.add(usr)
    session.commit()

    return pwd

def verUser(usr):
    result = session.query(users.password).filter_by(username=usr).first()
    
    return '' if result == None else result.password

def updateUsr(id1, obj):
    usr = session.query(users).filter_by(id=id1).first()
    usr.username = obj
    session.commit()
    return True
