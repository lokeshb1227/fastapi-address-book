from pydantic import BaseModel

class AddressCreate(BaseModel):
    name: str
    email: str
    phone: str
    latitude: float
    longitude: float


class Address(BaseModel):
    id: int
    name: str
    email: str
    phone: str
    latitude: float
    longitude: float

    class Config:
        orm_mode = True