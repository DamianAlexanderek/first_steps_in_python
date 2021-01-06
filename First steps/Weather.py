import datetime
import requests
import random

def get_current_weather(query):
    url = "https://community-open-weather-map.p.rapidapi.com/weather"
    querystring = {"q": query, "lang": "en"}
    headers = {
        'x-rapidapi-key': "83eedd2f8amsh3047e1fda8ee63fp194334jsnbeee3b5c71c2",
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
    }
    response = requests.request(
        "GET", url, headers=headers, params=querystring)
    return response.json()

def kelvin2celsius(tk):
    tc = tk - 273.15
    return tc

def get_random_quote():
    url = "https://type.fit/api/quotes"
    response = requests.get(url)
    quotes = response.json()
    return random.choice(quotes)

now = datetime.datetime.now()
city = "Starogard Gdański"
data = get_current_weather(city)
weather = data["weather"][0]["description"]
temp = kelvin2celsius(data["main"]["temp"])
wind = data["wind"]["speed"]
press = data["main"]["pressure"]
hum = data["main"]["humidity"]
quote = get_random_quote()

print(datetime.datetime.strftime(now, "%d %B %Y"))
print(datetime.datetime.strftime(now, "%H:%M:%S"))
print("City: " + city)
print("Weather: " + weather)
print("Temperature: " + str(round(temp)) + u"\u00b0" + "C")
print("Speed wind: " + str(wind) + " km/h")
print("Pressure: " + str(press) + " hPa")
print("Humidity: " + str(hum) + "%")
print("\"" + quote["text"] + "\" (" + quote["author"] + ")")