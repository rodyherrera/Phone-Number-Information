import os
from phonenumbers import (
    geocoder, carrier, parse
)
from opencage.geocoder import OpenCageGeocode

print('''
=============== PHONE NUMBERS DATA ===============
 * Developed by Rodolfo Herrera Hernandez
 * https://github.com/rodiihernandezz/
''')

print('Phone number example: +56 9 1122 3344')
number = input('Enter a phone number including the country code: ')

# https://opencagedata.com/ API KEY
KEY = '3c3d3f1a27614afd86b3f64addc1ceb3'

num = parse(number.replace(' ', ''))

country = geocoder.description_for_number(num, 'en')
service = carrier.name_for_number(num, 'en')

Location_Connection = OpenCageGeocode(KEY)
Location_Result = Location_Connection.geocode(country)

Location_Geometry = Location_Result[8]
Location_Lat = Location_Geometry['geometry']['lat']
Location_Lng = Location_Geometry['geometry']['lng']
Location_State = Location_Geometry['components']['state']

Location_Annotations = Location_Result[0]['annotations']
Location_Timezone = Location_Annotations['timezone']['name']

Location_Components = Location_Result[0]['components']
Location_CountryCode = Location_Components['country_code']
Location_Continent = Location_Components['continent']

data = f'''
=============== RESULTS ===============
* Country: {country} [{Location_CountryCode.upper()}] [{Location_Continent}]
* State: {Location_State}
* Carrier: {service}
* Timezone: {Location_Timezone}
* Latitude: {Location_Lat} [Approximate]
* Longitude: {Location_Lng} [Approximate]
=======================================
'''

print(data)

save_data = input('Do you want to save the information in a file?[y/N]: ')

if save_data.lower() == 'y':
    file = open('data.txt', 'a')
    file.write(f'''
Information related to the number: {number}
{data}
    ''')
    print('Information saved [data.txt]')
    file.close()
