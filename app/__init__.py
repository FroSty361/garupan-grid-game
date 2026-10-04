from flask import Flask
from models.models import db

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_ENGINES"] = {
        "default": "sqlite:///characters.db"
    }

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = "Hi!"

    db.init_app(app)

    from game import game
    app.register_blueprint(game)

    return app