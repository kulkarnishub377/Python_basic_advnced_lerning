from database import add_location

MOCK_POIS = [
    {"name": "Gateway of India", "lat": 18.922, "lon": 72.834, "category": "landmark"},
    {"name": "Marine Drive", "lat": 18.943, "lon": 72.823, "category": "landmark"},
    {"name": "Taj Mahal Palace", "lat": 18.921, "lon": 72.833, "category": "hotel"},
    {"name": "Chhatrapati Shivaji Terminus", "lat": 18.940, "lon": 72.835, "category": "transport"},
    {"name": "Bandra-Worli Sea Link", "lat": 19.030, "lon": 72.815, "category": "landmark"},
    {"name": "Juhu Beach", "lat": 19.098, "lon": 72.826, "category": "beach"},
    {"name": "Elephanta Caves", "lat": 18.963, "lon": 72.931, "category": "heritage"},
    {"name": "Haji Ali Dargah", "lat": 18.982, "lon": 72.809, "category": "religious"},
    {"name": "Siddhivinayak Temple", "lat": 19.017, "lon": 72.830, "category": "religious"},
    {"name": "Powai Lake", "lat": 19.127, "lon": 72.906, "category": "nature"},
    {"name": "Eiffel Tower", "lat": 48.858, "lon": 2.294, "category": "landmark"},
    {"name": "Statue of Liberty", "lat": 40.689, "lon": -74.044, "category": "landmark"},
    {"name": "Sydney Opera House", "lat": -33.856, "lon": 151.215, "category": "landmark"},
]


def seed():
    for poi in MOCK_POIS:
        add_location(poi)
    print(f"[+] Seeded {len(MOCK_POIS)} Points of Interest")


if __name__ == "__main__":
    seed()
