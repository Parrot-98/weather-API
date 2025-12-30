import requests

# Your API key
api_key = "fe96ceb60ea24f1a8f130657253012"

# City you want weather for
city = "Montreal"

# API endpoint
url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"

# Make the request
response = requests.get(url)
data = response.json()

# Print weather information
print(f"City: {data['location']['name']}, {data['location']['country']}")
print(f"Temperature: {data['current']['temp_c']}°C")
print(f"Condition: {data['current']['condition']['text']}")
print(f"Wind Speed: {data['current']['wind_kph']} kph")
print(f"Humidity: {data['current']['humidity']}%")
