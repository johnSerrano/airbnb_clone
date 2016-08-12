from app import app
from app.models.place import Place
from app.models.city import City
from flask import jsonify, request
from app.views.error import error_msg

@app.route("/places", methods=["GET"])
# @app.route("/places/", method=["GET"])
def get_all_places():
    """
    Get all places
    List all places in the database.
    ---
    tags:
      - place
    responses:
      200:
        description: List of all places
        schema:
          id: places_array
          properties:
            places:
              type: array
              description: places array
              items:
                properties:
                    name:
                        type: string
                        description: name of the place
                        default: "1 bedroom box"
                    owner_id:
                        type: number
                        description: id of the owner
                        default: 0
                    description:
                        type: string
                        description: details about the place
                        default: "A comfy box in an ideal downtown location."
                    number_rooms:
                        type: number
                        description: the number of rooms
                        default: 1
                    number_bathrooms:
                        type: number
                        description: the number of bathrooms
                        default: 0
                    max_guest:
                        type: number
                        description: the maximum number of guests a place can host
                        default: 1
                    price_by_night:
                        type: number
                        description: the price (in dollars) to rent for a night.
                        default: 500
                    latitude:
                        type: float
                        description: the position of the place in latitude
                        default: 0.000
                    longitude:
                        type: float
                        description: the position of the place in longitude
                        default: 0.000
                    id:
                        type: number
                        description: id of the place
                        default: 0
                    created_at:
                        type: datetime string
                        description: date and time the place was created
                        default: '2016-08-11 20:30:38.959846'
                    updated_at:
                        type: datetime string
                        description: date and time the place was updated
                        default: '2016-08-11 20:30:38.959846'
                default: [{"name": "a cool house", "city": 0, "owner": 0, "description": "it's a cool house", "number_rooms": 4, "number_bathrooms": 4, "max_guest": 6, "price_by_night": 150, "latitude": 0.000, "longitude": 0.000, "id": 0, "created_at": '2016-08-11 20:30:38.959846', "updated_at": '2016-08-11 20:30:38.959846'}, {"name": "a cheap house", "city": 0, "owner": 0, "description": "it's a very cheap house. Alley cats provide ambiance.", "number_rooms": 2, "number_bathrooms": 1, "max_guest": 10, "price_by_night": 15, "latitude": 0.000, "longitude": 0.000, "id": 0, "created_at": '2016-08-11 20:30:38.959846', "updated_at": '2016-08-11 20:30:38.959846'}]
    """
    places = []
    for place in Place.select():
        places.append(place.to_dict())
    return jsonify({"places": places})


@app.route("/places", methods=["POST"])
def create_places():
    """
    Create a place
    Creates a place based on post parameters.
    ---
    tags:
      - place
    parameters:
      - name: name
        in: query
        type: string
        description: name of the amenity to create
      - name: city
        in: query
        type: number
        description: id of the city the place is in
      - name: owner
        in: query
        type: number
        description: id of the owner of the place
      - name: description
        in: query
        type: string
        description: details about the place
      - name: number_rooms
        in: query
        type: number
        description: number of bedrooms in place
      - name: number_bathrooms
        in: query
        type: number
        description: number of bathrooms in place
      - name: max_guest
        in: query
        type: number
        description: max number of guests that can stay at a time
      - name: price_by_night
        in: query
        type: number
        description: price (in USD) to stay a night
      - name: latitude
        in: query
        type: float
        description: location of the place in latitude
      - name: longitude
        in: query
        type: float
        description: location of the place in longitude
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
    if not all(param in content.keys() for param in ["name", "city", "owner", "description", "number_rooms", "number_bathrooms", "max_guest", "price_by_night", "latitude", "longitude"]):
        #ERROR
        return error_msg(400, 40000, "Missing parameters")
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
        return error_msg(400, 400, "Error")
    return error_msg(200, 200, "Success")


@app.route("/places/<place_id>", methods=["GET"])
def get_place_by_id_aaa(place_id):
    """
    Get details about one place
    Get details about one place specified by id
    ---
    tags:
      - place
    responses:
      200:
        description: details about one place
        schema:
            id: place
            properties:
                name:
                    type: string
                    description: name of the place
                    default: "1 bedroom box"
                owner_id:
                    type: number
                    description: id of the owner
                    default: 0
                description:
                    type: string
                    description: details about the place
                    default: "A comfy box in an ideal downtown location."
                number_rooms:
                    type: number
                    description: the number of rooms
                    default: 1
                number_bathrooms:
                    type: number
                    description: the number of bathrooms
                    default: 0
                max_guest:
                    type: number
                    description: the maximum number of guests a place can host
                    default: 1
                price_by_night:
                    type: number
                    description: the price (in dollars) to rent for a night.
                    default: 500
                latitude:
                    type: float
                    description: the position of the place in latitude
                    default: 0.000
                longitude:
                    type: float
                    description: the position of the place in longitude
                    default: 0.000
                id:
                    type: number
                    description: id of the place
                    default: 0
                created_at:
                    type: datetime string
                    description: date and time the place was created
                    default: '2016-08-11 20:30:38.959846'
                updated_at:
                    type: datetime string
                    description: date and time the place was updated
                    default: '2016-08-11 20:30:38.959846'
            default: {"name": "a cool house", "city": 0, "owner": 0, "description": "it's a cool house", "number_rooms": 4, "number_bathrooms": 4, "max_guest": 6, "price_by_night": 150, "latitude": 0.000, "longitude": 0.000, "id": 0, "created_at": '2016-08-11 20:30:38.959846', "updated_at": '2016-08-11 20:30:38.959846'}
    """

    if not isinstance(int(place_id), int):
        return error_msg(400, 400, "Error")
    places = Place.select().where(Place.id == int(place_id))
    place = None
    for u in places:
        place = u
    if place == None:
        return error_msg(400, 400, "Error")
    return jsonify(place.to_dict())


@app.route("/places/<place_id>", methods=["PUT"])
def update_place_by_id(place_id):
    """
    Update a place
    Update a place based on post parameters.
    All parameters are optional.
    ---
    tags:
      - place
    parameters:
      - name: name
        in: query
        type: string
        description: name of the amenity to create
      - name: city
        in: query
        type: number
        description: id of the city the place is in
      - name: owner
        in: query
        type: number
        description: id of the owner of the place
      - name: description
        in: query
        type: string
        description: details about the place
      - name: number_rooms
        in: query
        type: number
        description: number of bedrooms in place
      - name: number_bathrooms
        in: query
        type: number
        description: number of bathrooms in place
      - name: max_guest
        in: query
        type: number
        description: max number of guests that can stay at a time
      - name: price_by_night
        in: query
        type: number
        description: price (in USD) to stay a night
      - name: latitude
        in: query
        type: float
        description: location of the place in latitude
      - name: longitude
        in: query
        type: float
        description: location of the place in longitude
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
            return error_msg(400, 400, "Error")
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
        return error_msg(400, 400, "Error")
    return jsonify(place.to_dict())


# AAAAAAAHH!!!!
@app.route("/places/<place_id>", methods=["DELETE"])
def delete_place_by_id(place_id):
    """
    Delete a place
    Deletes a place based on id.
    ---
    tags:
      - place
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
        places = Place.select().where(Place.id == int(place_id))
        place = None
        for u in places:
            place = u
        if place == None:
            return error_msg(400, 400, "Error")
        place.delete_instance()
    except:
        return error_msg(400, 400, "Error")
    return error_msg(200, 200, "Success")


@app.route("/states/<state_id>/cities/<city_id>/places", methods=["GET"])
# @app.route("/states/<state_id>/cities/<city_id>/places/", methods=["GET"])
def get_all_places_hdf(state_id, city_id):
    """
    Get all places in city
    List all places in the specified city.
    ---
    tags:
      - place
    responses:
      200:
        description: List of all places in city
        schema:
          id: places_array
          properties:
            places:
              type: array
              description: places array
              items:
                properties:
                    name:
                        type: string
                        description: name of the place
                        default: "1 bedroom box"
                    owner_id:
                        type: number
                        description: id of the owner
                        default: 0
                    description:
                        type: string
                        description: details about the place
                        default: "A comfy box in an ideal downtown location."
                    number_rooms:
                        type: number
                        description: the number of rooms
                        default: 1
                    number_bathrooms:
                        type: number
                        description: the number of bathrooms
                        default: 0
                    max_guest:
                        type: number
                        description: the maximum number of guests a place can host
                        default: 1
                    price_by_night:
                        type: number
                        description: the price (in dollars) to rent for a night.
                        default: 500
                    latitude:
                        type: float
                        description: the position of the place in latitude
                        default: 0.000
                    longitude:
                        type: float
                        description: the position of the place in longitude
                        default: 0.000
                    id:
                        type: number
                        description: id of the place
                        default: 0
                    created_at:
                        type: datetime string
                        description: date and time the place was created
                        default: '2016-08-11 20:30:38.959846'
                    updated_at:
                        type: datetime string
                        description: date and time the place was updated
                        default: '2016-08-11 20:30:38.959846'
                default: [{"name": "a cool house", "city": 0, "owner": 0, "description": "it's a cool house", "number_rooms": 4, "number_bathrooms": 4, "max_guest": 6, "price_by_night": 150, "latitude": 0.000, "longitude": 0.000, "id": 0, "created_at": '2016-08-11 20:30:38.959846', "updated_at": '2016-08-11 20:30:38.959846'}, {"name": "a cheap house", "city": 0, "owner": 0, "description": "it's a very cheap house. Alley cats provide ambiance.", "number_rooms": 2, "number_bathrooms": 1, "max_guest": 10, "price_by_night": 15, "latitude": 0.000, "longitude": 0.000, "id": 0, "created_at": '2016-08-11 20:30:38.959846', "updated_at": '2016-08-11 20:30:38.959846'}]
    """

    places = []
    for place in Place.select().where(Place.city == city_id):
        places.append(place.to_dict())
    return jsonify({"places": places})


@app.route("/states/<state_id>/cities/<city_id>/places", methods=["POST"])
def create_place_in_city(state_id, city_id):
    """
    Create a place in a city specified by url
    Creates a place based on post parameters and url.
    ---
    tags:
      - place
    parameters:
      - name: name
        in: query
        type: string
        description: name of the amenity to create
      - name: owner
        in: query
        type: number
        description: id of the owner of the place
      - name: description
        in: query
        type: string
        description: details about the place
      - name: number_rooms
        in: query
        type: number
        description: number of bedrooms in place
      - name: number_bathrooms
        in: query
        type: number
        description: number of bathrooms in place
      - name: max_guest
        in: query
        type: number
        description: max number of guests that can stay at a time
      - name: price_by_night
        in: query
        type: number
        description: price (in USD) to stay a night
      - name: latitude
        in: query
        type: float
        description: location of the place in latitude
      - name: longitude
        in: query
        type: float
        description: location of the place in longitude
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
    if not all(param in content.keys() for param in ["name", "owner", "description", "number_rooms", "number_bathrooms", "max_guest", "price_by_night", "latitude", "longitude"]):
        #ERROR
        return error_msg(400, 40000, "Missing parameters")
    try:
        cities = City.select().where(City.id == int(city_id))
        city = None
        for u in cities:
            city = u
        if city == None:
            return error_msg(400, 400, "Error")

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
        return error_msg(400, 400, "Error")
    return error_msg(200, 200, "Success")

#TODO
@app.route("/places/<place_id>/available", methods=["POST"])
def get_available_place(place_id):
    # is place available at (["year", "month", "date"])
    """
    Get place availability at a given date
    Get place availability at a given date
    ---
    tags:
      - place
    parameters:
      - name: year
        in: query
        type: number
        description: year to check
      - name: month
        in: query
        type: number
        description: month to check
      - name: day
        in: query
        type: number
        description: day to check
    responses:
      200:
        description: Success message
        schema:
          id: availability
          properties:
            msg:
              type: boolean
              description: availability status
              default: false
    """
    #TODO finish this method
    content = request.get_json(force=True)
    availability = True
    if not all(param in content.keys() for param in ["year", "month", "day"]):
        return error_msg(400, 40000, "Missing parameters")
    try:
        # try to convert post params to date
        date_to_check = datetime.date(content["year"], content["month"], content["day"])
        # get all bookings for place before date
        # get timedelta for each booking/date
        # compare if timedelta is less than book["number_nights"], return avail.: false
        pass
    except:
        return error_msg(400, 400, "Error")
    return jsonify({"available": availability})

@app.route("/states/<state_id>/places", methods=["GET"])
def get_all_places_feedbull(state_id):
    """
    Get all places in a given state
    List all places in the specified state.
    ---
    tags:
      - place
    responses:
      200:
        description: List of all places
        schema:
          id: places_array
          properties:
            places:
              type: array
              description: places array
              items:
                properties:
                    name:
                        type: string
                        description: name of the place
                        default: "1 bedroom box"
                    owner_id:
                        type: number
                        description: id of the owner
                        default: 0
                    description:
                        type: string
                        description: details about the place
                        default: "A comfy box in an ideal downtown location."
                    number_rooms:
                        type: number
                        description: the number of rooms
                        default: 1
                    number_bathrooms:
                        type: number
                        description: the number of bathrooms
                        default: 0
                    max_guest:
                        type: number
                        description: the maximum number of guests a place can host
                        default: 1
                    price_by_night:
                        type: number
                        description: the price (in dollars) to rent for a night.
                        default: 500
                    latitude:
                        type: float
                        description: the position of the place in latitude
                        default: 0.000
                    longitude:
                        type: float
                        description: the position of the place in longitude
                        default: 0.000
                    id:
                        type: number
                        description: id of the place
                        default: 0
                    created_at:
                        type: datetime string
                        description: date and time the place was created
                        default: '2016-08-11 20:30:38.959846'
                    updated_at:
                        type: datetime string
                        description: date and time the place was updated
                        default: '2016-08-11 20:30:38.959846'
                default: [{"name": "a cool house", "city": 0, "owner": 0, "description": "it's a cool house", "number_rooms": 4, "number_bathrooms": 4, "max_guest": 6, "price_by_night": 150, "latitude": 0.000, "longitude": 0.000, "id": 0, "created_at": '2016-08-11 20:30:38.959846', "updated_at": '2016-08-11 20:30:38.959846'}, {"name": "a cheap house", "city": 0, "owner": 0, "description": "it's a very cheap house. Alley cats provide ambiance.", "number_rooms": 2, "number_bathrooms": 1, "max_guest": 10, "price_by_night": 15, "latitude": 0.000, "longitude": 0.000, "id": 0, "created_at": '2016-08-11 20:30:38.959846', "updated_at": '2016-08-11 20:30:38.959846'}]
    """
    places = []
    # select all cities in state_id
    cities = [city.id for city in City.select().where(City.state_id == state_id)]
    for place in Place.select():
        if place.city not in cities:
            continue
        places.append(place.to_dict())
    return jsonify({"places": places})
