from app import app
from app.models.place import Place
from app.models.city import City
from flask import jsonify, request

@app.route("/places", methods=["GET"])
@app.route("/places/", methods=["GET"])
def get_all_places():
    places = []
    for place in Place.select():
        places.append(place.to_hash())
    return jsonify({"places": places})

@app.route("/places", methods=["POST"])
@app.route("/places/", methods=["POST"])
def create_places():
    content = request.get_json()
    if not all(param in content.keys() for param in ["name", "city", "owner", "description", "number_rooms", "number_bathrooms", "max_guest", "price_by_night", "latitude", "longitude"]):
        #ERROR
        return "Failed: bad input"
    try:
        place = Place()
        place.name = content["name"]
        place.city = content["city"]
        place.owner = content["owner"]
        place.description = content["description"]
        place.number_rooms = content["number_rooms"]
        place.number_bathrooms = content["number_bathrooms"]
        place.max_guest = content["max_guest"]
        place.price_by_night = content["price_by_night"]
        place.latitude = content["latitude"]
        place.longitude = content["longitude"]
        place.save()
    except Exception as e:
        return "Failed"
    return "Success"

@app.route("/places/<place_id>", methods=["GET"])
@app.route("/places/<place_id>/", methods=["GET"])
def get_place_by_id_aaa(place_id):
    if not isinstance(int(place_id), int):
        return "Failed"
    places = Place.select().where(Place.id == int(place_id))
    place = None
    for u in places:
        place = u
    if place == None:
        return "Failed"
    return jsonify(place.to_hash())


@app.route("/places/<place_id>", methods=["PUT"])
@app.route("/places/<place_id>/", methods=["PUT"])
def update_place_by_id(place_id):
    def update_name(place, val):
        place.name = val

    def update_description(place, val):
        place.description = val

    def update_number_rooms(place, val):
        place.number_rooms = val

    def update_number_bathrooms(place, val):
        place.number_bathrooms = val

    def update_max_guest(place, val):
        place.max_guest = val

    def update_price_by_night(place, val):
        place.price_by_night = val

    def update_latitude(place, val):
        place.latitude = val

    def update_longitude(place, val):
        place.longitude = val

    try:
        content = request.get_json()
        places = Place.select().where(Place.id == int(place_id))
        place = None
        for u in places:
            place = u
        if place == None:
            return "Failed"
        for param in content.keys():
            try:
                {
                    "name": update_name,
                    "description": update_description,
                    "number_rooms": update_number_rooms,
                    "number_bathrooms": update_number_bathrooms,
                    "max_guest": update_max_guest,
                    "price_by_night": update_price_by_night,
                    "latitude": update_latitude,
                    "longitude": update_longitude,
                }[param](place, content[param])
            except NameError:
                pass
        place.save()
    except:
        return "Failed"
    return jsonify(place.to_hash())

# AAAAAAAHH!!!!
@app.route("/places/<place_id>", methods=["DELETE"])
@app.route("/places/<place_id>/", methods=["DELETE"])
def delete_place_by_id(place_id):
    try:
        places = Place.select().where(Place.id == int(place_id))
        place = None
        for u in places:
            place = u
        if place == None:
            return "Failed"
        place.delete_instance()
    except:
        return "Failed"
    return "success"


@app.route("/states/<state_id>/cities/<city_id>/places", methods=["GET"])
@app.route("/states/<state_id>/cities/<city_id>/places/", methods=["GET"])
def get_all_places_hdf(place_id, city_id):
    places = []
    for place in Place.select().where(Place.city.id == city_id):
        places.append(place.to_hash())
    return jsonify({"places": places})

@app.route("/states/<state_id>/cities/<city_id>/places", methods=["POST"])
@app.route("/states/<state_id>/cities/<city_id>/places/", methods=["POST"])
def create_places_fds(state_id, city_id):
    content = request.get_json()
    if not all(param in content.keys() for param in ["name", "owner", "description", "number_rooms", "number_bathrooms", "max_guest", "price_by_night", "latitude", "longitude"]):
        #ERROR
        return "Failed: bad input"
    try:
        cities = Cities.select().where(city.id == int(city_id))
        city = None
        for u in cities:
            city = u
        if city == None:
            return "Failed"

        place = Place()
        place.name = content["name"]
        place.city = city
        place.owner = content["owner"]
        place.description = content["description"]
        place.number_rooms = content["number_rooms"]
        place.number_bathrooms = content["number_bathrooms"]
        place.max_guest = content["max_guest"]
        place.price_by_night = content["price_by_night"]
        place.latitude = content["latitude"]
        place.longitude = content["longitude"]
        place.save()
    except Exception as e:
        return "Failed"
    return "Success"
