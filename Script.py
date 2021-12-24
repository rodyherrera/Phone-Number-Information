# ***
# * Copyright (C) Rodolfo Herrera Hernandez. All rights reserved.
# * Licensed under the MIT license. See LICENSE file in the project root 
# * for full license information.
# *
# * =+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+
# *
# * For related information - https://github.com/codewithrodi/Phone-Number-Information/
# *
# * =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# ****/

from opencage.geocoder import OpenCageGeocode
from phonenumbers import ( geocoder, carrier, parse )
from os import system

import platform

kOperativeSystem = platform.system()

def Main():
    print('''\
=============== PHONE NUMBERS INFORMATION ===============
 * Developed by Rodolfo Herrera Hernandez
 * https://github.com/codewithrodi/
 * contact@codewithrodi.com - Full Stack Developer
''')

    print(':: Phone number example: +56 9 1122 3344')
    Number = input('/> Enter a phone number including the country code: ')

    # https://opencagedata.com/ API KEY
    KEY = '3c3d3f1a27614afd86b3f64addc1ceb3'

    ParsedNumber = parse(Number.replace(' ', ''))
    Country = geocoder.description_for_number(ParsedNumber, 'en')
    Service = carrier.name_for_number(ParsedNumber, 'en')

    PhoneInformation = OpenCageGeocode(KEY).geocode(Country)
    Geometry = PhoneInformation[8]
    Latitude = Geometry['geometry']['lat']
    Longitude = Geometry['geometry']['lng']
    State = Geometry['components']['state']

    Annotations = PhoneInformation[0]['annotations']
    Timezone = Annotations['timezone']['name']

    Components = PhoneInformation[0]['components']
    CountryCode = Components['country_code']
    Continent = Components['continent']

    Output = f'''
=============== RESULTS ===============
 * Country: {Country} [{CountryCode.upper()}] [{Continent}]
 * State: {State} [Approximate]
 * Carrier: {Service}
 * Timezone: {Timezone}
 * Latitude: {Latitude} [Approximate]
 * Longitude: {Longitude} [Approximate]
 =======================================
'''

    print(Output)

    SaveDataResponse = input('/> Do you want to save the information in a file?[y/N]: ')

    if SaveDataResponse.upper() == 'Y':
        LogFile = open('Log.txt', 'a')
        LogFile.write(
    f'''\
Information related to the number: {Number}
{Output}\n''')
        print('\nInformation saved in [Log.txt]')
        LogFile.close()
    else:
        print('\n:: Gooooooodbye, drink water!')

def ClearScreen() -> None:
    system('cls' if kOperativeSystem == 'Windows' else 'clear')

if __name__ == '__main__':
    try:
        ClearScreen()
        Main()
    except KeyboardInterrupt:
        print('\n:: Remember drink water!')
    except Exception:
        print('\n:: An error occurred when trying to continue with the execution of the program, it is an unhandled exception was thrown.')