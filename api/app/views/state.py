from app import app
from app.models.state import State
from app.views.error import error_msg
from flask import jsonify, request

@app.route("/states", methods=["GET"])
def get_all_states():
    """
    Get all states
    List all states in the database.
    ---
    tags:
      - state
    responses:
      200:
        description: List of all states
        schema:
          id: states_array
          properties:
            states:
              type: array
              description: states array
              items:
                properties:
                    name:
                        type: string
                        description: name of the state
                        default: "California"
                    id:
                        type: number
                        description: id of the state
                        default: 0
                    created_at:
                        type: datetime string
                        description: date and time the state was created
                        default: '2016-08-11 20:30:38.959846'
                    updated_at:
                        type: datetime string
                        description: date and time the state was updated
                        default: '2016-08-11 20:30:38.959846'
              default: [{"name": "California", "id": 0, "created_at": '2016-08-11 20:30:38.959846', "updated_at": '2016-08-11 20:30:38.959846'}, {"name": "hammock", "id": 1, "created_at": '2016-08-11 20:30:38.959846', "updated_at": '2016-08-11 20:30:38.959846'}]
    """
    states = []
    for state in State.select():
        states.append(state.to_dict())
    return jsonify({"states": states})

@app.route("/states", methods=["POST"])
# @app.route("/states/", methods=["POST"])
def create_state():
    """
    Create a state
    Creates a state based on post parameters.
    ---
    tags:
      - state
    parameters:
      - name: name
        in: query
        type: string
        description: name of the state to create
    responses:
      200:
        description: Success message
        schema:
          id: success_message
          properties:
            status:
              type: number
              description: status code
              default: 200
            msg:
              type: string
              description: Status message
              default: 'Success'
      400:
          description: Error message
          schema:
            id: error_message
            properties:
              status:
                type: number
                description: status code
                default: 40000
              msg:
                type: string
                description: Status message
                default: 'Missing parameters'
    """
    content = request.get_json(force=True)
    if not all(param in content.keys() for param in ["name"]):
        #ERROR
        return error_msg(400, 40000, "Missing parameters")
    try:
        state = State()
        state.name = content["name"]
        state.save()
    except Exception as e:
        return error_msg(400, 400, "Error")
    return error_msg(200, 200, "Success")

@app.route("/states/<state_id>", methods=["GET"])
def get_statedddd_by_id(state_id):
    """
    Get one state
    Returns information about one state.
    ---
    tags:
      - state
    responses:
      200:
        description: Information about one state
        schema:
          id: amenity
          properties:
            name:
                type: string
                description: name of the state
                default: "California"
            id:
                type: number
                description: id of the state
                default: 0
            created_at:
                type: datetime string
                description: date and time the state was created
                default: '2016-08-11 20:30:38.959846'
            updated_at:
                type: datetime string
                description: date and time the state was updated
                default: '2016-08-11 20:30:38.959846'
    """
    if not isinstance(int(state_id), int):
        return error_msg(400, 400, "Error")
    states = State.select().where(State.id == int(state_id))
    state = None
    for u in states:
        state = u
    if state == None:
        return error_msg(400, 400, "Error")
    return jsonify(state.to_dict())


@app.route("/states/<state_id>", methods=["DELETE"])
# @app.route("/states/<state_id>/", methods=["DELETE"])
def delete_one_state(state_id):
    """
    Delete an state
    Deletes an state based on id.
    ---
    tags:
      - state
    responses:
      200:
        description: Success message
        schema:
          id: success_message
          properties:
            status:
              type: number
              description: status code
              default: 200
            msg:
              type: string
              description: Status message
              default: 'Success'
      400:
          description: Error message
          schema:
            id: error_message
            properties:
              status:
                type: number
                description: status code
                default: 400
              msg:
                type: string
                description: Status message
                default: 'Error'
    """
    try:
        states = State.select().where(State.id == int(state_id))
        state = None
        for u in states:
            state = u
        if state == None:
            return error_msg(400, 400, "Error")
        state.delete_instance()
    except:
        return error_msg(400, 400, "Error")
    return error_msg(200, 200, "Success")
