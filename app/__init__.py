import os
from flask import Flask
from models.matching_game_models import db
from dotenv import load_dotenv

def create_app():
    load_dotenv()

    app = Flask(__name__)

    app.config["SQLALCHEMY_ENGINES"] = {
        "default": os.getenv("DATABASE_URL", "sqlite:///characters.db")
    }

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = os.getenv("SECRET_KEY", "dev-fallback-key")

    db.init_app(app)

    from game import game
    app.register_blueprint(game)

    return app