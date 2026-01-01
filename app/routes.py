from flask import Blueprint, redirect, render_template, request, url_for
from .models import User, Color
from . import db

main = Blueprint('main', __name__)

@main.route("/")
def home():
    users = User.query.all()
    colors = Color.query.all()
    return render_template("index.html", users=users, colors=colors)

@main.route("/add_user_route", methods=["GET"])
def add_user():
    username = request.args.get("username")
    email = request.args.get("email")
    if username and email:
        user = User(username=username, email=email)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('main.home'))
    return "Invalid input."

@main.route("/remove_user_route", methods=["POST"])
def remove_user():
    username = request.form.get("username")

    user = User.query.filter_by(username=username).first()
    if username:
        db.session.delete(user)
        db.session.commit()
        return redirect(url_for('main.home'))
    return "Invalid input."

@main.route("/chosen_color/<int:user_id>/<color_name>")
def choose_color(user_id, color_name):
    user = User.query.get(user_id)
    if user:
        user.color_name = color_name
        db.session.commit()
    return redirect(url_for('main.home'))

@main.route("/choose_color_form", methods=["GET"])
def choose_color_form():
    user_id = request.args.get("user_id", type=int)
    color_name = request.args.get("color_name")
    if user_id and color_name:
        return redirect(url_for('main.choose_color', user_id=user_id, color_name=color_name))
    return "Invalid input."

@main.route("/reset_colors", methods=["GET"])
def reset_colors():
    users = User.query.all()
    for user in users:
        user.color_name = None
    db.session.commit()
    return redirect(url_for('main.home'))
