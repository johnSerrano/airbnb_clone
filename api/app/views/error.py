from flask import jsonify

#TODO: create a framework for error messages
def error_msg(code, status, msg):
    return jsonify({"status": status, "msg": msg}), code
