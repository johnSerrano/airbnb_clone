from app import app
import datetime
from flask import jsonify
from app.views.error import error_msg

@app.route("/", methods=["GET"])
def index():
    """
    This is the index. It returns the current time in utc and local.
    Use it to check things are working.
    ---
    tags:
      - index
    responses:
      200:
        description: Current time
        schema:
          id: current_time
          properties:
            status:
              type: string
              description: Status of the api
              default: 'OK'
            time:
              type: datetime string
              description: current local time of the server
              default: '2016-08-11 13:30:38.959883'
            utc-time:
              type: datetime string
              description: current UTC time
              default: '2016-08-11 20:30:38.959846'
    """
    data = {
        "status": "OK",
        "utc-time": str(datetime.datetime.utcnow()),
        "time": str(datetime.datetime.now()),
    }
    return jsonify(data)
