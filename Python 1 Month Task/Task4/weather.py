import requests

API_KEY = "d530708170c5eba675035f2f46b014d9"
city = input("Enter City Name: ")
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    temp = data['main']['temp']
    weather = data['weather'][0]['description']
    humidity = data['main']['humidity']

    print("\nWeather Information: ")
    print("City: ", city)
    print("Temperacture: ", temp, "°C")
    print("Wheather :", weather)
    print("Humidity: ", humidity, "%")

else:
    print("Error: Unable to fetch weather data.")

