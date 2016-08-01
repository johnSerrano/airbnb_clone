from app import app
from app.models.amenity import Amenity
from flask import jsonify, request

@app.route("/amenities", methods=["GET"])
# @app.route("/amenities/", methods=["GET"])
def get_all_amenities():
    amenities = []
    for amenity in Amenity.select():
        amenities.append(amenity.to_dict())
    return jsonify({"amenities": amenities})

@app.route("/amenities", methods=["POST"])
# @app.route("/amenities/", methods=["POST"])
def create_asdfstate():
    content = request.get_json(force=True)
    if not content: return "Failed"
    if not all(param in content.keys() for param in ["name"]):
        #ERROR
        return "Failed: bad input"
    try:
        amenity = Amenity()
        amenity.name = content["name"]
        amenity.save()
    except Exception as e:
        return "Failed"
    return "Success"

@app.route("/amenities/<amen_id>", methods=["GET"])
# @app.route("/amenities/<amen_id>/", methods=["GET"])
def get_statdasfde_by_id(amen_id):
    amens = Amenity.select().where(Amenity.id == int(amen_id))
    amen = None
    for u in amens:
        amen = u
    if amen == None:
        return "Failed"
    return jsonify(amen.to_dict())

@app.route("/amenities/<amen_id>", methods=["DELETE"])
# @app.route("/amenities/<amen_id>/", methods=["DELETE"])
def get_staasedfazte_by_id(amen_id):
    amens = Amenity.select().where(Amenity.id == int(amen_id))
    amen = None
    for u in amens:
        amen = u
    if amen == None:
        return "Failed"
    amen.delete_instance()
    return "Success"

@app.route("/places/<place_id>/amenities", methods=["GET"])
# @app.route("/places/<place_id>/amenities/", methods=["GET"])
def get_asdhfjahsdfja(place_id):
    pas = PlaceAmenities.select().where(PlaceAmenities.place.id == place_id)
    ams = []
    for pa in pas:
        ams.append(pa.amenity.to_dict())
    return jsonify(ams)

@app.route("/places/<place_id>/amenities/<amenity_id>", methods=["POST"])
def create_new_amenity_in_place(place_id, amenity_id):
    try:
        pas = PlaceAmenities.select().where(PlaceAmenities.place.id == int(place_id))
        amens = Amenity.select().where(Amenity.id == int(amen_id))
        if pas == None or amens == None:
            throw Exception
        place_amenity = app.models.place_amenity.PlaceAmenities()
        place_amenity.place = pas
        place_amenity.amenity = amens
    except:
        return "Failed"
    return "Success"

#TODO
@app.route("/places/<place_id>/amenities/<amenity_id>", methods=["DELETE"])
def delete_amenity_in_place(place_id, amenity_id):
    pasamen = PlaceAmenities.select().where(PlaceAmenities.place.id == int(place_id) and PlaceAmenities.amenity.id == int(amenity_id))
    amen = None
    for u in pasamen:
        amen = u
    if amen == None:
        return "Failed"
    amen.delete_instance()
    return "Success"
