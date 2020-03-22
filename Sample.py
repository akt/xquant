import requests

# api-endpoint
URL = 'https://api.binance.com/api/v3/time'
# URL = 'http://api.douban.com/v2/movie/top250?apikey=0df993c66c0c636e29ecbb5344252a4a'
# location given here
# location = "delhi technological university"

# defining a params dict for the parameters to be sent to the API 
PARAMS = {}

# sending get request and saving the response as response object 
r = requests.get(url=URL, params=PARAMS)
# r = requests.get(url=URL)

# extracting data in json format 
data = r.json()

# extracting latitude, longitude and formatted address
# of the first matching location
# latitude = data['results'][0]['geometry']['location']['lat']
# longitude = data['results'][0]['geometry']['location']['lng']
# formatted_address = data['results'][0]['formatted_address']

# printing the output 
# print("Latitude:%s\nLongitude:%s\nFormatted Address:%s"
#       % (latitude, longitude, formatted_address))
print(r.text)
