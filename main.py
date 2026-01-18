import requests
from dotenv import load_dotenv
from os import getenv
from etl import extract, transform, load

load_dotenv()
API_KEY = getenv('API_KEY')

cities = ["Bogota", "Medellin", "Cali", "Bucaramanga", "Tunja"]

data_city = [ ]

for city in cities:
    try:
        data = extract.extract_weather(city, API_KEY)
        
        data_city.append(transform.transform_weather(data))

    except requests.exceptions.RequestException:
        print(f"La ciudad {city} no existe o no cargó correctamente")


load.load_weather(data_city)