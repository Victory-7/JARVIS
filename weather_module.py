import requests

def get_weather(city):
    api_key = "your_openweather_api_key"
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temp = data['main']['temp'] - 273.15
        return f"Weather in {city}: {weather}, Temperature: {temp:.2f}°C"
    else:
        return "City not found."
