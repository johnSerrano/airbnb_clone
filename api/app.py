from app import app
from app.models import db
from app.views import *
import config
from flask import jsonify
from werkzeug.contrib.fixers import ProxyFix

@app.before_request
def before_request():
    db.connect()
    pass

@app.after_request
def after_request(resp):
    db.close()
    return resp

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'code': 404,
        'msg': 'not found',
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp

app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == '__main__':
    app.config.update(
        SERVER_NAME = config.HOST + ":" + str(config.PORT),
        DEBUG = config.DEBUG,
    )
    app.run()
