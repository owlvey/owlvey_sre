import threading

from flask import Blueprint, request, make_response
from app.components.UsersComponent import UsersComponent
from app.repositories.database import db_init

users_api = Blueprint('users_api', __name__)


@users_api.route("/", methods=["GET"])
def users_list():
    component = UsersComponent()
    return make_response({"data": component.list()}, 200)


@users_api.route("/", methods=["POST"])
def users_create():
    data = request.get_json()
    component = UsersComponent()
    component.create(data)
    return make_response({}, 200)


@users_api.route("/", methods=["PUT"])
def users_update():
    data = request.get_json()
    component = UsersComponent()
    result = component.update(data)
    return make_response(result, 200)


@users_api.route("/", methods=["DELETE"])
def users_delete():
    user_id = request.args.get('user_id')
    component = UsersComponent()
    component.delete(user_id)
    return make_response({}, 200)
