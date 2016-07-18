import unittest
import json
import requests
import datetime

class AirbnbIndexTestCase(unittest.TestCase):
    create_ran = False

    def setUp(self):
        #delete all from users
        pass

    def tearDown(self):
        #delete all from users
        pass

    def test_create(self):
        #test we can create a user
        resp = requests.post('http://localhost:5555/users/', data={"email": "test@test.test",
                                                    "password": "TeSt!2#",
                                                    "first_name": "Testy",
                                                    "last_name": "McTest",
                                                    "is_admin": False})
        assert(resp.text=="Success")


    def test_list(self):
        #test the app returns a 200 code from /
        resp = requests.get('http://localhost:5555/users/')


    def test_get(self):
        #test the app returns a 200 code from /
        resp = requests.get('http://localhost:5555/')


    def test_delete(self):
        #test the app returns a 200 code from /
        resp = requests.delete('http://localhost:5555/')


    def test_update(self):
        #test the app returns a 200 code from /
        resp = requests.put('http://localhost:5555/', data={})


if __name__ == '__main__':
    unittest.main()
