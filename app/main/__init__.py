from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from .config import config_by_name

flask_bcrypt = Bcrypt()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    flask_bcrypt.init_app(app)

    #apply blueprint to the app
    from .controller import auth_controller, material_controller, barcode_controller

    app.register_blueprint(auth_controller.api)
    app.register_blueprint(material_controller.api)
    app.register_blueprint(barcode_controller.api)


    app.add_url_rule("/", endpoint="index")

    return app