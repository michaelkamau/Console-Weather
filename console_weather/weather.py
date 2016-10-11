import json
import urllib.request
import datetime
from console_weather.utilities import degrees_to_direction
from console_weather.utilities import bcolors


def get_weather():
    # TODO: Complete intro string
    header = '''
      _  _        __  _      _           _     ___     _  _
     /  / \ |\ | (_  / \ |  |_   \    / |_  /\  | |_| |_ |_)
     \_ \_/ | \| __) \_/ |_ |_    \/\/  |_ /--\ | | | |_ | \ '''

    print(bcolors.HEADER, header, bcolors.ENDC)
    intro = 'Find the prevailing weather condition right away!'
    print(bcolors.WARNING, intro, bcolors.ENDC)

    # prompt user for place
    # TODO: Sanitize this input: - trim, must be single for now
    print('\t', bcolors.BOLD)
    place = input("Enter the name of place: ")
    print(bcolors.ENDC)
    place = place.strip()

    place_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + place + '&units=metric&appid=aa5ef977dbf3abdd8f60ad680ad2e4aa'

    # make get request
    data = urllib.request.urlopen(place_url).read()

    # decode the weather data to dict
    weather_data = json.loads(str(data, encoding='utf-8'))

    # print(weather_data)

    # Get important parameters
    desc = weather_data['weather'][0]['description'].capitalize()  # weather summary
    dt = datetime.datetime.fromtimestamp(weather_data['dt'])  # date timestamp
    date_obtained = dt.strftime("%A, %d %B %Y %I:%M%p")  # date report obtained
    temp = weather_data['main']['temp']  # temperature
    pressure = weather_data['main']['pressure']  # pressure
    humidity = weather_data['main']['humidity']  # humidity
    wind_direction = degrees_to_direction(weather_data['wind']['deg'])  # wind direction
    wind_speed = weather_data['wind']['speed']  # wind speed
    sr = datetime.datetime.fromtimestamp(weather_data['sys']['sunrise'])
    sunrise = sr.strftime("%I:%M%p")  # sunrise
    st = datetime.datetime.fromtimestamp(weather_data['sys']['sunset'])
    sunset = st.strftime("%I:%M%p")  # sunset

    # Output weather data obtained
    print("\n")
    print('\t', bcolors.HEADER, 'Weather  in ', place.capitalize(), bcolors.ENDC, '\n')
    print('\t', bcolors.OKBLUE, 'Description\t:', bcolors.ENDC, bcolors.OKGREEN, desc, bcolors.ENDC)
    print('\t', bcolors.OKBLUE, 'Date obtained\t:', bcolors.ENDC, bcolors.OKGREEN, date_obtained, bcolors.ENDC)
    print('\t', bcolors.OKBLUE, 'Temperature\t:', bcolors.ENDC, bcolors.OKGREEN, temp, bcolors.ENDC)
    print('\t', bcolors.OKBLUE, 'Pressure\t\t:', bcolors.ENDC, bcolors.OKGREEN, pressure, ' hpa', bcolors.ENDC)
    print('\t', bcolors.OKBLUE, 'Humidity\t\t:', bcolors.ENDC, bcolors.OKGREEN, humidity, '%', bcolors.ENDC)
    print('\t', bcolors.OKBLUE, 'Wind Direction:', bcolors.ENDC, bcolors.OKGREEN, wind_direction, bcolors.ENDC)
    print('\t', bcolors.OKBLUE, 'Wind Speed\t:', bcolors.ENDC, bcolors.OKGREEN, wind_speed, ' m/s', bcolors.ENDC)
    print('\t', bcolors.OKBLUE, 'Sunrise\t\t:', bcolors.ENDC, bcolors.OKGREEN, sunrise, bcolors.ENDC)
    print('\t', bcolors.OKBLUE, 'Sunset\t\t:', bcolors.ENDC, bcolors.OKGREEN, sunset, bcolors.ENDC)

    print('\n', bcolors.BOLD, "Powered by http://openweathermap.org/", bcolors.ENDC)
