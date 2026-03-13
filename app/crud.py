from sqlalchemy.orm import Session
from . import models, schemas
import math


def create_address(db: Session, address: schemas.AddressCreate):
    db_address = models.Address(
        name=address.name,
        email=address.email,
        phone=address.phone,
        latitude=address.latitude,
        longitude=address.longitude
    )

    db.add(db_address)
    db.commit()
    db.refresh(db_address)

    return db_address


def get_addresses(db: Session):
    return db.query(models.Address).all()


def delete_address(db: Session, address_id: int):
    address = db.query(models.Address).filter(models.Address.id == address_id).first()

    if address:
        db.delete(address)
        db.commit()

    return {"message": "Address deleted successfully"}


# Distance calculation
def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371

    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))

    return R * c


def get_nearby_addresses(db: Session, lat, lon, radius):
    addresses = db.query(models.Address).all()
    result = []

    for address in addresses:
        distance = calculate_distance(lat, lon, address.latitude, address.longitude)

        if distance <= radius:
            result.append({
                "id": address.id,
                "name": address.name,
                "email": address.email,
                "phone": address.phone,
                "distance_km": round(distance, 2)
            })

    return result