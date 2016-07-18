from app import app
from app.models.state import State
from app.models.city import City
from flask import jsonify, request

@app.route("/states/<state_id>/cities", methods=["GET"])
# @app.route("/states/<state_id>/cities/", methods=["GET"])
def get_all_cities(state_id):
    cities = []
    for city in City.select().where(City.state == state_id):
        cities.append(city.to_hash())
    return jsonify({"cities": cities})

@app.route("/states/<state_id>/cities", methods=["POST"])
# @app.route("/states/<state_id>/cities/", methods=["POST"])
def create_city(state_id):
    content = request.get_json(force=True)
    if not all(param in content.keys() for param in ["name"]):
        #ERROR
        return "Failed: bad input"
    try:
        city = City()
        city.name = content["name"]
        city.state = state_id
        city.save()
    except Exception as e:
        return "Failed"
    return "Success"

@app.route("/states/<state_id>/cities/<city_id>", methods=["GET"])
# @app.route("/states/<state_id>/cities/<city_id>/", methods=["GET"])
def get_state_by_id(state_id, city_id):
    if not isinstance(int(city_id), int):
        return "Failed"
    cities = City.select().where(City.id == int(city_id))
    city = None
    for u in cities:
        city = u
    if city == None:
        return "Failed"
    return jsonify(city.to_hash())


@app.route("/states/<state_id>/cities/<city_id>", methods=["DELETE"])
# @app.route("/states/<state_id>/cities/<city_id>/", methods=["DELETE"])
def delete_state_by_id(state_id, city_id):
    try:
        cities = City.select().where(City.id == int(city_id))
        city = None
        for u in cities:
            city = u
        if city == None:
            return "Failed"
        city.delete_instance()
    except:
        return "Failed"
    return "Success"
