import unittest
import json
import requests
from app.models.amenity import Amenity

#these tests appeear to be run in alphabetical order.
#make sure to keep the names alphabetically sorted.

class AirbnbIndexTestCase(unittest.TestCase):
    def setUp(self):
        #connect to db and delete everyone in the amenities table
        Amenity.delete().execute()


    def tearDown(self):
        #delete all from amenities
        Amenity.delete().execute()


    def test_a_create(self):
        #test we can create a amenity
        resp = requests.post('http://localhost:5555/amenities', data=json.dumps({"name": "bathroom"}))
        assert(resp.text=="Success")


    def test_b_list(self):
        #verify we can list all amenities
        self.test_a_create()

        resp = requests.get('http://localhost:5555/amenities')
        data = json.loads(resp.text)
        assert(len(data)==1)


    def test_c_get(self):
        #get one amenity by id
        self.test_a_create()
        resp = requests.get('http://localhost:5555/amenities')
        data = json.loads(resp.text)
        amenity_id = data["amenities"][0]["id"]

        resp = requests.get('http://localhost:5555/amenities/' + str(amenity_id))
        data = json.loads(resp.text)
        assert(data["id"]==amenity_id)


    def test_d_delete(self):
        #test the app returns a 200 code from /
        self.test_a_create()
        resp = requests.get('http://localhost:5555/amenities')
        data = json.loads(resp.text)
        amenity_id = data["amenities"][0]["id"]

        resp = requests.delete('http://localhost:5555/amenities/' + str(amenity_id))
        assert(resp.text=="Success")


        #TODO test get all amenities for a place


if __name__ == '__main__':
    unittest.main()
