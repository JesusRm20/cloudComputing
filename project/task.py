import json
import requests
from passwordHash import hashPassword
import crimeClasses
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///db/cloudCompProject.db", connect_args={'check_same_thread': False})
session = sessionmaker(bind=engine)()

def loadStreestLevelCrimes():
    crime_url_template = 'https://data.police.uk/api/crimes-street/all-crime?lat={lat}&lng={lng}&date={data}'

    my_latitude = '51.52369'
    my_longitude = '-0.0395857'
    my_date = '2018-11'
    crime_url = crime_url_template.format(lat = my_latitude, lng = my_longitude, data = my_date)
    resp = requests.get(crime_url)

    if resp.ok:
        result = resp.json()

    for r in result:
        crimes = crimeClasses.streetLevelCrimes(id=None if r['id'] == '' else r['id'], 
                                   category_id=None if r['category'] == '' else r['category'], 
                                   location_type=None if r['location_type'] == '' else r['location_type'], 
                                   latitude=None if r['location']['latitude'] == '' else r['location']['latitude'], 
                                   longitude=None if r['location']['longitude'] == '' else r['location']['longitude'], 
                                   street_id=None if r['location']['street']['id'] == '' else r['location']['street']['id'],
                                   street_name=None if r['location']['street']['name'] == '' else r['location']['street']['name'], 
                                   context=None if r['context'] == '' else r['context'], 
                                   outcome_status=None, 
                                   persistent_id=None if r['persistent_id'] == '' else r['persistent_id'], 
                                   location_subtype=None if r['location_subtype'] == '' else r['location_subtype'], 
                                   month=None if r['month'] == '' else r['month'])
        session.add(crimes)

    session.commit()

def loadCrimesCategories():
    categories_url_template = 'https://data.police.uk/api/crime-categories'
    resp = requests.get(categories_url_template)

    if resp.ok:
        result = resp.json()
    
    for cat in result:
        category = crimeClasses.crimeCategories(name=cat['url'].lower())
        session.add(category)
    session.commit()

def loadCrimesOutcome():
    our_user = session.query(crimeClasses.streetLevelCrimes.persistent_id).distinct('persistent_id') 
    for u in our_user:
        crimeoutcome_url_template = 'https://data.police.uk/api/outcomes-for-crime/{id}'
        crimeid = u[0]
        crime_url = crimeoutcome_url_template.format(id = crimeid)

        resp = requests.get(crime_url)      

        if resp.ok:
            result = resp.json()
        for res in result['outcomes']:
            outcome = crimeClasses.outcomesCrimes(persistent_id=result['crime']['persistent_id'],category=res['category']['name'],date_1=res['date'],person_id=res['person_id'])
            session.add(outcome)
        session.commit()

def getStreestLevelCrimes():
    result = session.query(crimeClasses.streetLevelCrimes).order_by(crimeClasses.streetLevelCrimes.month).limit(100)
    return result

def getCrimesCategories():
    result = session.query(crimeClasses.crimeCategories).all()

def getCrimesOutcome(id):
    result = session.query(crimeClasses.outcomesCrimes).filter_by(persistent_id=id).all()
    return result

# for i in getCrimesOutcome('de8d2d293c09aa6a6bf98da17a2e0f59cbb488aea60c3e475321bdce2908c09b'):
#     print(i.category)
# category_id = session.query(crimeClasses.crimeCategories.id).filter_by(name='bicycle-theft'.lower()).first()
# print(category_id.id)
# loadStreestLevelCrimes()
# resp = getStreestLevelCrimes()
# for i in resp:
#     print()