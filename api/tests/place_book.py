import unittest
import json
import requests
from app.models.place_book import PlaceBook
from app.models.user import User
from app.models.place import Place
from app.models.state import State
from app.models.city import City
import datetime

#these tests appeear to be run in alphabetical order.
#make sure to keep the names alphabetically sorted.

def get_user():
    resp = requests.post('http://localhost:5555/users', data=json.dumps({"email": "test@test.test",
                                                "password": "TeSt!2#",
                                                "first_name": "Testy",
                                                "last_name": "McTest",
                                                "is_admin": False}))
    resp = requests.get('http://localhost:5555/users')
    data = json.loads(resp.text)
    user_id = data["users"][0]["id"]
    return user_id

def get_place():
    #create state
    resp = requests.post('http://localhost:5555/states', data=json.dumps({"name": "caulifornia"}))
    resp = requests.get('http://localhost:5555/states')
    data = json.loads(resp.text)
    state_id = data["states"][0]["id"]
    #create city
    resp = requests.post('http://localhost:5555/states/'+str(state_id)+'/cities', data=json.dumps({"name": "africa"}))
    resp = requests.get('http://localhost:5555/states/'+str(state_id)+'/cities')
    data = json.loads(resp.text)
    city_id = data["cities"][0]["id"]
    #create user (owner)
    resp = requests.post('http://localhost:5555/users', data=json.dumps({"email": "owner@test.test",
                                                    "password": "TeSt!2#",
                                                    "first_name": "Lordy",
                                                    "last_name": "McLandlord",
                                                    "is_admin": False}))
    resp = requests.get('http://localhost:5555/users')
    data = json.loads(resp.text)
    user_id = data["users"][0]["id"]

    #test we can create a place
    resp = requests.post('http://localhost:5555/places', data=json.dumps(
        {
            "name": "Barracks",
            "city": city_id,
            "owner": user_id,
            "description": "Its cool",
            "number_rooms": 150,
            "number_bathrooms": 2,
            "max_guest": 300,
            "price_by_night": 3500,
            "latitude": 14.443,
            "longitude": 123.321,
        }))

    resp = requests.get('http://localhost:5555/places')
    data = json.loads(resp.text)
    place_id = data["places"][0]["id"]
    return place_id


class AirbnbIndexTestCase(unittest.TestCase):
    def setUp(self):
        #connect to db and delete everyone in the users table
        PlaceBook.delete().execute()
        Place.delete().execute()
        User.delete().execute()
        City.delete().execute()
        State.delete().execute()


    def tearDown(self):
        #delete all from users
        PlaceBook.delete().execute()
        Place.delete().execute()
        User.delete().execute()
        City.delete().execute()
        State.delete().execute()


    def test_a_create(self):
        #test we can create a user
        user_id = get_user()
        place_id = get_place()
        resp = requests.post('http://localhost:5555/places/'+str(place_id)+'/books',
                                data=json.dumps({"user": user_id,
                                                "is_validated": False,
                                                "date_start": str(datetime.datetime.now()),
                                                "number_nights": 5}))
        assert(resp.text=="Success")


    def test_b_list(self):
        #verify we can list all users
        self.test_a_create()
        resp = requests.get('http://localhost:5555/places')
        data = json.loads(resp.text)
        place_id = data["places"][0]["id"]

        resp = requests.get('http://localhost:5555/places/'+str(place_id)+'/books')
        data = json.loads(resp.text)
        assert(len(data)==1)


    def test_c_get(self):
        #get one user by id
        self.test_a_create()

        resp = requests.get('http://localhost:5555/places')
        data = json.loads(resp.text)
        place_id = data["places"][0]["id"]

        resp = requests.get('http://localhost:5555/places/'+str(place_id)+'/books')
        data = json.loads(resp.text)
        book_id = data["books"][0]["id"]

        resp = requests.get('http://localhost:5555/places/'+str(place_id)+'/books/' + str(book_id))
        data = json.loads(resp.text)
        assert(data["id"]==book_id)


    def test_d_update(self):
        #update a user
        self.test_a_create()

        resp = requests.get('http://localhost:5555/places')
        data = json.loads(resp.text)
        place_id = data["places"][0]["id"]

        resp = requests.get('http://localhost:5555/places/'+str(place_id)+'/books')
        data = json.loads(resp.text)
        book_id = data["books"][0]["id"]

        resp = requests.put('http://localhost:5555/places/'+str(place_id)+'/books/' + str(book_id),
            data=json.dumps({
                "is_validated": True,
            }))
        assert(resp.text != "Failed")
        resp = requests.get('http://localhost:5555/places/'+str(place_id)+'/books/' + str(book_id))
        data = json.loads(resp.text)
        assert(data["is_validated"]==True)


    def test_e_delete(self):
        #test the app returns a 200 code from /
        self.test_a_create()

        resp = requests.get('http://localhost:5555/places')
        data = json.loads(resp.text)
        place_id = data["places"][0]["id"]

        resp = requests.get('http://localhost:5555/places/'+str(place_id)+'/books')
        data = json.loads(resp.text)
        book_id = data["books"][0]["id"]

        resp = requests.delete('http://localhost:5555/places/'+str(place_id)+'/books/' + str(book_id))
        assert(resp.text=="Success")


if __name__ == '__main__':
    unittest.main()
