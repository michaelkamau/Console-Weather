import json
import urllib.request
import datetime
from console_weather.utilities import degrees_to_direction


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

# Get important parameters
desc = weather_data['weather'][0]['description'].capitalize() # weather summary
dt = datetime.datetime.fromtimestamp(weather_data['dt']) # date timestamp
date_obtained = dt.strftime("%A, %d %B %Y %I:%M%p") # date report obtained
temp = weather_data['main']['temp'] # temperature
pressure = weather_data['main']['pressure'] # pressure
humidity = weather_data['main']['humidity'] # humidity
wind_direction = degrees_to_direction(weather_data['wind']['deg']) # wind direction
wind_speed = weather_data['wind']['speed'] # wind speed
sr = datetime.datetime.fromtimestamp(weather_data['sys']['sunrise'])
sunrise = sr.strftime("%I:%M%p") # sunrise
st = datetime.datetime.fromtimestamp(weather_data['sys']['sunset'])
sunset = st.strftime("%I:%M%p") # sunset

# Output weather data obtained
print("\n\n")
print('Weather  in ', place.capitalize(), '\n')
print('Description\t:', desc)
print('Date obtained\t:', date_obtained)
print('Temperature\t:', temp)
print('Pressure\t:', pressure)
print('Humidity\t:', humidity)
print('Wind\t:', 'Direction\t:', wind_direction, 'Speed:\t', wind_speed)
print('Sunrise\t:', sunrise)
print('Sunset\t:', sunset)



