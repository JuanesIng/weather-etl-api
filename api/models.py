from sqlalchemy import String, Float, DateTime, Enum as AlEnum
from sqlalchemy.orm import Mapped, mapped_column
from db import Base
from datetime import datetime
from enum import Enum

class WeatherType(str, Enum):
    Thunderstorm = "Thunderstorm"
    Drizzle = "Drizzle"
    Rain = "Rain"
    Snow = "Snow"
    Clear = "Clear"
    Clouds = "Clouds"
    Mist = "Mist"
    Fog = "Fog"

class Weather(Base):
    __tablename__ = "weather"

    id: Mapped[int] = mapped_column(primary_key=True)
    city: Mapped[str] = mapped_column(String(50), nullable=False)
    weather: Mapped[WeatherType] = mapped_column(AlEnum(WeatherType, name="weather_type"), nullable=False)
    temperature: Mapped[float] = mapped_column(Float(), nullable=False, default=0.0)
    humidity: Mapped[float] = mapped_column(Float(), nullable=False, default=0.0)
    wind_speed: Mapped[float] = mapped_column(Float(), nullable=False, default=0.0)
    time_stamp: Mapped[datetime] = mapped_column(DateTime(), nullable=False, default=datetime.now())