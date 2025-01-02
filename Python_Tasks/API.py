import requests

api_key = 'Your_API_Key'
city = 'Mumbai'
url = f'http://api.weatherstack.com/current?access_key={api_key}&query={city}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
    temperature = data['current']['temperature']
    icon = data['current']['weather_icons'][0]
    description = data['current']['weather_descriptions']

    print(f"Weather in {city}:")
    print(f"Temperature: {temperature}°C")
    print(f"Temperature: {icon}°C")
    print(f"Condition: {description}")
else:
    print("Failed to retrieve data. HTTP Status Code:", response.status_code)
