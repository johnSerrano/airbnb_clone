import unittest
import json
import requests
from app.models.state import State

#these tests appeear to be run in alphabetical order.
#make sure to keep the names alphabetically sorted.

class AirbnbIndexTestCase(unittest.TestCase):
    def setUp(self):
        #connect to db and delete everyone in the states table
        State.delete().execute()


    def tearDown(self):
        #delete all from states
        State.delete().execute()


    def test_a_create(self):
        #test we can create a state
        resp = requests.post('http://localhost:5555/states', data=json.dumps({"name": "caulifornia"}))
        assert(resp.status_code == 200)


    def test_b_list(self):
        #verify we can list all states
        self.test_a_create()

        resp = requests.get('http://localhost:5555/states')
        data = json.loads(resp.text)
        assert(len(data)==1)


    def test_c_get(self):
        #get one state by id
        self.test_a_create()
        resp = requests.get('http://localhost:5555/states')
        data = json.loads(resp.text)
        state_id = data["states"][0]["id"]

        resp = requests.get('http://localhost:5555/states/' + str(state_id))
        data = json.loads(resp.text)
        assert(data["id"]==state_id)


    def test_e_delete(self):
        #test the app returns a 200 code from /
        self.test_a_create()
        resp = requests.get('http://localhost:5555/states')
        data = json.loads(resp.text)
        state_id = data["states"][0]["id"]

        resp = requests.delete('http://localhost:5555/states/' + str(state_id))
        assert(resp.status_code == 200)


if __name__ == '__main__':
    unittest.main()
