import json
import requests
from flask_sqlalchemy import SQLAlchemy

crime_url_template = 'https://data.police.uk/api/crimes-street/all-crime?lat={lat}&lng={lng}&date={data}'
crimeoutcome_url_template = 'https://data.police.uk/api/crimes-street/outcomes-for-crime?id={id}'
categories_url_template = 'https://data.police.uk/api/crime-categories?date={date}'

my_latitude = '51.52369'
my_longitude = '-0.0395857'
my_date = '2018-11'
crime_url = crime_url_template.format(lat = my_latitude, lng = my_longitude, data = my_date)
resp = requests.get(crime_url)

for r in resp:
    print(r[1], r[2])
