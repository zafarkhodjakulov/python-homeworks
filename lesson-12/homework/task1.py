import requests

def fetch_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        print(f"Weather in {city}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Weather: {data['weather'][0]['description']}")
    else:
        print(f"Failed to fetch weather data: {response.status_code} - {response.reason}")
    
    print(response.content)

if __name__ == "__main__":
    city_name = "TASHKENT"
    api_key = "c15e929b0abd59b529b1666c44ff4b57"

    fetch_weather(city_name, api_key)