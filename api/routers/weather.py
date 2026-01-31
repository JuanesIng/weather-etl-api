from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from typing import List
from schemas import WeatherSchema
from db import get_db
import models

router = APIRouter(prefix="/weather", tags=["weather"])

@router.get("/latest", response_model= List[WeatherSchema], summary="List last records")
def list_last(limit: int = 10, db: Session = Depends(get_db)):
    return (db.query(models.Weather)
            .order_by(models.Weather.time_stamp.desc())
            .limit(limit)
            .all()
            )

@router.get("/{city}", response_model=List[WeatherSchema], summary="List data by city")
def list_by_city(city: str, limit: int = 100, db: Session = Depends(get_db)):
    return (db.query(models.Weather).filter(models.Weather.city == city)
            .order_by(models.Weather.time_stamp.desc())
            .limit(limit)
            .all()
            )

@router.get("/", response_model=List[WeatherSchema], summary="List all cities")
def list_all(limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.Weather).limit(limit).all()