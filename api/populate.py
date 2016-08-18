import sys
import requests
import json
# Populates the test database for testing purposes

def populate_states():
    states = [
        "California",
        "Nevada",
        "Oregon",
        "Washington",
        "Arizona"
    ]
    for state in states:
        resp = requests.post('http://localhost:5555/states', data=json.dumps({"name": state}))
        print resp.status_code,

if __name__ == "__main__":
    action = sys.argv[1]

    actions = {
        "states": populate_states
    }

    if action in actions:
        actions[action]()
    else:
        print("Not a valid action.")
