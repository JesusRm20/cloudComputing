import json
import requests
# from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, String, Date, Integer, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///cloudCompProject.db")
session = sessionmaker(bind=engine)()

Base = declarative_base()

# class users(Base):
#     __tablename__ = "users"
#     id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
#     username = Column(String)
#     password = Column(String)

#     def __repr__(self):
#         return "<User(username='%s', password='%s')>" % (
#                                 self.username, self.password)

class streetLevelCrimes(Base):
    __tablename__ = "streetLevelCrimes"
    id = Column(Integer, primary_key=True)
    category = Column(String)
    location_type = Column(String)
    latitude = Column(String)
    longitude = Column(String)
    street_id = Column(String)
    street_name = Column(String)
    context = Column(String)
    outcome_status = Column(String)
    persistent_id = Column(String)
    location_subtype = Column(String)
    month = Column(String)

    def __repr__(self):
        return "<streetLevelCrimes(id='%i',category='%s',location_type='%s',latitude='%s',longitude='%s',street_id='%s',street_name='%s',context='%s',outcome_status='%s',persistent_id='%s',location_subtype='%s',month='%s')>" % (
                                self.id, self.category, self.location_type, self.latitude, self.longitude, self.street_id, 
                                self.street_name, self.context, self.outcome_status, self.persistent_id, self.location_subtype, self.month)


crime_url_template = 'https://data.police.uk/api/crimes-street/all-crime?lat={lat}&lng={lng}&date={data}'
# crimeoutcome_url_template = 'https://data.police.uk/api/crimes-street/outcomes-for-crime?id={id}'
# categories_url_template = 'https://data.police.uk/api/crime-categories?date={date}'

# my_latitude = '51.52369'
# my_longitude = '-0.0395857'
# my_date = '2018-11'
# crime_url = crime_url_template.format(lat = my_latitude, lng = my_longitude, data = my_date)
# resp = requests.get(crime_url)

# if resp.ok:
#     result = resp.json()

# for r in result:
#     crimes = streetLevelCrimes(id=None if r['id'] == '' else r['id'], 
#                                category=None if r['category'] == '' else r['category'], 
#                                location_type=None if r['location_type'] == '' else r['location_type'], 
#                                latitude=None if r['location']['latitude'] == '' else r['location']['latitude'], 
#                                longitude=None if r['location']['longitude'] == '' else r['location']['longitude'], 
#                                street_id=None if r['location']['street']['id'] == '' else r['location']['street']['id'],
#                                street_name=None if r['location']['street']['id'] == '' else r['location']['street']['id'], 
#                                context=None if r['context'] == '' else r['context'], 
#                                outcome_status=None, 
#                                persistent_id=None if r['persistent_id'] == '' else r['persistent_id'], 
#                                location_subtype=None if r['location_subtype'] == '' else r['location_subtype'], 
#                                month=None if r['month'] == '' else r['month'])
#     session.add(crimes)

# session.commit()

# for r in result:

#     x = None if r['outcome_status'] == '' else r['outcome_status'],
#     print(x)
#     print(r['persistent_id'])
    # x = None if r['outcome_status']['category'] == '' else r['outcome_status']['category']

our_user = session.query(streetLevelCrimes).filter_by(category='anti-social-behaviour').first() 

print(our_user['category'])