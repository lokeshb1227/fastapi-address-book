from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from . import models, schemas, crud
from .database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Address Book API is running"}


# Database connection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/addresses", response_model=schemas.Address)
def create_address(address: schemas.AddressCreate, db: Session = Depends(get_db)):
    return crud.create_address(db, address)


@app.get("/addresses")
def get_addresses(db: Session = Depends(get_db)):
    return crud.get_addresses(db)


@app.delete("/addresses/{address_id}")
def delete_address(address_id: int, db: Session = Depends(get_db)):
    return crud.delete_address(db, address_id)


@app.get("/addresses/nearby")
def get_nearby(lat: float, lon: float, radius: float, db: Session = Depends(get_db)):
    return crud.get_nearby_addresses(db, lat, lon, radius)