from datetime import datetime

def transform_weather(data):
    return({
                "name" : data['name'],
                "weather" : data["weather"][0]["main"],
                "windspeed" : data["wind"]["speed"],
                "temperature" : data["main"]["temp"],
                "humidity" : data["main"]["humidity"],
                "date" : datetime.now().isoformat()
            })