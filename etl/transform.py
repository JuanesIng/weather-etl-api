from datetime import datetime

def transform_weather(data):
    return({
                "nombre" : data['name'],
                "clima" : data["weather"][0]["main"],
                "viento" : data["wind"]["speed"],
                "temperatura" : data["main"]["temp"],
                "humedad" : data["main"]["humidity"],
                "hora" : datetime.now().isoformat()
            })