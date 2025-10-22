from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from app.models import User
from app import db

main = Blueprint('main', __name__)

@main.route("/")
def index():
    return redirect(url_for("main.login"))

@main.route("/register", methods=["GET", "POST"])
def register():
    ...
# (rest of your login/logout/home routes)

