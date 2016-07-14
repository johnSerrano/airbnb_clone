from app import app
import datetime
from flask import jsonify

@app.route("/", methods=["GET"])
def index():
    data = {
        "status": "OK",
        "utc-time": str(datetime.datetime.utcnow()),
        "time": str(datetime.datetime.now()),
    }
    return jsonify(data)
