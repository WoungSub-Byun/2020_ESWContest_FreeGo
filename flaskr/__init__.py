import os

from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
    )

    #apply blueprint to the app
    from flaskr import auth, material, code

    app.register_blueprint(auth.bp)
    app.register_blueprint(material.bp)
    app.register_blueprint(code.bp)


    app.add_url_rule("/", endpoint="index")

    return app