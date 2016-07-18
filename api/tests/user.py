import unittest
import json
import requests
from app.models.user import User

#these tests appeear to be run in alphabetical order.
#make sure to keep the names alphabetically sorted.

class AirbnbIndexTestCase(unittest.TestCase):
    def setUp(self):
        #connect to db and delete everyone in the users table
        User.delete().execute()


    def tearDown(self):
        #delete all from users
        User.delete().execute()


    def test_a_create(self):
        #test we can create a user
        resp = requests.post('http://localhost:5555/users', data=json.dumps({"email": "test@test.test",
                                                    "password": "TeSt!2#",
                                                    "first_name": "Testy",
                                                    "last_name": "McTest",
                                                    "is_admin": False}))
        assert(resp.text=="Success")


    def test_b_list(self):
        #verify we can list all users
        self.test_a_create()

        resp = requests.get('http://localhost:5555/users')
        data = json.loads(resp.text)
        assert(len(data)==1)

#        self.user_id = data[0]["id"]


    def test_c_get(self):
        #get one user by id
        self.test_a_create()
        resp = requests.get('http://localhost:5555/users')
        data = json.loads(resp.text)
        user_id = data["users"][0]["id"]

        resp = requests.get('http://localhost:5555/users/' + str(user_id))
        data = json.loads(resp.text)
        assert(data["id"]==user_id)

    def test_d_update(self):
        #update a user
        self.test_a_create()
        resp = requests.get('http://localhost:5555/users')
        data = json.loads(resp.text)
        user_id = data["users"][0]["id"]

        resp = requests.put('http://localhost:5555/users/' + str(user_id),
            data=json.dumps({
                "first_name": "TESSSSTTTTTT",
            }))
        assert(resp.text != "Failed")
        resp = requests.get('http://localhost:5555/users/' + str(user_id))
        data = json.loads(resp.text)
        assert(data["first_name"]=="TESSSSTTTTTT")


    def test_e_delete(self):
        #test the app returns a 200 code from /
        self.test_a_create()
        resp = requests.get('http://localhost:5555/users')
        data = json.loads(resp.text)
        user_id = data["users"][0]["id"]

        resp = requests.delete('http://localhost:5555/users/' + str(user_id))
        assert(resp.text=="Success")


if __name__ == '__main__':
    unittest.main()
