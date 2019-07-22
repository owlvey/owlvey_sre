from flask import Blueprint, request, make_response

from app.components.FeaturesComponent import FeaturesComponent
from app.components.SquadsComponent import SquadsComponent


api = Blueprint('features_api', __name__)

component = FeaturesComponent()


url_prefix = "/features"


@api.route(url_prefix, methods=["GET"])
def list_items():
    return make_response({"data": component.list()}, 200)


@api.route(url_prefix + "/<key>", methods=["GET"])
def get_item(key):
    return make_response(component.get(key), 200)


@api.route(url_prefix, methods=["POST"])
def create():
    data = request.get_json()
    component.create(data)
    return make_response({}, 200)


@api.route(url_prefix, methods=["PUT"])
def update():
    data = request.get_json()
    result = component.update(data)
    return make_response(result, 200)


@api.route(url_prefix + "/<key>", methods=["DELETE"])
def delete(key):
    component.delete(key)
    return make_response({}, 200)
