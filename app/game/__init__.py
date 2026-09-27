from flask import Flask, Blueprint

game = Blueprint("game", __name__, static_folder="../static", template_folder="../templates")

from . import routes