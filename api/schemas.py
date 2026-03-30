from pydantic import BaseModel, Field
from datetime import datetime

class WeatherSchema(BaseModel):
    city: str = Field(example="Cartagena")
    weather: str = Field(example="Haze")
    temperature: float = Field(example=35.2)
    humidity: float = Field(example=88.0)
    wind_speed: float = Field(example=2.4)
    time_stamp: datetime = Field(example=datetime.now())
    class Config:
        orm_mode = True