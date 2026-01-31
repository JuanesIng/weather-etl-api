from fastapi import FastAPI
import models, db
from routers import weather

app = FastAPI()

models.Base.metadata.create_all(bind=db.engine)
app.include_router(weather.router)