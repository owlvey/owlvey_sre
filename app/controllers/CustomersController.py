from flask import Blueprint


customers_api = Blueprint('customers_api', __name__)


@customers_api.route("/")
def customers_list():
    return "ok customer list"
