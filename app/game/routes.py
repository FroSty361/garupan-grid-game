from flask import render_template
from . import game
from sqlalchemy import select
from models.models import db, Character


@game.route("/")
def index():
    character_statement = select(Character).where(Character.name == "Miho Nishizumi|Miporin")
    character = db.session.scalars(character_statement).first()

    return render_template("game/index.html", text=character.attributes[0].category_name)