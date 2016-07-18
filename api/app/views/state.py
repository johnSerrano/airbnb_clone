from app import app
from app.models.state import State
from flask import jsonify, request

@app.route("/states", methods=["GET"])
# @app.route("/states/", methods=["GET"])
def get_all_states():
    states = []
    for state in State.select():
        states.append(state.to_hash())
    return jsonify({"states": states})

@app.route("/states", methods=["POST"])
# @app.route("/states/", methods=["POST"])
def create_state():
    content = request.get_json(force=True)
    if not all(param in content.keys() for param in ["name"]):
        #ERROR
        return "Failed: bad input"
    try:
        state = State()
        state.name = content["name"]
        state.save()
    except Exception as e:
        return "Failed"
    return "Success"

@app.route("/states/<state_id>", methods=["GET"])
# @app.route("/states/<state_id>/", methods=["GET"])
def get_statedddd_by_id(state_id):
    if not isinstance(int(state_id), int):
        return "Failed"
    states = State.select().where(State.id == int(state_id))
    state = None
    for u in states:
        state = u
    if state == None:
        return "Failed"
    return jsonify(state.to_hash())


@app.route("/states/<state_id>", methods=["DELETE"])
# @app.route("/states/<state_id>/", methods=["DELETE"])
def delete_statedddd_by_id(state_id):
    try:
        states = State.select().where(State.id == int(state_id))
        state = None
        for u in states:
            state = u
        if state == None:
            return "Failed"
        state.delete_instance()
    except:
        return "Failed"
    return "Success"
