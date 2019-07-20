from flask import Blueprint, make_response, request

from app.components.CustomersComponent import CustomersComponent

api = Blueprint('customers_api', __name__)


component = CustomersComponent()


@api.route("/", methods=["GET"])
def list_items():
    return make_response({"data": component.list()}, 200)


@api.route("/", methods=["POST"])
def create():
    data = request.get_json()
    component.create(data)
    return make_response({}, 200)


@api.route("/", methods=["PUT"])
def update():
    data = request.get_json()
    result = component.update(data)
    return make_response(result, 200)


@api.route("/", methods=["DELETE"])
def delete():
    user_id = request.args.get('id')
    component.delete(user_id)
    return make_response({}, 200)
