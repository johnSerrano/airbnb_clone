import unittest
import json
import requests
from app.models.city import City
from app.models.state import State

#these tests appeear to be run in alphabetical order.
#make sure to keep the names alphabetically sorted.
#TODO: need to make state tests before this will work
#ATTN: this may be failing because 'state' is broken

class AirbnbIndexTestCase(unittest.TestCase):
    def setUp(self):
        #connect to db and delete everyone in the cities table
        City.delete().execute()
        State.delete().execute()

    def tearDown(self):
        #delete all from cities
        City.delete().execute()
        State.delete().execute()


    def test_a_create(self):
        #cities need states, so we're going to create one here. If states are broken, cities are too.
        resp = requests.post('http://localhost:5555/states', data=json.dumps({"name": "caulifornia"}))
        resp = requests.get('http://localhost:5555/states')
        data = json.loads(resp.text)
        state_id = data["states"][0]["id"]

        #test we can create a city
        resp = requests.post('http://localhost:5555/states/'+str(state_id)+'/cities', data=json.dumps({"name": "bathroom"}))
        assert(resp.text=="Success")


    def test_b_list(self):
        resp = requests.post('http://localhost:5555/states', data=json.dumps({"name": "caulifornia"}))
        resp = requests.get('http://localhost:5555/states')
        data = json.loads(resp.text)
        state_id = data["states"][0]["id"]

        #verify we can list all cities
        self.test_a_create()

        resp = requests.get('http://localhost:5555/states/'+str(state_id)+'/cities')
        data = json.loads(resp.text)
        assert(len(data)==1)


    def test_c_get(self):
        resp = requests.post('http://localhost:5555/states', data=json.dumps({"name": "caulifornia"}))
        resp = requests.get('http://localhost:5555/states')
        data = json.loads(resp.text)
        state_id = data["states"][0]["id"]

        #get one city by id
        self.test_a_create()
        resp = requests.get('http://localhost:5555/states/'+str(state_id)+'/cities')
        data = json.loads(resp.text)
        city_id = data["cities"][0]["id"]

        resp = requests.get('http://localhost:5555/states/'+str(state_id)+'/cities/' + str(city_id))
        data = json.loads(resp.text)
        assert(data["id"]==city_id)


    def test_d_delete(self):
        resp = requests.post('http://localhost:5555/states', data=json.dumps({"name": "caulifornia"}))
        resp = requests.get('http://localhost:5555/states')
        data = json.loads(resp.text)
        state_id = data["states"][0]["id"]
        
        #test the app returns a 200 code from /
        self.test_a_create()
        resp = requests.get('http://localhost:5555/states/'+str(state_id)+'/cities')
        data = json.loads(resp.text)
        city_id = data["cities"][0]["id"]

        resp = requests.delete('http://localhost:5555/states/'+str(state_id)+'/cities/' + str(city_id))
        assert(resp.text=="Success")


if __name__ == '__main__':
    unittest.main()
