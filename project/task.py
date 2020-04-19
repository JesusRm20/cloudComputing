import json
import requests
from passwordHash import hashPassword
import crimeClasses
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://postgres:password@localhost:5432/cloudComputing")
session = sessionmaker(bind=engine)()

def loadStreetLevelCrimes(date):
    crime_url_template = 'https://data.police.uk/api/crimes-street/all-crime?lat={lat}&lng={lng}&date={data}'

    my_latitude = '51.52369'
    my_longitude = '-0.0395857'
    crime_url = crime_url_template.format(lat = my_latitude, lng = my_longitude, data = date.strip())
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
                                   persistent_id=0 if r['persistent_id'] == '' else r['persistent_id'], 
                                   location_subtype=None if r['location_subtype'] == '' else r['location_subtype'], 
                                   month=None if r['month'] == '' else r['month'])
        session.add(crimes)

    session.commit()

    outcome = session.query(crimeClasses.streetLevelCrimes).filter_by(persistent_id='0').all()
    for i in outcome:
        session.delete(i)
    session.commit()
    return 'OK'

def loadCrimesCategories():
    categories_url_template = 'https://data.police.uk/api/crime-categories'
    resp = requests.get(categories_url_template)

    if resp.ok:
        result = resp.json()
    
    for cat in result:
        category = crimeClasses.crimeCategories(name=cat['url'].lower())
        session.add(category)
    session.commit()

def loadCrimesOutcome(id):
    crimeoutcome_url_template = 'https://data.police.uk/api/outcomes-for-crime/{id}'
    crimeid = id
    crime_url = crimeoutcome_url_template.format(id = crimeid)

    resp = requests.get(crime_url)      

    if resp.ok:
        count = crimeClasses.outcomesCount(persistent_id=id)
        session.add(count)
        result = resp.json()
        for res in result['outcomes']:
            outcome = crimeClasses.outcomesCrimes(persistent_id=result['crime']['persistent_id'],category=res['category']['name'],date_1=res['date'],person_id=res['person_id'])
            session.add(outcome)
        session.commit()

def getStreestLevelCrimes(date=None):
    if date:
        result = session.query(crimeClasses.streetLevelCrimes).filter_by(month=date).limit(500)
    else:
        result = session.query(crimeClasses.streetLevelCrimes).order_by(crimeClasses.streetLevelCrimes.month).limit(500)
    return result

def getStreestLevelCrimesId(id1):
    result = session.query(crimeClasses.streetLevelCrimes).filter_by(id=id1)
    return result

def getStreestLevelCrimesPersistentId(id1):
    result = session.query(crimeClasses.streetLevelCrimes).filter_by(persistent_id=id1).first()
    return result

def getCrimesCategories():
    result = session.query(crimeClasses.crimeCategories).all()

def getCrimesOutcome(id):
    result = session.query(crimeClasses.outcomesCrimes).filter_by(persistent_id=id).all()
    return result

def countCrimesOutcome(id):
    count = session.query(crimeClasses.outcomesCount).filter_by(persistent_id=id).count()
    return count

def updateCrime(obj):
    crime = session.query(crimeClasses.streetLevelCrimes).filter_by(id=obj['id']).first()
    crime.location_type = obj['location_type']
    crime.category_id = obj['category']
    crime.latitude = obj['latitude']
    crime.longitude = obj['longitude']
    crime.street_name = obj['street_name']
    crime.month = obj['month']
    session.commit()
    return 'OK'

def deleteOutcome(id_outcome):
    persistent_id = ''
    outcome = session.query(crimeClasses.outcomesCrimes).filter_by(id=id_outcome).first()
    session.delete(outcome)
    persistent_id = outcome.persistent_id
    session.commit()
    crime = getStreestLevelCrimesPersistentId(persistent_id)
    crime_id = crime.id
    return crime_id

def selectDates():
    result = session.query(crimeClasses.streetLevelCrimes.month).distinct().all()
    return result

def selectCrimeByDate(date):
    result = session.query(crimeClasses.streetLevelCrimes.month).filter_by(month=date).count()
    return result