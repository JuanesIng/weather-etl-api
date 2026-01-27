from sqlalchemy import create_engine, text
from dotenv import load_dotenv
from os import getenv

#Load environment variables from .env file
load_dotenv()

#Database connection settings
DB_NAME = getenv('DB_NAME')
DB_USER = getenv('DB_USER')
DB_PASSWORD = getenv('DB_PASSWORD')
DB_HOST = getenv('DB_HOST')
DB_PORT = getenv('DB_PORT')
DB_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

#Create SQLAlchemy engine
engine = create_engine(DB_URL)


def load_weather(data: list[dict]):
    """
    Inserts weather data into the 'weather' table

    :param data: List of dictionaries with weather information.
                 Each dictionary must match the following keys:
                 -name
                 -weather
                 -temperature
                 -humidity
                 -windspeed
                 -date
    """
    
    query = text("INSERT INTO weather(city, weather, temperature, humidity, wind_speed, time_stamp) " \
            "VALUES (:name, :weather, :temperature, :humidity, :windspeed, :date)")

    try:
        with engine.begin() as conn:
            for row in data:
                conn.execute(query, row)
            print("The data was inserted correctly")
    except Exception as e:
          print("Error: ", e)
