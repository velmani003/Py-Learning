#print the phone number and serivce provider name

import phonenumbers

#import folium 

from mynumber import number

from phonenumbers import geocoder

key = "be586704558d45cbbae26fce2563d29d"

samnumber = phonenumbers.parse(number)

yourLocation = geocoder.description_for_number(samnumber, 'en')

print(yourLocation)

#get service provider

from phonenumbers import carrier

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, 'en'))

from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(key)

query = str(yourLocation)

result = geocoder.geocode(query)
#print(result)

lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']
print(lat,lng)

#myMap = folium.Map(location=[lat, lng], zoom_start_=_9)

#folium.Marker([lat,lng], popup=_yourLocation).add_to((myMap)) 

#save map in html file
#myMap.save("myLocation_html")


