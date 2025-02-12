import requests

lat = 41.2995
lon = 69.2401
api_key = '8f972a21e6fca8765b0fc25f2c910363'

response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}')

res = response.json()

data = {   
    'coord': 
        {'lon': 69.2401, 'lat': 41.2995},
    'weather': 
        [  
            {'id': 701, 'main': 'Mist', 'description': 'mist', 'icon': '50n'}
        ],
    'base': 'stations',
    'main': 
        {'temp': 274.99, 'feels_like': 272.77, 'temp_min': 274.99, 'temp_max': 274.99, 'pressure': 1031, 'humidity': 87, 'sea_level': 1031, 'grnd_level': 978},
    'visibility': 4000, 
    'wind': 
        {'speed': 2.06, 'deg': 300},
    'clouds': 
        {'all': 40}, 'dt': 1739280541, 
    'sys': {'type': 1, 'id': 9016, 'country': 'UZ', 'sunrise': 1739240604, 'sunset': 1739278279}, 
    'timezone': 18000, 
    'id': 1514635, 
    'name': 'Aktepa', 
    'cod': 200
}

print(f'''
      {res['weather'][0]['main']}
      {(res['main']['temp'] - 273.15):.2}
      {res['main']['humidity']} %
''')