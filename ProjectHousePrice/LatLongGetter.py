from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="miguff")
location = geolocator.geocode("XIII. kerület, Karikás Frigyes utca 15.")
print(location.address)
print((location.latitude, location.longitude))
print(location.raw)
