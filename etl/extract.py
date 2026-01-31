import requests

def extract_weather(city, API_KEY):

    """
    Gets current weather data from OpenWeather API

    :param city(str): Name of the city
    :param API_KEY(str): Access key for Openweather API

    :return: Weather data in json format
    """

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=es"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    return(data)