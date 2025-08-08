from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])

def hello_visitor():
    visitor_name = request.args.get('visitor_name', 'Visitor')

    if visitor_name is None:
        return jsonify({"error": "Missing visitor_name parameter"}), 400  # Bad request

    client_ip = request.remote_addr

    location_url = f'https://ipapi.co/{client_ip}/json/'
    location_response = requests.get(location_url)
    location_data = location_response.json()
    city = location_data.get('city', 'Unknown location')

    weather_api_key = 'your_openweathermap_api_key'
    weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric'
    weather_response = requests.get(weather_url)
    weather_data = weather_response.json()
    temperature = weather_data['main']['temp']

    greeting = f"Hello, {visitor_name}! The temperature is {temperature} degrees Celsius in {city}."

    return jsonify(client_ip=client_ip, location=city, greeting=greeting)

if __name__ == '__main__':
    app.run(debug=True)