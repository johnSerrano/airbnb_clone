import unittest
import json
import requests
import datetime

class AirbnbIndexTestCase(unittest.TestCase):
    def test_200(self):
        #test the app returns a 200 code from /
        resp = requests.get('http://localhost:5555/')
        assert resp.status_code == 200


    def test_status(self):
        #verify the 'status' field of the response json is 'OK'
        resp = requests.get('http://localhost:5555/')
        data = json.loads(resp.text)
        assert data['status'] == 'OK'


    def test_time(self):
        #verify the 'time' field of the response json is correct
        resp = requests.get('http://localhost:5555/')
        data = json.loads(resp.text)
        dt = datetime.datetime.strptime(data['time'], "%Y-%m-%d %H:%M:%S.%f")
        assert (datetime.datetime.now() - dt) < datetime.timedelta(minutes=1)


    def test_time_utc(self):
        #verify the 'utc_time' field of the response json is correct
        resp = requests.get('http://localhost:5555/')
        data = json.loads(resp.text)
        dt = datetime.datetime.strptime(data['utc-time'], "%Y-%m-%d %H:%M:%S.%f")
        assert (datetime.datetime.utcnow() - dt) < datetime.timedelta(minutes=1)


if __name__ == '__main__':
    unittest.main()
