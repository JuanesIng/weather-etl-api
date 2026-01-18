from sqlalchemy import create_engine, text
from dotenv import load_dotenv
from os import getenv

load_dotenv()

DB_NAME = getenv('DB_NAME')
DB_USER = getenv('DB_USER')
DB_PASSWORD = getenv('DB_PASSWORD')
DB_HOST = getenv('DB_HOST')
DB_PORT = getenv('DB_PORT')
DB_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

def load_weather(data: list[dict]):
    engine = create_engine(DB_URL)

    query = text("INSERT INTO weather(city, weather, temperature, humidity, wind_speed, time_stamp) " \
            "VALUES (:nombre, :clima, :temperatura, :humedad, :viento, :hora)")

    try:
        with engine.begin() as conn:
            for row in data:
                conn.execute(query, row)
            print("Los datos se insertaron correctamente")
    except Exception as e:
          print("Error: ", e)
