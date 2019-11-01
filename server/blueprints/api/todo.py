from flask import Blueprint, request as current_request

from server.blueprints.base import json_endpoint
from server.db.todo import ToDo

todo_blueprint = Blueprint("todo_blueprint", __name__,
                           url_prefix="/api/todo")


@todo_blueprint.route("/", strict_slashes=False)
@json_endpoint
def find_all():
    return list(ToDo.find_all()), 200


@todo_blueprint.route("/", methods=["PUT", "POST"], strict_slashes=False)
@json_endpoint
def save():
    return ToDo.save_or_update(current_request.get_json()), 201


@todo_blueprint.route("/<doc_id>", methods=["DELETE"], strict_slashes=False)
@json_endpoint
def delete(doc_id):
    ToDo.delete(doc_id)
    return {}, 201
