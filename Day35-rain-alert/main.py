import requests
from secretss import twilio_account_sid, twilio_auth_token
from twilio.rest import Client


count_url = "https://api.openweathermap.org/data/2.5/forecast?lat=6.524379&lon=3.379206&cnt=4&appid=ce3140107ea09985570740fd6cc8551d"

api_url = "https://api.openweathermap.org/data/2.5/forecast?"
api_key = "ce3140107ea09985570740fd6cc8551d"
lat = 6.524379
lon = 3.379206

weather_parameter = {
    "lat": lat,
    "lon": lon,
    "appid": api_key,
    "cnt": 4
}


response = requests.get(url= api_url, params= weather_parameter)
data = response.json()
response.raise_for_status()

rainy_day = False
for hour_data in data['list']:
    forecast_id = hour_data['weather'][0]['id']
    if forecast_id < 700:
        rainy_day = True
    print(forecast_id)

if rainy_day:
    client = Client(twilio_account_sid, twilio_auth_token)

    message = client.messages \
        .create(
            body= "Its gonna rain soon buddy get an umbrella.",
            from_="+13159152758",
            to= "+2348131954247"
        )
    print(message.status)






#weather_data = [{'cod': '200', 'message': 0, 'cnt': 4, 'list': [{'dt': 1751187600, 'main': {'temp': 298.27, 'feels_like': 299.29, 'temp_min': 298.27, 'temp_max': 300.24, 'pressure': 1015, 'sea_level': 1015, 'grnd_level': 1014, 'humidity': 94, 'temp_kf': -1.97}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'clouds': {'all': 75}, 'wind': {'speed': 4.99, 'deg': 232, 'gust': 6.15}, 'visibility': 10000, 'pop': 0.79, 'rain': {'3h': 0.69}, 'sys': {'pod': 'd'}, 'dt_txt': '2025-06-29 09:00:00'}, {'dt': 1751198400, 'main': {'temp': 299.3, 'feels_like': 299.3, 'temp_min': 299.3, 'temp_max': 301.37, 'pressure': 1014, 'sea_level': 1014, 'grnd_level': 1012, 'humidity': 86, 'temp_kf': -2.07}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'clouds': {'all': 83}, 'wind': {'speed': 6.66, 'deg': 224, 'gust': 7.53}, 'visibility': 10000, 'pop': 0.95, 'rain': {'3h': 0.42}, 'sys': {'pod': 'd'}, 'dt_txt': '2025-06-29 12:00:00'}, {'dt': 1751209200, 'main': {'temp': 300.1, 'feels_like': 302.78, 'temp_min': 300.1, 'temp_max': 301.01, 'pressure': 1012, 'sea_level': 1012, 'grnd_level': 1010, 'humidity': 80, 'temp_kf': -0.91}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'clouds': {'all': 72}, 'wind': {'speed': 7.43, 'deg': 224, 'gust': 8.51}, 'visibility': 10000, 'pop': 0.57, 'rain': {'3h': 0.36}, 'sys': {'pod': 'd'}, 'dt_txt': '2025-06-29 15:00:00'}, {'dt': 1751220000, 'main': {'temp': 299.98, 'feels_like': 302.43, 'temp_min': 299.98, 'temp_max': 299.98, 'pressure': 1012, 'sea_level': 1012, 'grnd_level': 1011, 'humidity': 79, 'temp_kf': 0}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'clouds': {'all': 77}, 'wind': {'speed': 6.66, 'deg': 229, 'gust': 8.57}, 'visibility': 10000, 'pop': 0.53, 'rain': {'3h': 0.25}, 'sys': {'pod': 'd'}, 'dt_txt': '2025-06-29 18:00:00'}], 'city': {'id': 2332459, 'name': 'Lagos', 'coord': {'lat': 6.5244, 'lon': 3.3792}, 'country': 'NG', 'population': 9000000, 'timezone': 3600, 'sunrise': 1751175296, 'sunset': 1751220283}}]
# forecast_list = weather_data[0]['list']

# will_rain = False
# for forecast in forecast_list:
#     weather_id = forecast['weather'][0]['id']
#     if weather_id < 700:
#         will_rain = True

# if will_rain:
#     print("Bring out an umbrella!")