from flask import render_template, request, jsonify
from . import game
from sqlalchemy import select
from models.models import db, Character
from servcies.ui_utils import character_search

@game.route("/")
def index():
    return render_template("game/index.html")

@game.route('/api/game/check-character-name', methods=['POST'])
def auto_check_character():
    data = request.get_json()

    character_name = data.get("character_name")

    matched_character_names = character_search(character_name)

    return jsonify({'success': True, 'result': matched_character_names})