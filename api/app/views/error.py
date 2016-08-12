from flask import jsonify

def error_msg(code, status, msg):
    """
    A sane function for returning error messages in flask.
    the first parameter, code, is the http status code that will be returned.
    """
    return jsonify({"status": status, "msg": msg}), code
