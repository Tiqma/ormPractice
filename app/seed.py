import json
from . import db
from .models import Color
from flask import current_app

def load_colors_from_json(json_path):
    with open(json_path, "r", encoding="utf-8") as f:
        colors = json.load(f)

        added = 0

        for color_name in colors:
            if not Color.query.get(color_name):
                db.session.add(Color(name=color_name))
                added += 1

        db.session.commit()
        return added