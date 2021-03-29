from flask import Blueprint

hello_world_bp = Blueprint("hello_world_bp", __name__)


@hello_world_bp.route("/hello-world", methods=["GET"])
def hello_world():
    return "Hello, World!"


@hello_world_bp.route("/hello/JSON", methods=["GET"])
def hello_json():
    return {
        "name": "Ada Lovelace",
        "message": "Hello!",
        "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"]
    }
