import os
from app.controllers.CustomersController import customers_api
from app.controllers.UsersController import users_api
from flask import Flask

os.environ["environment"] = "dev"

from app.core.UserEntity import UserEntity
from app.repositories.database import db_session


app = Flask(__name__)
app.register_blueprint(users_api, url_prefix="/users")
app.register_blueprint(customers_api, url_prefix="/customers")


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.teardown_appcontext
def shut_down_session(exception=None):
    print("end session")
    db_session.remove()


if __name__ == "__main__":
    app.run(debug=True)


