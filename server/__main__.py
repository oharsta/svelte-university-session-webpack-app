import logging
import os
import sys

import yaml
from flask import Flask
from flask_pymongo import PyMongo
from munch import munchify

from server.blueprints.api.todo import todo_blueprint

logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)


def read_file(file_name):
    file = f"{os.path.dirname(os.path.realpath(__file__))}/{file_name}"
    with open(file) as f:
        return f.read()


config_file = os.environ.get("CONFIG", "config.yml")
config_file_location = f"config/{config_file}"
config = munchify(yaml.load(read_file(config_file_location), Loader=yaml.FullLoader))

app = Flask(__name__)
app.secret_key = config.secret_key

app.config.update({
    "MONGO_URI": config.database.uri,
})

app.app_config = config

app.mongo = PyMongo(app)

app.register_blueprint(todo_blueprint)

# WSGI production mode dictates that no flask app is actually running
if __name__ == "__main__":
    app.run(port=8080, debug=False, host="localhost", threaded=True)
