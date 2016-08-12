from app import app
from app.models.amenity import Amenity
from app.views.error import error_msg
from flask import jsonify, request

@app.route("/amenities", methods=["GET"])
def get_all_amenities():
    """
    Get all amenities
    List all amenities in the database.
    ---
    tags:
      - amenity
    responses:
      200:
        description: List of all amenities
        schema:
          id: amenities_array
          properties:
            amenities:
              type: array
              description: amenities array
              items:
                properties:
                    name:
                        type: string
                        description: name of the amenity
                        default: "flush toilets"
                    id:
                        type: number
                        description: id of the amenity
                        default: 0
                    created_at:
                        type: datetime string
                        description: date and time the amenity was created
                        default: '2016-08-11 20:30:38.959846'
                    updated_at:
                        type: datetime string
                        description: date and time the amenity was updated
                        default: '2016-08-11 20:30:38.959846'
              default: [{"name": "flush toilets", "id": 0, "created_at": '2016-08-11 20:30:38.959846', "updated_at": '2016-08-11 20:30:38.959846'}, {"name": "hammock", "id": 1, "created_at": '2016-08-11 20:30:38.959846', "updated_at": '2016-08-11 20:30:38.959846'}]
    """
    amenities = []
    for amenity in Amenity.select():
        amenities.append(amenity.to_dict())
    return jsonify({"amenities": amenities})

@app.route("/amenities", methods=["POST"])
# @app.route("/amenities/", methods=["POST"])
def create_amenity():
    """
    Create an amenity
    Creates an amenity based on post parameters.
    ---
    tags:
      - amenity
    parameters:
      - name: name
        in: query
        type: string
        description: name of the amenity to create
    responses:
      200:
        description: Success message
        schema:
          id: success_message
          properties:
            status:
              type: number
              description: status code
              default: 200
            msg:
              type: string
              description: Status message
              default: 'Success'
      400:
          description: Error message
          schema:
            id: error_message
            properties:
              status:
                type: number
                description: status code
                default: 40000
              msg:
                type: string
                description: Status message
                default: 'Missing parameters'
    """
    content = request.get_json(force=True)
    if not content: return error_msg(400, 400, "Error")
    if not all(param in content.keys() for param in ["name"]):
        #ERROR
        return error_msg(400, 40000, "Missing parameters")
    try:
        amenity = Amenity()
        amenity.name = content["name"]
        amenity.save()
    except Exception as e:
        return error_msg(400, 400, "Error")
    return error_msg(200, 200, "Success")

@app.route("/amenities/<amen_id>", methods=["GET"])
# @app.route("/amenities/<amen_id>/", methods=["GET"])
def get_amenity_by_id(amen_id):
    """
    Get one amenity
    Returns information about one amenity.
    ---
    tags:
      - amenity
    responses:
      200:
        description: Information about one amenity
        schema:
          id: amenity
          properties:
            name:
                type: string
                description: name of the amenity
                default: "flush toilets"
            id:
                type: number
                description: id of the amenity
                default: 0
            created_at:
                type: datetime string
                description: date and time the amenity was created
                default: '2016-08-11 20:30:38.959846'
            updated_at:
                type: datetime string
                description: date and time the amenity was updated
                default: '2016-08-11 20:30:38.959846'
    """
    amens = Amenity.select().where(Amenity.id == int(amen_id))
    amen = None
    for u in amens:
        amen = u
    if amen == None:
        return error_msg(400, 400, "Error")
    return jsonify(amen.to_dict())

@app.route("/amenities/<amen_id>", methods=["DELETE"])
# @app.route("/amenities/<amen_id>/", methods=["DELETE"])
def delete_one_amenity(amen_id):
    """
    Delete an amenity
    Deletes an amenity based on id.
    ---
    tags:
      - amenity
    responses:
      200:
        description: Success message
        schema:
          id: success_message
          properties:
            status:
              type: number
              description: status code
              default: 200
            msg:
              type: string
              description: Status message
              default: 'Success'
      400:
          description: Error message
          schema:
            id: error_message
            properties:
              status:
                type: number
                description: status code
                default: 400
              msg:
                type: string
                description: Status message
                default: 'Error'
    """
    amens = Amenity.select().where(Amenity.id == int(amen_id))
    amen = None
    for u in amens:
        amen = u
    if amen == None:
        return error_msg(400, 400, "Error")
    amen.delete_instance()
    return error_msg(200, 200, "Success")

@app.route("/places/<place_id>/amenities", methods=["GET"])
def get_amenities_at_place(place_id):
    """
    Get all amenities at a place
    List all amenities at a place.
    ---
    tags:
      - amenity
    parameters:
      - name: place id
        in: query
        type: number
        description: id of the place to search
    responses:
      200:
        description: List of all amenities at place
        schema:
          id: amenities_array
          properties:
            amenities:
              type: array
              description: amenities array
              items:
                properties:
                    name:
                        type: string
                        description: name of the amenity
                        default: "flush toilets"
                    id:
                        type: number
                        description: id of the amenity
                        default: 0
                    created_at:
                        type: datetime string
                        description: date and time the amenity was created
                        default: '2016-08-11 20:30:38.959846'
                    updated_at:
                        type: datetime string
                        description: date and time the amenity was updated
                        default: '2016-08-11 20:30:38.959846'
              default: [{"name": "flush toilets", "id": 0, "created_at": '2016-08-11 20:30:38.959846', "updated_at": '2016-08-11 20:30:38.959846'}, {"name": "hammock", "id": 1, "created_at": '2016-08-11 20:30:38.959846', "updated_at": '2016-08-11 20:30:38.959846'}]
    """
    pas = PlaceAmenities.select().where(PlaceAmenities.place.id == place_id)
    ams = []
    for pa in pas:
        ams.append(pa.amenity.to_dict())
    return jsonify(ams)

@app.route("/places/<place_id>/amenities/<amenity_id>", methods=["POST"])
def create_new_amenity_in_place(place_id, amenity_id):
    """
    Add an amenity to a place
    Adds an amenity to the referenced place.
    ---
    tags:
      - amenity
    responses:
      200:
        description: Success message
        schema:
          id: success_message
          properties:
            status:
              type: number
              description: status code
              default: 200
            msg:
              type: string
              description: Status message
              default: 'Success'
      400:
          description: Error message
          schema:
            id: error_message
            properties:
              status:
                type: number
                description: status code
                default: 400
              msg:
                type: string
                description: Status message
                default: 'Error'
    """
    try:
        pas = PlaceAmenities.select().where(PlaceAmenities.place.id == int(place_id))
        amens = Amenity.select().where(Amenity.id == int(amen_id))
        if pas == None or amens == None:
            raise Exception
        place_amenity = app.models.place_amenity.PlaceAmenities()
        place_amenity.place = pas
        place_amenity.amenity = amens
        place_amenity.save()
    except:
        return error_msg(400, 400, "Error")
    return error_msg(200, 200, "Success")

#TODO
@app.route("/places/<place_id>/amenities/<amenity_id>", methods=["DELETE"])
def delete_amenity_in_place(place_id, amenity_id):
    """
    Remove an amenity from a place
    Removes the specified amenity from the specified place.
    Does not delete the amenity from the database.
    ---
    tags:
      - amenity
    responses:
      200:
        description: Success message
        schema:
          id: success_message
          properties:
            status:
              type: number
              description: status code
              default: 200
            msg:
              type: string
              description: Status message
              default: 'Success'
      400:
          description: Error message
          schema:
            id: error_message
            properties:
              status:
                type: number
                description: status code
                default: 400
              msg:
                type: string
                description: Status message
                default: 'Error'
    """
    pasamen = PlaceAmenities.select().where(PlaceAmenities.place.id == int(place_id) and PlaceAmenities.amenity.id == int(amenity_id))
    amen = None
    for u in pasamen:
        amen = u
    if amen == None:
        return error_msg(400, 400, "Error")
    amen.delete_instance()
    return error_msg(200, 200, "Success")
