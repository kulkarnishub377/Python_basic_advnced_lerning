import math

EARTH_RADIUS_KM = 6371.0


def haversine(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """
    Calculate the great-circle distance between two points on Earth
    using the Haversine formula. Returns distance in kilometers.
    """
    lat1_r, lon1_r = math.radians(lat1), math.radians(lon1)
    lat2_r, lon2_r = math.radians(lat2), math.radians(lon2)

    dlat = lat2_r - lat1_r
    dlon = lon2_r - lon1_r

    a = math.sin(dlat / 2) ** 2 + math.cos(lat1_r) * math.cos(lat2_r) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return round(EARTH_RADIUS_KM * c, 2)


def find_within_radius(center_lat: float, center_lon: float, radius_km: float, points: list) -> list:
    """Filter points that fall within the given radius from center."""
    results = []
    for point in points:
        dist = haversine(center_lat, center_lon, point["lat"], point["lon"])
        if dist <= radius_km:
            results.append({**point, "distance_km": dist})
    results.sort(key=lambda x: x["distance_km"])
    return results
