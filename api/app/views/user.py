from app import app
from app.models.user import User
from flask import jsonify, request
from app.views.error import error_msg

@app.route("/users", methods=["GET"])
def get_all_users():
    """
    Get all users
    List all users in the database.
    ---
    tags:
      - user
    responses:
      200:
        description: List of all users
        schema:
          id: users_array
          properties:
            amenities:
              type: array
              description: users array
              items:
                properties:
                    first_name:
                        type: string
                        description: name of the user
                        default: "George"
                    last_name:
                        type: string
                        description: name of the user
                        default: "Washington"
                    email:
                        type: string
                        description: main contant email
                        default: "george.washington@usa.gov"
                    is_admin:
                        type: boolean
                        description: does the user have admin rights?
                    id:
                        type: number
                        description: id of the user
                        default: 0
                    created_at:
                        type: datetime string
                        description: date and time the user was created (not birthday)
                        default: '2016-08-11 20:30:38.959846'
                    updated_at:
                        type: datetime string
                        description: date and time the user was updated
                        default: '2016-08-11 20:30:38.959846'
              default: [{"name": "flush toilets", "id": 0, "created_at": '2016-08-11 20:30:38.959846', "updated_at": '2016-08-11 20:30:38.959846'}, {"name": "hammock", "id": 1, "created_at": '2016-08-11 20:30:38.959846', "updated_at": '2016-08-11 20:30:38.959846'}]
    """
    users = []
    for user in User.select():
        users.append(user.to_dict())
    return jsonify({"users": users})

@app.route("/users", methods=["POST"])
def create_user():
    """
    Create a user
    Creates an user based on post parameters.
    ---
    tags:
      - user
    parameters:
      - name: first_name
        in: query
        type: string
        description: name of the user to create
      - name: last_name
        in: query
        type: string
        description: name of the user to create
      - name: email
        in: query
        type: string
        description: email of the user to create
      - name: is_admin
        in: query
        type: boolean
        description: if true the user has admin rights
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
    if not content:
        error_msg(400, 400, "Error")
    if not all(param in content.keys() for param in ["email", "password", "first_name", "last_name", "is_admin"]):
        #ERROR
        return error_msg(400, 40000, "Missing parameters")
    try:
        user = User()
        user.email = content["email"]
        user.first_name = content["first_name"]
        user.last_name = content["last_name"]
        user.is_admin = content["is_admin"]
        user.set_password(content["password"])
        user.save()
    except Exception as e:
        print e
        return error_msg(400, 400, "Error")
    return error_msg(200, 200, "Success")

@app.route("/users/<user_id>", methods=["GET"])
def get_user_by_id(user_id):
    """
    Get one users
    get details about one user.
    ---
    tags:
      - user
    responses:
      200:
        description: details about one user
        schema:
            id: user
            properties:
                first_name:
                    type: string
                    description: name of the user
                    default: "George"
                last_name:
                    type: string
                    description: name of the user
                    default: "Washington"
                email:
                    type: string
                    description: main contant email
                    default: "george.washington@usa.gov"
                is_admin:
                    type: boolean
                    description: does the user have admin rights?
                id:
                    type: number
                    description: id of the user
                    default: 0
                created_at:
                    type: datetime string
                    description: date and time the user was created (not birthday)
                    default: '2016-08-11 20:30:38.959846'
                updated_at:
                    type: datetime string
                    description: date and time the user was updated
                    default: '2016-08-11 20:30:38.959846'
    """
    if not isinstance(int(user_id), int):
        return error_msg(400, 400, "Error")
    users = User.select().where(User.id == int(user_id))
    user = None
    for u in users:
        user = u
    if user == None:
        return error_msg(400, 400, "Error")
    return jsonify(user.to_dict())

@app.route("/users/<user_id>", methods=["PUT"])
def update_user_by_id(user_id):
    """
    Update a user
    Update an user based on post parameters.
    All parameters are optional
    ---
    tags:
      - user
    parameters:
      - name: first_name
        in: query
        type: string
        description: name of the user to create
      - name: last_name
        in: query
        type: string
        description: name of the user to create
      - name: email
        in: query
        type: string
        description: email of the user to create
      - name: is_admin
        in: query
        type: boolean
        description: if true the user has admin rights
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
    def update_password(user, newpass):
        user.set_password(newpass)

    def update_first_name(user, newname):
        user.first_name = newname

    def update_last_name(user, newname):
        user.last_name = newname

    def update_admin(user, newrights):
        user.is_admin = newrights

    # try:
    content = request.get_json(force=True)
    if not content:
        return error_msg(400, 400, "Error")
    users = User.select().where(User.id == int(user_id))
    user = None
    for u in users:
        user = u
    if user == None:
        return error_msg(400, 400, "Error")
    for param in content.keys():
        try:
            {
                "password": update_password,
                "first_name": update_first_name,
                "last_name": update_last_name,
                "is_admin": update_admin,
            }[param](user, content[param])
        except NameError:
            pass
    user.save()
    # except Exception as e:
    return jsonify(user.to_dict())

# AAAAAAAHH!!!!
@app.route("/users/<user_id>", methods=["DELETE"])
def delete_user_by_id(user_id):
    """
    Delete a user
    Deletes an user based on id.
    ---
    tags:
      - user
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
        users = User.select().where(User.id == int(user_id))
        user = None
        for u in users:
            user = u
        if user == None:
            return error_msg(400, 400, "Error")
        user.delete_instance()
    except:
        return error_msg(400, 400, "Error")
    return error_msg(200, 200, "Success")
