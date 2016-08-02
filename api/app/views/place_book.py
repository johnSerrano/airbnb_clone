from app import app
from app.models.place import Place
from app.models.user import User
from app.models.place_book import PlaceBook
from flask import jsonify, request
from app.views.error import error_msg
import datetime

@app.route("/places/<place_id>/books", methods=["GET"])
# @app.route("/places/<place_id>/books/", methods=["GET"])
def get_all_bookings(place_id):
    books = []
    for book in PlaceBook.select().where(PlaceBook.place == place_id):
        books.append(book.to_dict())
    return jsonify({"books": books})


@app.route("/places/<place_id>/books", methods=["POST"])
# @app.route("/places/<place_id>/books/", methods=["POST"])
def create_new_booking(place_id):
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
# @app.route("/places/<place_id>/books/<book_id>/", methods=["GET"])
def get_book_by_id(place_id, book_id):
    books = PlaceBook.select().where(PlaceBook.id == int(book_id))
    book = None
    for u in books:
        book = u
    if book == None:
        return error_msg(400, 400, "Error")
    return jsonify(book.to_dict())


@app.route("/places/<place_id>/books/<book_id>", methods=["PUT"])
# @app.route("/places/<place_id>/books/<book_id>/", methods=["PUT"])
def update_placebook_by_id(place_id, book_id):
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

    # try:
    if True:
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
    # except:
    #     return error_msg(400, 400, "Error")
    return jsonify(book.to_dict())


@app.route("/places/<place_id>/books/<book_id>", methods=["DELETE"])
# @app.route("/places/<place_id>/books/<book_id>/", methods=["DELETE"])
def delete_book_by_id(place_id, book_id):
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
