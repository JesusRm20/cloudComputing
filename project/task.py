import json
import requests
#from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, String, Date, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///cloudCompProject.db")
session = sessionmaker(bind=engine)()
Base = declarative_base()

class users(Base):
    __tablename__ = "users"
    _id = Column(Integer, primary_key = True)
    username = Column(String(100))
    password = Column(String(100))

    def __ini__(self, _id, username, password):
        self._id = _id
	self.username = username
	self.password = password
user = users(1, "Jesus", "JR2019")
session.add(user)
session.commit()



# crime_url_template = 'https://data.police.uk/api/crimes-street/all-crime?lat={lat}&lng={lng}&date={data}'
# crimeoutcome_url_template = 'https://data.police.uk/api/crimes-street/outcomes-for-crime?id={id}'
# categories_url_template = 'https://data.police.uk/api/crime-categories?date={date}'

# my_latitude = '51.52369'
# my_longitude = '-0.0395857'
# my_date = '2018-11'
# crime_url = crime_url_template.format(lat = my_latitude, lng = my_longitude, data = my_date)
# resp = requests.get(crime_url)

# for r in resp:
#     print(r[1], r[2])
