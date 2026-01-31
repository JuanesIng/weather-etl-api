from pydantic import BaseModel, Field
from datetime import datetime
from models import WeatherType

class WeatherSchema(BaseModel):
    city: str = Field(example="Cartagena")
    weather: WeatherType = Field(WeatherType.Clear)
    temperature: float = Field(example=35.2)
    humidity: float = Field(example=88.0)
    wind_speed: float = Field(example=2.4)
    time_stamp: datetime = Field(example=datetime.now())

class Config:
        orm_mode = True