from flask import Flask
from flask_json import FlaskJSON
from flasgger import Swagger

app = Flask(__name__)
FlaskJSON(app)
Swagger(app)
