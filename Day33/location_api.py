import requests
from datetime import datetime

# response = requests.get(url= "http://api.open-notify.org/iss-now.json")
# data = response.json()
# response.raise_for_status()
# print(data)

# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]

# iss_position = (latitude,longitude)
# print(iss_position)
LAT = 6.524379
LNG = 3.379206


parameters = {
    "lat":LAT,
    "lng":LNG,
    "formatted": 0,
}

response = requests.get(url = 'https://api.sunrise-sunset.org/json', params= parameters)
response.raise_for_status()
data = response.json()
print(data)
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset =data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)

daytime = datetime.now()
print(daytime)