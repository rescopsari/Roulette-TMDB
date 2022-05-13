import sys

from flask_cors import CORS
from flask import Flask

if sys.platform != "win32":
    path = "/opt/flask_app/"
    sys.path.append(path)
else:
    path = ""
from api.get_random import get_random

app = Flask(__name__)
CORS(app)


@app.route('/movie')
def movie():
    return get_random("movie")


@app.route('/tv')
def tv():
    return get_random("tv")
