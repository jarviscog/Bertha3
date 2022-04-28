import requests, json
import math
API_KEY = "b190a0605344cc4f3af08d0dd473dd25"
def get_weather(CITY="Ilderton"):
    # importing requests and json
    # base URL
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    # City Name CITY = "Hyderabad"
    # API key API_KEY = "Your API Key"
    # upadting the URL
    URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
    # print(URL)
    # HTTP request
    response = requests.get(URL)
    # checking the status code of the request
    if response.status_code == 200:
        # getting data in the json format
        data = response.json()
        # getting the main dict block
        main = data['main']
        # getting temperature
        temperature = main['temp']
        # getting the humidity
        humidity = main['humidity']
        # getting the pressure
        pressure = main['pressure']
        # weather report
        report = data['weather']
        # print(f"{CITY:-^30}")
        # print(f"Temperature: {temperature}")
        # print(f"Humidity: {humidity}")
        # print(f"Pressure: {pressure}")
        # print(f"Weather Report: {report[0]['description']}")
        return_string = "In " + CITY + " it is currently " + str(round(temperature-273.15,2)) + "C"
        return return_string
    else:
        # showing the error message
        print("Error in the HTTP request")
        return ""