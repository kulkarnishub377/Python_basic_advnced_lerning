from pydantic import BaseModel


class Location(BaseModel):
    name: str
    lat: float
    lon: float
    category: str = "general"


class NearbyQuery(BaseModel):
    lat: float
    lon: float
    radius_km: float = 10.0
