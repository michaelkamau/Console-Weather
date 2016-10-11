import json
import  urllib.request

# TODO: Complete intro string
intro = 'Welcome to Console Weather'

# prompt user for place
# TODO: Sanitize this input: - trim, must be single for now
place = input("Enter the place name: ")

place_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + place + '&units=metric&appid=aa5ef977dbf3abdd8f60ad680ad2e4aa'

# make get request
data = urllib.request.urlopen(place_url).read()

# decode the weather data to dict
weather_data = json.loads(str(data, encoding='utf-8'))

print(weather_data)