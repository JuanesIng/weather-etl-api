import requests


data_city = [ ]

def extract_weather(city, API_KEY):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=es"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    return(data)