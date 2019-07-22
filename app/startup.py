import os
from app.controllers.CustomersController import api as customers_api
from app.controllers.UsersController import api as users_api
from app.controllers.ProductsController import api as products_api
from app.controllers.SquadsController import api as squads_api
from app.controllers.ServicesController import api as services_api
from app.controllers.FeaturesController import api as features_api

from flask import Flask

os.environ["environment"] = "dev"

from app.repositories.database import db_session

app = Flask(__name__)
app.register_blueprint(users_api)
app.register_blueprint(customers_api)
app.register_blueprint(products_api)
app.register_blueprint(squads_api)
app.register_blueprint(services_api)
app.register_blueprint(features_api)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.teardown_appcontext
def shut_down_session(exception=None):
    db_session.remove()


if __name__ == "__main__":
    app.run(debug=True)


