locations_db = []


def get_all_locations():
    return locations_db


def add_location(loc: dict):
    locations_db.append(loc)
    return loc
