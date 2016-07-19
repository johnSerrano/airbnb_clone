import unittest
import json
import requests
from app.models.place import Place
from app.models.user import User
from app.models.city import City
from app.models.state import State

#these tests appeear to be run in alphabetical order.
#make sure to keep the names alphabetically sorted.

class AirbnbIndexTestCase(unittest.TestCase):
    def setUp(self):
        #connect to db and delete everyone in the places table
        Place.delete().execute()
        User.delete().execute()
        City.delete().execute()
        State.delete().execute()


    def tearDown(self):
        #delete all from places
        Place.delete().execute()
        User.delete().execute()
        City.delete().execute()
        State.delete().execute()


    def test_a_create(self):
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
        resp = requests.post('http://localhost:5555/users', data=json.dumps({"email": "test@test.test",
                                                            "password": "TeSt!2#",
                                                            "first_name": "Testy",
                                                            "last_name": "McTest",
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
        assert(resp.text=="Success")


    def test_b_list(self):
        #verify we can list all places
        self.test_a_create()

        resp = requests.get('http://localhost:5555/places')
        data = json.loads(resp.text)
        assert(len(data)==1)


    def test_c_get(self):
        #get one place by id
        self.test_a_create()
        resp = requests.get('http://localhost:5555/places')
        data = json.loads(resp.text)
        place_id = data["places"][0]["id"]

        resp = requests.get('http://localhost:5555/places/' + str(place_id))
        data = json.loads(resp.text)
        assert(data["id"]==place_id)


    def test_d_create(self):
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
        resp = requests.post('http://localhost:5555/users', data=json.dumps({"email": "tessst@test.test",
                                                            "password": "TeSt!2#",
                                                            "first_name": "Testy",
                                                            "last_name": "McTest",
                                                            "is_admin": False}))
        resp = requests.get('http://localhost:5555/users')
        data = json.loads(resp.text)
        user_id = data["users"][0]["id"]

        #test we can create a place
        resp = requests.post('http://localhost:5555/states/'+str(state_id)+'/cities/'+str(city_id)+'/places', data=json.dumps(
            {
                "name": "Barracks",
                "owner": user_id,
                "description": "Its cool",
                "number_rooms": 150,
                "number_bathrooms": 2,
                "max_guest": 300,
                "price_by_night": 3500,
                "latitude": 14.443,
                "longitude": 123.321,
            }))
        assert(resp.text=="Success")


    def test_e_list(self):
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
        resp = requests.post('http://localhost:5555/users', data=json.dumps({"email": "test@test.test",
                                                            "password": "TeSt!2#",
                                                            "first_name": "Testy",
                                                            "last_name": "McTest",
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

        resp = requests.get('http://localhost:5555/states/'+str(state_id)+'/cities/'+str(city_id)+'/places')


    def test_f_delete(self):
        #test the app returns a 200 code from /
        self.test_a_create()
        resp = requests.get('http://localhost:5555/places')
        data = json.loads(resp.text)
        place_id = data["places"][0]["id"]

        resp = requests.delete('http://localhost:5555/places/' + str(place_id))
        assert(resp.text=="Success")


if __name__ == '__main__':
    unittest.main()
