from app import app
from app.models.state import State
from app.models.city import City
from app.views.error import error_msg
from flask import jsonify, request

@app.route("/states/<state_id>/cities", methods=["GET"])
def get_all_cities(state_id):
    """
    Get all cities in a state
    List all cities in the specified state.
    ---
    tags:
      - city
    responses:
      200:
        description: List of all cities in state
        schema:
          id: cities_array
          properties:
            cities:
              type: array
              description: cities array
              items:
                properties:
                    name:
                        type: string
                        description: name of the city
                        default: "San Jose"
                    state_id:
                        type: number
                        description: id of the state which the city is in
                        default: 0
                    id:
                        type: number
                        description: id of the city
                        default: 0
                    created_at:
                        type: datetime string
                        description: date and time the city was created (in the database, not when it was founded)
                        default: '2016-08-11 20:30:38.959846'
                    updated_at:
                        type: datetime string
                        description: date and time the city was updated
                        default: '2016-08-11 20:30:38.959846'
              default: [{"name": "San Francisco", "state_id": 5, "id": 0, "created_at": '2016-08-11 20:30:38.959846', "updated_at": '2016-08-11 20:30:38.959846'}, {"name": "San Jose", "state_id": 5, "id": 1, "created_at": '2016-08-11 20:30:38.959846', "updated_at": '2016-08-11 20:30:38.959846'}]
    """
    cities = []
    for city in City.select().where(City.state == state_id):
        cities.append(city.to_dict())
    return jsonify({"cities": cities})

@app.route("/states/<state_id>/cities", methods=["POST"])
def create_city(state_id):
    """
    Create an city
    Creates an city based on post parameters.
    ---
    tags:
      - city
    parameters:
      - name: name
        in: query
        type: string
        description: name of the city to create
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
    if not all(param in content.keys() for param in ["name"]):
        #ERROR
        return error_msg(400, 40000, "Missing parameters")
    try:
        city = City()
        city.name = content["name"]
        city.state = state_id
        city.save()
    except Exception as e:
        return error_msg(400, 400, "Error")
    return error_msg(200, 200, "Success")

@app.route("/states/<state_id>/cities/<city_id>", methods=["GET"])
def get_city_by_id(state_id, city_id):
    """
    Get information about one city
    Returns information about the specified city
    ---
    tags:
      - city
    responses:
      200:
        description: List of all cities in state
        schema:
          id: city
          properties:
              name:
                  type: string
                  description: name of the city
                  default: "San Jose"
              state_id:
                  type: number
                  description: id of the state which the city is in
                  default: 0
              id:
                  type: number
                  description: id of the city
                  default: 0
              created_at:
                  type: datetime string
                  description: date and time the city was created (in the database, not when it was founded)
                  default: '2016-08-11 20:30:38.959846'
              updated_at:
                  type: datetime string
                  description: date and time the city was updated
                  default: '2016-08-11 20:30:38.959846'
    """
    if not isinstance(int(city_id), int):
        return error_msg(400, 400, "Error")
    cities = City.select().where(City.id == int(city_id))
    city = None
    for u in cities:
        city = u
    if city == None:
        return error_msg(400, 400, "Error")
    return jsonify(city.to_dict())


@app.route("/states/<state_id>/cities/<city_id>", methods=["DELETE"])
def delete_city_by_id(state_id, city_id):
    """
    Delete a city
    Deletes a city based on id.
    ---
    tags:
      - city
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
        cities = City.select().where(City.id == int(city_id))
        city = None
        for u in cities:
            city = u
        if city == None:
            return error_msg(400, 400, "Error")
        city.delete_instance()
    except:
        return error_msg(400, 400, "Error")
    return error_msg(200, 200, "Success")
