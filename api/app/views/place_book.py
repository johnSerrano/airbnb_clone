from app import app
from app.models.place import Place
from app.models.user import User
from app.models.place_book import PlaceBook
from flask import jsonify, request
from app.views.error import error_msg
import datetime

@app.route("/places/<place_id>/books", methods=["GET"])
def get_all_bookings(place_id):
    """
    Get all bookings for a place
    Get all bookings for a place
    ---
    tags:
      - booking
    responses:
      200:
        description: List of all bookings at a place
        schema:
          id: bookings_array
          properties:
            bookings:
              type: array
              description: bookings array
              items:
                properties:
                    place_id:
                        type: number
                        description: id of the place for a booking
                        default: 0
                    user_id:
                        type: number
                        description: id of the user who booked the place
                        default: 0
                    is_validated:
                        type: boolean
                        description: true if the booking has been validated
                        default: false
                    date_start:
                        type: datetime string
                        description: the date of the booking
                        default: '2016-08-11 20:30:38.959846'
                    number_nights:
                        type: number
                        description: duration of the booking
                        default: 1
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
              default: [{"place_id": 0, "user_id": 0, "is_validated": false, "date_start": "2016-08-11 20:30:38.959846", "number_nights": 4, "id": 0, "created_at": "2016-08-11 20:30:38.959846", "updated_at": "2016-08-11 20:30:38.959846"}, {"place_id": 0, "user_id": 0, "is_validated": false, "date_start": "2016-08-16 20:30:38.959846", "number_nights": 4, "id": 0, "created_at": "2016-08-11 20:30:38.959846", "updated_at": "2016-08-11 20:30:38.959846"}]
    """
    books = []
    for book in PlaceBook.select().where(PlaceBook.place == place_id):
        books.append(book.to_dict())
    return jsonify({"books": books})


@app.route("/places/<place_id>/books", methods=["POST"])
def create_new_booking(place_id):
    """
    Create a booking
    Creates a booking based on post parameters.
    ---
    tags:
      - booking
    parameters:
      - name: user
        in: query
        type: number
        description: id of the user who is booking the place
      - name: is_validated
        in: query
        type: boolean
        description: whether the booking has been validated
      - name: date_start
        in: query
        type: date string
        description: date the booking will start
      - name: number_nights
        in: query
        type: number
        description: duration of the booking
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
    if not all(param in content.keys() for param in ["user", "is_validated", "date_start", "number_nights"]):
        #ERROR
        return error_msg(400, 40000, "Missing parameters")
    try:
        users = User.select().where(User.id == int(content['user']))
        user = None
        for u in users:
            user = u
        if user == None:
            return error_msg(400, 400, "user does not exist")
        places = Place.select().where(Place.id == int(place_id))
        place = None
        for u in places:
            place = u
        if place == None:
            return error_msg(400, 400, "place does not exist")
        placebook = PlaceBook()
        placebook.user = user
        placebook.place = place
        placebook.is_validated = content["is_validated"]
        placebook.date_start = datetime.datetime.strptime(content["date_start"], "%Y-%m-%d %H:%M:%S.%f")
        placebook.number_nights = content["number_nights"]
        placebook.save()
    except Exception as e:
        return error_msg(400, 400, "Error")
    return error_msg(200, 200, "Success")


@app.route("/places/<place_id>/books/<book_id>", methods=["GET"])
def get_book_by_id(place_id, book_id):
    """
    Details about one booking
    Get details about one booking
    ---
    tags:
      - booking
    responses:
      200:
        description: Details about one booking
        schema:
          id: booking
          properties:
            place_id:
                type: number
                description: id of the place for a booking
                default: 0
            user_id:
                type: number
                description: id of the user who booked the place
                default: 0
            is_validated:
                type: boolean
                description: true if the booking has been validated
                default: false
            date_start:
                type: datetime string
                description: the date of the booking
                default: '2016-08-11 20:30:38.959846'
            number_nights:
                type: number
                description: duration of the booking
                default: 1
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
    books = PlaceBook.select().where(PlaceBook.id == int(book_id))
    book = None
    for u in books:
        book = u
    if book == None:
        return error_msg(400, 400, "Error")
    return jsonify(book.to_dict())


@app.route("/places/<place_id>/books/<book_id>", methods=["PUT"])
def update_placebook_by_id(place_id, book_id):
    """
    Update a booking
    Updates a booking based on post parameters. All parameters are optional.
    ---
    tags:
      - booking
    parameters:
      - name: user
        in: query
        type: number
        description: id of the user who is booking the place
      - name: is_validated
        in: query
        type: boolean
        description: whether the booking has been validated
      - name: date_start
        in: query
        type: date string
        description: date the booking will start
      - name: number_nights
        in: query
        type: number
        description: duration of the booking
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
    def update_place(book, place_id):
        places = Place.select().where(Place.id == int(place_id))
        place = None
        for u in places:
            place = u
        if place == None:
            return error_msg(400, 400, "place does not exist")
        book.place = place

    def update_valid(book, val):
         book.is_validated = val

    def update_date(book, val):
        book.date_start = val

    def update_nights(book, val):
        book.number_nights = val

    try:
        content = request.get_json(force=True)
        books = PlaceBook.select().where(PlaceBook.id == int(book_id))
        book = None
        for u in books:
            book = u
        if book == None:
            return error_msg(400, 400, "Error")
        for param in content.keys():
            try:
                {
                    "place": update_place,
                    "is_validated": update_valid,
                    "date_start": update_date,
                    "number_nights": update_nights,
                }[param](book, content[param])
            except NameError:
                pass
        book.save()
    except:
        return error_msg(400, 400, "Error")
    return jsonify(book.to_dict())


@app.route("/places/<place_id>/books/<book_id>", methods=["DELETE"])
def delete_book_by_id(place_id, book_id):
    """
    Delete a booking
    Deletes a booking based on id.
    ---
    tags:
      - booking
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
        books = PlaceBook.select().where(PlaceBook.id == int(book_id))
        book = None
        for u in books:
            book = u
        if book == None:
            return error_msg(400, 400, "Error")
        book.delete_instance()
    except:
        return error_msg(400, 400, "Error")
    return error_msg(200, 200, "Success")
